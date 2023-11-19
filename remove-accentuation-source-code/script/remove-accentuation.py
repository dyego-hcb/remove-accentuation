from unidecode import unidecode

def remove_accentuation(texto):
    return unidecode(texto)

def remove_accentuation_in_file(path_input, path_ouput):
    try:
        with open(path_input, 'r', encoding='utf-8') as input_file:
            texto = arquivo_entrada.read()

        texto_sem_acentuacoes = remove_accentuation(texto)

        with open(path_ouput, 'w', encoding='utf-8') as arquivo_saida:
            output_file.write(texto_sem_acentuacoes)

        print("Processamento concluído com sucesso.")

    except FileNotFoundError:
        print(f"Arquivo {path_input} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

path_input = './input/in.txt'
path_ouput = './output/out.txt'

remove_accentuation_in_file(path_input, path_ouput)
