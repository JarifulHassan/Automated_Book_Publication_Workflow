# ai_writer.py

import google.generativeai as genai

def configure_gemini(api_key: str):
    """Configures the Gemini API with your key"""
    genai.configure(api_key=api_key)

def rewrite_chapter(content: str, tone: str = "simple and engaging") -> str:
    """
    Uses Gemini to rewrite a chapter with a specified tone.
    
    Args:
        content (str): Original text to be rewritten
        tone (str): Desired rewrite tone (default: simple and engaging)

    Returns:
        str: Rewritten chapter content
    """
    prompt = (
        f"Please rewrite the following chapter content in a {tone} style:\n\n"
        f"{content}\n\n"
        f"Keep the meaning intact, but make it more modern, readable, and engaging."
    )
    
    # ✅ Fixed model name here
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text.strip()
