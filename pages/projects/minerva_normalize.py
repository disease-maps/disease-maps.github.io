#!/usr/bin/env python3

import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def normalize_value(val):
    try:
        v = float(val)
        return max(-1.0, min(1.0, v / 3))
    except:
        return val  # Leave unchanged if not a number

def normalize_file():
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select input file",
        filetypes=[("CSV/TSV files", "*.csv *.tsv *.txt")]
    )

    if not file_path:
        return

    # Determine delimiter based on file extension
    if file_path.endswith(".tsv") or file_path.endswith(".txt"):
        delimiter = "\t"
    elif file_path.endswith(".csv"):
        delimiter = ","
    else:
        messagebox.showerror("Error", "Unsupported file type.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=delimiter)
            rows = list(reader)

        if not rows or len(rows) < 2:
            messagebox.showerror("Error", "File is empty or malformed.")
            return

        header = rows[0]
        data = rows[1:]

        # Rename first column
        header[0] = "identifier_hgnc_symbol"

        # Find the 'value' column
        if "value" not in header:
            messagebox.showerror("Error", "Missing 'value' column.")
            return
        value_index = header.index("value")

        # Normalize values in the 'value' column
        for row in data:
            if len(row) > value_index:
                row[value_index] = str(normalize_value(row[value_index]))

        # Write output file
        out_path = os.path.splitext(file_path)[0] + "_normalized.txt"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(header)
            writer.writerows(data)

        messagebox.showinfo("Done", f"Saved:\n{out_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Normalize Expression Values")
    root.geometry("300x120")
    tk.Button(root, text="Select File to Normalize", command=normalize_file, height=2, width=30).pack(expand=True)
    root.mainloop()
