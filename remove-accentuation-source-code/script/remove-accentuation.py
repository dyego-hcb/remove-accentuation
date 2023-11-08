from unidecode import unidecode

def remover_acentuacoes(texto):
    return unidecode(texto)

nome_arquivo_entrada = './input/in.txt'

nome_arquivo_saida = './output/out.txt'

with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
    texto = arquivo_entrada.read()

texto_sem_acentuacoes = remover_acentuacoes(texto)

with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto_sem_acentuacoes)
