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

### 7. `annotated_new_dataset.csv`

This file is the output produced after running the annotation process. It contains the annotated data with the entity tags defined in `settings.json`.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```
