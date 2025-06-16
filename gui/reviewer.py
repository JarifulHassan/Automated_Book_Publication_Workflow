# gui/reviewer.py

import tkinter as tk

def review_and_edit(text, output_path):
    print("[DEBUG] Launching tkinter window...")  # Add this

    def save_and_exit():
        reviewed_text = text_area.get("1.0", tk.END).strip()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(reviewed_text)
        root.destroy()

    root = tk.Tk()
    root.title("Review and Edit Chapter")
    root.geometry("900x600")

    text_area = tk.Text(root, wrap="word", font=("Courier", 12))
    text_area.insert("1.0", text)
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    save_button = tk.Button(root, text="Save & Close", command=save_and_exit)
    save_button.pack(pady=10)

    root.mainloop()
