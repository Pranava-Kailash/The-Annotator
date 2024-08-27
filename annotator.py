import csv
import json
import pandas as pd
import tkinter as tk
from checkpoint import Checkpoint
from writer import Writer
from read_files import Reader
from tkinter import ttk, messagebox

# def checkpoint_save(index):
#     with open('checkpoint.txt', 'w') as f:
#         f.write(str(index))

# def checkpoint_load():
#     try:
#         with open('checkpoint.txt', 'r') as f:
#             return int(f.read())
#     except FileNotFoundError:
#         return 0

# def correct_ner_tags_writer(tokens, ner_tags, file_exists):
#     with open('final_augmented_dataset.csv', 'a', newline='') as csvfile:
#         fieldnames = ['tokens', 'ner_tags']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()
#         writer.writerow({'tokens': json.dumps(tokens), 'ner_tags': json.dumps(ner_tags)})

class mainUI:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        self.current_index = Checkpoint.checkpoint_load()
        self.file_exists = Reader.file_exists()

        self.create_widgets()
        self.load_row(self.current_index)

        # Bind the Enter key and space bar to the update_tag method
        self.root.bind('<space>', self.update_tag_keypress)
        self.root.bind('<Return>', self.next_row_keypress)

    def create_widgets(self):
        self.root.state('zoomed')

        # Create Listboxes
        self.tokens_listbox = tk.Listbox(self.root, width=50, height=25, font=("Helvetica", 14))
        self.tokens_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tokens_listbox.bind("<MouseWheel>", self.sync_scroll)

        self.ner_tags_listbox = tk.Listbox(self.root, width=50, height=25, font=("Helvetica", 14))
        self.ner_tags_listbox.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.ner_tags_listbox.bind("<MouseWheel>", self.sync_scroll)

        control_frame = tk.Frame(self.root)
        control_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.index_label = tk.Label(control_frame, text="Index: 0", font=("Helvetica", 14))
        self.index_label.pack(pady=10)

        # Create Dropdown for NER tag selection
        settings = json.load(open('settings.json'))
        self.ner_tag_options =  settings['ner_tags'] 
        self.ner_tag_var = tk.StringVar(value=self.ner_tag_options[0])
        self.new_tag_dropdown = ttk.Combobox(control_frame, textvariable=self.ner_tag_var, values=self.ner_tag_options, font=("Helvetica", 10))
        self.new_tag_dropdown.pack(pady=5)

        self.update_button = tk.Button(control_frame, text="Update Tag", command=self.update_tag, font=("Helvetica", 10), width=20)
        self.update_button.pack(pady=10)

        self.next_button = tk.Button(control_frame, text="Next sentence", command=self.next_row, font=("Helvetica", 10), width=20)
        self.next_button.pack(pady=10)

        self.save_button = tk.Button(control_frame, text="Exit", command=self.exit, font=("Helvetica", 10), width=20)
        self.save_button.pack(pady=10)

        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

    def load_row(self, index):
        if index >= len(self.df):
            messagebox.showinfo("End", "No more rows to annotate.")
            return

        row = self.df.iloc[index]
        self.tokens = row['tokens']
        self.ner_tags = row['ner_tags']

        self.tokens_listbox.delete(0, tk.END)
        self.ner_tags_listbox.delete(0, tk.END)

        for token, ner_tag in zip(self.tokens, self.ner_tags):
            self.tokens_listbox.insert(tk.END, token)
            self.ner_tags_listbox.insert(tk.END, ner_tag)

        self.index_label.config(text=f"Index: {index}")

    def sync_scroll(self, event):
        self.tokens_listbox.yview_scroll(int(-1*(event.delta/120)), "units")
        self.ner_tags_listbox.yview_scroll(int(-1*(event.delta/120)), "units")
        return "break"

    def update_tag(self):
        selected_index = self.tokens_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No token selected.")
            return

        new_ner_tag = self.new_tag_dropdown.get()
        index = selected_index[0]
        self.ner_tags[index] = new_ner_tag
        self.ner_tags_listbox.delete(index)
        self.ner_tags_listbox.insert(index, new_ner_tag)


    def update_tag_keypress(self, event):
        self.update_tag()

    def next_row_keypress(self, event):
        self.next_row()

    def exit(self):
        Checkpoint.checkpoint_save(self.current_index)
        self.root.destroy()

    def next_row(self):
        if self.current_index >= len(self.df) + 1:
            messagebox.showinfo("End", "No more rows to annotate.")
            return

        Writer.write_csv(self.tokens, self.ner_tags, self.file_exists)
        self.file_exists = True  
        self.current_index += 1
        Checkpoint.checkpoint_save(self.current_index)
        self.load_row(self.current_index)

# if __name__ == "__main__":

#     df = pd.read_csv('annotated_new_dataset.csv')
#     df['tokens'] = df['tokens'].apply(json.loads)
#     df['ner_tags'] = df['ner_tags'].apply(json.loads)

#     root = tk.Tk()
#     root.title("The Annotator")
#     app = TheAnnotator(root, df)
#     root.mainloop()
