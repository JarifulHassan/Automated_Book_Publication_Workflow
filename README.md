### `README.md`

```markdown
#  Automated Book Publisher (AI + Human-in-the-Loop)

This project implements an **Automated Book Publication Workflow** using web scraping, AI-powered content rewriting with **Google Gemini**, human-in-the-loop review via a GUI editor, and semantic storage using **ChromaDB** with retrieval support.

> Built in **Anaconda Base Environment**  
> Python version: **3.12.7**

---

##  Features

- Scrape and screenshot chapters from public book sources  
- Rewrite chapters using **Gemini LLM** (Google Generative AI)  
- Review & edit rewritten content manually via a GUI (Tkinter)  
- Store final content in **ChromaDB** for intelligent semantic search  
- Enable **human-in-the-loop** editing before publishing  
-  Retrieve chapters based on semantic meaning (RL-style search)

---

##  Project Structure

```

automated\_book\_publisher/
├── main.py                     #  Main pipeline to run entire flow
├── ai\_writer.py                # Rewrite chapter using Gemini
├── requirements.txt            #  Required dependencies
├── README.md                   #  Documentation
│
├── utils/
│   └── scraping.py             #  Scrape chapter + screenshot using Playwright
│
├── gui/
│   └── reviewer.py             #  Tkinter-based editor
│
├── db/
│   └── knowledge.py            #  ChromaDB operations
│
├── data/                       #  Raw HTML files
├── output/                     #  Final reviewed chapters
└── screenshots/                #  Screenshots of pages

````

---

## Setup Instructions

### 1. Clone the Repository


### 2. Create & Activate Environment (Optional)

If you're using Anaconda (recommended):

```bash
conda create -n autobook python=3.12.7
conda activate autobook
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

##  Gemini API Setup

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Paste it in `main.py`:

```python
API_KEY = "YOUR_API_KEY"
```

---

##  How to Run

Run the full pipeline using:

```bash
python main.py
```

### What Happens:

* Scrapes HTML and saves a screenshot
* Uses Gemini to rewrite the chapter
* Opens a GUI for you to edit it
* Saves the final reviewed version to `output/`
* Stores the chapter in ChromaDB with vector indexing

---

###  Search for Stored Chapters

Use semantic search like:

```python
from db.knowledge import search_chapter
results = search_chapter("A description of a stormy ocean")
print(results)
```

---
### RL Search (Placeholder)

The current implementation uses ChromaDB for chapter retrieval based on semantic similarity.

To align with the assignment requirement, a placeholder `rl_search(query)` is provided in `db/knowledge.py`. It mimics RL behavior by performing standard retrieval for now. Future enhancements may integrate real Reinforcement Learning for search optimization.


###  Output Example

```
output/
├── chapter1_final.txt        # Final reviewed content
data/
├── chapter1.html             # Raw scraped HTML
screenshots/
├── chapter1_screenshot.png   # Screenshot of original page
```

---

###  Deadline & Notes

* **Submission Deadline:** 22 June 2025
* **Note:** This project is for evaluation only. No commercial use intended. Developer retains full ownership.

---

###  Requirements (via `requirements.txt`)

Key libraries:

* `playwright`
* `google-generativeai`
* `beautifulsoup4`
* `chromadb`
* `sentence-transformers`
* `tk` (GUI, built-in with Anaconda)

Install all via:

```bash
pip install -r requirements.txt
```

---

### Author

**Jariful Hassan**
 [jariful076@gmail.com](mailto:jariful076@gmail.com)
 [GitHub](https://github.com/JarifulHassan)
 [LinkedIn](https://www.linkedin.com/in/jariful-hassan-69142424a/)

---
