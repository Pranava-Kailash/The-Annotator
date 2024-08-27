import pandas as pd
import json

class Reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        df = pd.read_csv(self.file_path)
        df['tokens'] = df['tokens'].apply(json.loads)
        df['ner_tags'] = df['ner_tags'].apply(json.loads)
        return df
    
    def file_exists():
        try:
            with open('final_annotated_dataset.csv', 'r') as f:
                return True
        except FileNotFoundError:
            return False