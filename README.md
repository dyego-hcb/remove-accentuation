# Accentuation Removal

This is a simple Python utility that allows you to remove accents from text in files. It uses the `unidecode` library to efficiently perform this task.

### Folder Structure

- The **[Remove Accentuation Source Code](./remove-accentuation-source-code/)** folder contains the inputs and outputs used in the created project, as well as the source code itself.
- In the **[Script](./remove-accentuation-source-code/script/)** folder, you will find the source code for the project.

## How It Works

The utility reads an input text file and removes all accents, converting accented characters to their unaccented equivalents. The result is written to a new output file.

## How to Use

Follow these steps to remove accents from a text file:

1. Clone this repository or download the source code to your local environment.

2. Make sure you have the `unidecode` library installed. If not, install it with the following command:

pip install unidecode


3. Place the text file you want to process in the `input` folder.

4. Run the provided utility (`remove_accentuation.py`). Make sure to set the input file name (`nome_arquivo_entrada`) and the output file name (`nome_arquivo_saida`) in the code, if necessary.

5. After execution, the output file will contain text without accents in the `output` folder.

## Why Remove Accents?

Accent removal can be useful in various situations, such as:

- Preparing text for natural language processing.
- Standardizing text in systems that do not support accented characters.
- Simplifying search queries in databases.

This utility is a simple solution for effectively removing accents and can be easily incorporated into other projects.