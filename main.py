from annotator import mainUI as Annotator
import read_files
import tkinter as tk
import json

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("The Annotator")
    settings = json.load(open('settings.json'))
    file_path = settings['file_to_annotate']
    df = read_files.Reader(file_path).read_csv()
    annotator = Annotator(root,df)
    root.mainloop()