import tkinter as tk
from tkinter import filedialog, colorchooser
from renamer import shave_names

class NameShaverApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NameShaver")

        # Default settings
        self.font_size = tk.IntVar(value=12)
        self.font_color = tk.StringVar(value="#FFFFFF")
        self.bg_color = tk.StringVar(value="#2c2c2c")
        self.window_width = tk.IntVar(value=750)
        self.window_height = tk.IntVar(value=250)

        self.folder_path = tk.StringVar()
        self.words_to_remove = tk.StringVar()

        self._build_gui()
        self._apply_styles()

    def _build_gui(self):
        # Settings frame
        settings_frame = tk.Frame(self.root)
        settings_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        # Main controls
        tk.Label(self.root, text="Select Folder:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.folder_path, width=40).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_folder).grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self.root, text="Words to remove (comma-separated):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.words_to_remove, width=40).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Shave Names", command=self.shave_names).grid(row=3, column=1, pady=10)
        tk.Button(self.root, text="Clear", command=self.clear_fields).grid(row=4, column=2, pady=10)

        # Results display
        self.result_text = tk.Text(self.root, height=5, width=60, state='disabled')
        self.result_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def _apply_styles(self):
        font = ("Arial", self.font_size.get())
        fg = self.font_color.get()
        bg = self.bg_color.get()
        self.root.configure(bg=bg)
        for widget in self.root.winfo_children():
            self._set_widget_style(widget, font, fg, bg)
        self.root.geometry(f"{self.window_width.get()}x{self.window_height.get()}")

    def _set_widget_style(self, widget, font, fg, bg):
        # Recursively apply styles to all widgets
        if isinstance(widget, (tk.Label, tk.Button, tk.Entry, tk.Text, tk.Spinbox)):
            try:
                widget.configure(font=font, fg=fg, bg=bg)
            except tk.TclError:
                pass
        if isinstance(widget, tk.Text):
            widget.configure(insertbackground=fg)
        if isinstance(widget, tk.Frame):
            widget.configure(bg=bg)
            for child in widget.winfo_children():
                self._set_widget_style(child, font, fg, bg)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def shave_names(self):
        folder = self.folder_path.get()
        words = self.words_to_remove.get().split(",")
        words = [word.strip() for word in words if word.strip()]
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        if not folder or not words:
            self.result_text.insert(tk.END, "Please select a folder and enter words to remove.\n")
            self.result_text.config(state='disabled')
            return
        try:
            skipped = shave_names(folder, words)
            msg = "Renaming completed!\n"
            if skipped:
                msg += f"Skipped files: {', '.join(skipped)}"
            else:
                msg += "All files processed successfully."
            self.result_text.insert(tk.END, msg)
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")
        self.result_text.config(state='disabled')

    def clear_fields(self):
        self.folder_path.set("")
        self.words_to_remove.set("")
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

    def run(self):
        self.root.mainloop()