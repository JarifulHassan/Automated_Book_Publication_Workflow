from utils.scraping import scrape_and_screenshot
from ai_writer import configure_gemini, rewrite_chapter
from bs4 import BeautifulSoup
import os
from gui.reviewer import review_and_edit  # GUI Editor
from db.knowledge import store_chapter, search_chapter

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    chapter_id = "chapter1"

    print("[✓] Scraping and taking screenshot...")
    scrape_and_screenshot(url)

    print("[✓] Configuring Gemini...")
    API_KEY = "AIzaSyAyquhd-oe4G4wP2GRdWuK95Vdvjdt8QJA"
    configure_gemini(API_KEY)

    # Load HTML content
    with open("data/chapter1.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    clean_text = soup.get_text(separator="\n", strip=True)

    print("[✓] Rewriting chapter using Gemini...")
    spun_text = rewrite_chapter(clean_text)

    os.makedirs("output", exist_ok=True)
    output_path = f"output/{chapter_id}_final.txt"

    print("[*] Launching review window. Please edit and save manually.")
    review_and_edit(spun_text, output_path)
    print(f"[✓] Chapter saved to {output_path}")

    # Load the reviewed/edited content
    with open(output_path, "r", encoding="utf-8") as f:
        final_text = f.read()

    # Store final version to ChromaDB
    print("[*] Storing chapter to ChromaDB...")
    store_chapter(chapter_id, final_text)
    print(f"[✅] Chapter '{chapter_id}' stored in ChromaDB successfully.")
    # Optional: Test the RL search
    print("\n[🔍] Testing RL-based search for keyword: 'morning sea'")
    rl_results = search_chapter("morning sea")  # Or rl_search("morning sea")
    print("Top match:", rl_results["documents"][0][0])

