# ACESSAMOS UM ARQUIVO TXT E  EFETUAMOS A LEITURA DAS
import os


with open("teste.txt", "r") as arquivo:
 content = arquivo.read()
print(content)


with open("C:/Users/aluno/aula13", "w") as diretorio:
    os.mkdir("novo_arquivo")