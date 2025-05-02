
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def normalize_stl_file(filepath, new_filename=None):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            lines = f.readlines()

        if not lines:
            return False, "File is empty."

        # Normalize header
        first_line = lines[0].strip()
        if first_line.lower() == "solid":
            lines[0] = f"solid {os.path.splitext(os.path.basename(filepath))[0]}\n"

        # Normalize ending
        if not lines[-1].strip().startswith("endsolid"):
            lines.append(f"endsolid {os.path.splitext(os.path.basename(filepath))[0]}\n")

        output_path = new_filename or filepath.replace(".stl", "_normalized.stl")
        with open(output_path, 'w') as f:
            f.writelines(lines)

        return True, output_path
    except Exception as e:
        return False, str(e)

def select_and_normalize():
    filepath = filedialog.askopenfilename(filetypes=[("STL files", "*.stl")])
    if not filepath:
        return
    success, message = normalize_stl_file(filepath)
    if success:
        messagebox.showinfo("Success", f"Normalized STL saved to:\n{message}")
    else:
        messagebox.showerror("Error", f"Failed to normalize STL:\n{message}")

root = tk.Tk()
root.title("STL Normalizer")
root.geometry("300x150")

label = tk.Label(root, text="Select an STL file to normalize", pady=20)
label.pack()

button = tk.Button(root, text="Select File", command=select_and_normalize)
button.pack()

root.mainloop()
