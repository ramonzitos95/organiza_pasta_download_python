import os
import shutil
from servicos.fileservice import listar_arquivos_e_verificar_extensao, limpar_arquivos_da_pasta, obter_extensoes_da_pasta


caminho_downloads = r'C:\Users\RAMON\Downloads'
extensoes_encontradas = obter_extensoes_da_pasta(caminho_downloads)
print(f'Extensões: {extensoes_encontradas}')
for extensao in extensoes_encontradas:
    print(f'Processando extensão {extensao}')
    listar_arquivos_e_verificar_extensao(caminho_downloads, extensao)
        
limpar_arquivos_da_pasta(caminho_downloads)

