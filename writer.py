import csv
import json

class Writer:
    def __init__(self, tokens, ner_tags, file_exists):
        self.tokens = tokens
        self.ner_tags = ner_tags
        self.file_exists = file_exists

    def write_csv(tokens, ner_tags, file_exists):
        with open('final_annotated_dataset.csv', 'a', newline='') as csvfile:
            fieldnames = ['tokens', 'ner_tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'tokens': json.dumps(tokens), 'ner_tags': json.dumps(ner_tags)})
    