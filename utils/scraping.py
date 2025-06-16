# utils/scraping.py

from playwright.sync_api import sync_playwright
import os

def scrape_and_screenshot(url, output_folder="screenshots", html_save_path="data/chapter1.html"):
    # Ensure folders exist
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.dirname(html_save_path), exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Save screenshot
        screenshot_path = os.path.join(output_folder, "chapter1_screenshot.png")
        page.screenshot(path=screenshot_path, full_page=True)

        # Save HTML content
        with open(html_save_path, "w", encoding="utf-8") as f:
            f.write(page.content())

        browser.close()

    print(f"[✓] Screenshot saved to: {screenshot_path}")
    print(f"[✓] HTML content saved to: {html_save_path}")
