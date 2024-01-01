# Remoção de Acentuação

Este é um utilitário simples em Python que permite a remoção de acentos de texto em arquivos. Ele utiliza a biblioteca `unidecode` para realizar essa tarefa de forma eficiente.

### Estrutura de Pastas

- A pasta **[Código Fonte de Remoção de Acentuação](./remove-accentuation-source-code/)** contém as entradas e saídas utilizadas no projeto criado, bem como o próprio código fonte.
- Na pasta **[Script](./remove-accentuation-source-code/script/)**, você encontrará o código fonte do projeto.

## Como Funciona

O utilitário lê um arquivo de texto de entrada e remove todos os acentos, convertendo caracteres acentuados para suas equivalentes sem acentos. O resultado é escrito em um novo arquivo de saída.

## Como Usar

Siga estes passos para remover acentos de um arquivo de texto:

1. Clone este repositório ou baixe o código fonte para o seu ambiente local.

2. Certifique-se de ter a biblioteca `unidecode` instalada. Se não tiver, instale-a com o seguinte comando:

pip install unidecode

3. Coloque o arquivo de texto que deseja processar na pasta input.

4. Execute o utilitário fornecido (`remove_accentuation.py`). Certifique-se de definir o nome do arquivo de entrada (`nome_arquivo_entrada`) e o nome do arquivo de saída (`nome_arquivo_saida`) no código, se necessário.

5. Após a execução, o arquivo de saída conterá texto sem acentos na pasta `output`.

### Por que Remover Acentos?

A remoção de acentos pode ser útil em diversas situações, tais como:

- Preparação de texto para processamento de linguagem natural.
- Padronização de texto em sistemas que não suportam caracteres acentuados.
- Simplificação de consultas em bancos de dados.

Este utilitário é uma solução simples para remover acentos de forma eficaz e pode ser facilmente incorporado em outros projetos.

***

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