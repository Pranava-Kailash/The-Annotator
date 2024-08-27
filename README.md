# The Annotator 

## Overview

This project is designed to perform named entity recognition (NER) annotation, process data files, and manage annotations for various entity types such as malware, indicators, organizations, threat groups, vulnerabilities, systems, dates, and locations. The system is composed of several Python scripts that interact to read, annotate, and save the processed data. Designed on KISS (Keep It Stupid Simple) principle.

## Files

### 1. `main.py`

This is the entry point of the project. It coordinates the entire process by invoking different modules for reading files, processing annotations, and writing results.

### 2. `annotator.py`

This script contains the logic for annotating text data with specified named entities. It utilizes the tags defined in `settings.json` to identify and label entities in the text.

### 3. `checkpoint.py`

This file manages checkpointing, allowing the project to save progress and resume from a previous state if needed. This is useful for large datasets where processing can be time-consuming.

### 4. `read_files.py`

This script handles the reading of input data files. It reads and prepares the data for annotation, ensuring that the data is in the correct format before processing.

### 5. `writer.py`

This script handles the writing of annotated data to the output file. It ensures that the data is correctly formatted and saved according to the project's needs.

### 6. `settings.json`

This configuration file contains settings and parameters used across the project. It includes:

- **file_to_annotate**: Specifies the file that contains the data to be annotated.
- **ner_tags**: Defines the list of entity tags used for annotation.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```
2. **Adjust Setting json as you wish:**

   ```bash
   file_to_annotate: file_name.csv
   ner_tags: ["enter","list","of","entities"]
   ```

3. **Run the command from the root directory**

   ```bash
   python main.py
   ```

## How it works

f you need to alter or create new annotations for your NER model, this script can help manage those tasks efficiently. Simply enter your file name in the settings and specify the tags you wish to use. Once you run the command python main.py, you'll see a screen similar to this:

![Image of the annotator](https://github.com/user-attachments/assets/422704b9-a8ce-401a-ac5e-a983be2d5722)

The interface includes an "Update Tag" button to modify the NER tags, a "Next Sentence" button to proceed to the next row of tokens and NER tags, and an "Exit" button that saves the current sentence and remembers where you left off.
**Note: This script assumes that there are only two columns in the dataset, namely "tokens" and "ner_tags".**

   
