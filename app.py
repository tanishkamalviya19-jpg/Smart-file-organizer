import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def organize_folder(path):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Others": []
    }
    results = []
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            moved = False
            for folder, extensions in categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    dest = os.path.join(path, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(filepath, dest)
                    results.append(f"✅  {filename}  →  {folder}")
                    moved = True
                    break
            if not moved:
                dest = os.path.join(path, "Others")
                os.makedirs(dest, exist_ok=True)
                shutil.move(filepath, dest)
                results.append(f"📁  {filename}  →  Others")
    return results

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        path_label.config(text=folder, fg="#00d4aa")

def run_organizer():
    path = folder_path.get()
    if not path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return
    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)
    results = organize_folder(path)
    for line in results:
        output_box.insert(tk.END, line + "\n")
    output_box.insert(tk.END, f"\n🎉 Done! {len(results)} files organized.")
# Window setup
root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("500x600")
root.configure(bg="#0f1117")
root.resizable(True, True)

folder_path = tk.StringVar()

# Title
tk.Label(root, text="Smart File Organizer",
         font=("Courier", 20, "bold"),
         bg="#0f1117", fg="#00d4aa").pack(pady=(30, 5))

tk.Label(root, text="Organize your files instantly",
         font=("Courier", 10),
         bg="#0f1117", fg="#aaaaaa").pack(pady=(0, 20))

# Path display
path_label = tk.Label(root, text="No folder selected",
                      font=("Courier", 9),
                      bg="#0f1117", fg="#444444",
                      wraplength=500)
path_label.pack(pady=(0, 10))

# Buttons
btn_frame = tk.Frame(root, bg="#0f1117")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="📂  Select Folder",
          command=select_folder,
          font=("Courier", 11, "bold"),
          bg="#1e2130", fg="#ffffff",
          activebackground="#2a2f45",
          relief="flat", padx=20, pady=10,
          cursor="hand2").pack(side="left", padx=10)

tk.Button(btn_frame, text="⚡  Organize",
          command=run_organizer,
          font=("Courier", 11, "bold"),
          bg="#00d4aa", fg="#0f1117",
          activebackground="#00b894",
          relief="flat", padx=20, pady=10,
          cursor="hand2").pack(side="left", padx=10)

# Output box
output_box = tk.Text(root,
                     height=14, width=68,
                     font=("Courier", 9),
                     bg="#1e2130", fg="#ffffff",
                     relief="flat",
                     padx=10, pady=10,
                     state="disabled",
                     insertbackground="white")
output_box.pack(pady=20, padx=20)

root.mainloop()