# bibliotecas:
import pathlib
import os
import pyautogui

# Trecho que descobre qual o arquivo mais recente:

CaminhoAbsoluto = pathlib.Path(__file__).parent.absolute() # Caminho do arquivo python que está sendo executado.

ArquivosPasta = os.listdir(CaminhoAbsoluto) # Cria uma lista com todos os arquivos da pasta atual.

ListaComDatas = [] # Cria uma lista que armazena duplas com a data e o nome dos arquivos.
for arquivo in ArquivosPasta:
    # laco que insere na lista a data e o nome do arquivo.
    data = os.path.getmtime("{}/{}".format(CaminhoAbsoluto, arquivo)) # obtem a data do arquivo.
    ListaComDatas.append((data, arquivo)) # adiciona a data e o nome do arquivo na lista.

ListaComDatas.sort(reverse=True) # ordena a lista em ordem decrescente
ultimo_arquivo = ListaComDatas[0] # obtem o primeiro elemento da lista
ultimo_arquivo = ultimo_arquivo[1] # obtem apenas o nome da dupla de dados obtidos

# Trecho que executa o arquivo mais recente:
pyautogui.PAUSE = 1 # define o intervalo de tempo entre cada comando pyautogui
pyautogui.hotkey("win", "r") # clica no botão windows + r, para abrir o executar do windows
pyautogui.write("{}/{}".format(CaminhoAbsoluto, ultimo_arquivo)) # digita o caminho do arquivo
pyautogui.press("enter") # pressiona o botão enter
