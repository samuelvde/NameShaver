import tkinter as tk
from tkinter import filedialog, messagebox
from renamer import shave_names

class NameShaverApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NameShaver")
        self.folder_path = tk.StringVar()
        self.words_to_remove = tk.StringVar()

        self._build_gui()

    def _build_gui(self):
        tk.Label(self.root, text="Select Folder:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.folder_path, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_folder).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.root, text="Words to remove (space-separated):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.words_to_remove, width=40).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Shave Names", command=self.shave_names).grid(row=2, column=1, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def shave_names(self):
        folder = self.folder_path.get()
        words = self.words_to_remove.get().split()
        if not folder or not words:
            messagebox.showerror("Error", "Please select a folder and enter words to remove.")
            return
        try:
            # Space for custom logic: skip files if certain rules apply
            skipped = shave_names(folder, words)
            msg = "Renaming completed!"
            if skipped:
                msg += f"\nSkipped files: {', '.join(skipped)}"
            messagebox.showinfo("Success", msg)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()