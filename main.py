#   ╔╗  ╔╗         ╔╗     ╔╗          ╔╗  ╔╗    ╔╗            ╔═══╗              ╔╗            ╔╗       
#   ║╚╗╔╝║        ╔╝╚╗    ║║          ║╚╗╔╝║    ║║            ╚╗╔╗║              ║║            ║║       
#   ╚╗╚╝╔╝╔══╗╔╗╔╗╚╗╔╝╔╗╔╗║╚═╗╔══╗    ╚╗║║╔╝╔╗╔═╝║╔══╗╔══╗     ║║║║╔══╗╔╗╔╗╔╗╔═╗ ║║ ╔══╗╔══╗ ╔═╝║╔══╗╔═╗
#    ╚╗╔╝ ║╔╗║║║║║ ║║ ║║║║║╔╗║║╔╗║     ║╚╝║ ╠╣║╔╗║║╔╗║║╔╗║     ║║║║║╔╗║║╚╝╚╝║║╔╗╗║║ ║╔╗║╚ ╗║ ║╔╗║║╔╗║║╔╝
#     ║║  ║╚╝║║╚╝║ ║╚╗║╚╝║║╚╝║║║═╣     ╚╗╔╝ ║║║╚╝║║║═╣║╚╝║    ╔╝╚╝║║╚╝║╚╗╔╗╔╝║║║║║╚╗║╚╝║║╚╝╚╗║╚╝║║║═╣║║ 
#     ╚╝  ╚══╝╚══╝ ╚═╝╚══╝╚══╝╚══╝      ╚╝  ╚╝╚══╝╚══╝╚══╝    ╚═══╝╚══╝ ╚╝╚╝ ╚╝╚╝╚═╝╚══╝╚═══╝╚══╝╚══╝╚╝ 
########################################################################################################


import os
import pyperclip
from pytube import YouTube
from urllib.request import urlretrieve
import pyautogui
from pynput import keyboard
import re


print("Pressione F2 para adicionar URL do vídeo para download.")
print("Pressione F3 para iniciar o download dos vídeos adicionados.")


# ESTA FUNÇÃO RECEBE UM TEXTO
# COMO ENTRADA E RETORNA O MESMO TEXTO
# SEM CARACTERES ESPECIAIS
# E COM TODAS AS LETRAS EM MAIÚSCULO.
def text_no_especial_char(text):
    regex = re.compile('[^a-zA-Z0-9\s]+')
    text = regex.sub('', text)
    text = re.sub('\s{2,}', ' ', text)
    text = text.upper()
    return text


# FUNÇÃO PARA BAIXAR VÍDEO DO YOUTUBE :: START
def video_youtube_download(video_url):

    # Cria uma instância da classe YouTube com a URL do vídeo
    yt = YouTube(video_url)

    # Obtém o título do vídeo
    title = text_no_especial_char(yt.title)

    # Obtém a melhor qualidade de vídeo disponível
    stream = yt.streams.get_highest_resolution()

    # Define o nome do arquivo de saída como o título do vídeo + ".mp4"
    print(title)
    output_filename = f"{title}.mp4"

    # Cria o diretório "downloads" caso ele não exista
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # Faz o download do vídeo e obtém o caminho completo do arquivo baixado
    file_path = os.path.join("downloads", output_filename)
    urlretrieve(stream.url, file_path)

    # Obtém o tamanho do arquivo baixado em bytes
    file_size = os.path.getsize(file_path)

    try:
        # Define o progresso do download como uma barra de progresso usando a biblioteca tqdm
        print("Baixando vídeo...")
        with open(file_path, "rb") as file_handle:
            downloaded_size = 0
            block_size = 1024
            while True:
                buffer = file_handle.read(block_size)
                if not buffer:
                    break
                downloaded_size += len(buffer)
                progress = downloaded_size / file_size * 100
                print(f"Progresso: {progress:.2f}%", end="\r")

    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

    else:
        print("Vídeo baixado com sucesso!")
# FUNÇÃO PARA BAIXAR VÍDEO DO YOUTUBE :: END


# NÚMERO DE VEZES QUE A TECLA FOI PRESSIONADA
KEY_PRESS_COUNT = 0

# LISTA DE VÍDEOS A SEREM BAIXADOS
videos_to_download = []


# FUNÇÃO CHAMADA QUANDO UMA TECLA É PRESSIONADA :: START
def on_key_press(key):

    global KEY_PRESS_COUNT

    if key == keyboard.Key.f2:
        KEY_PRESS_COUNT += 1
        if KEY_PRESS_COUNT == 3:
            # COPIA A URL DO NAVEGADOR
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.hotkey('esc')

            # PEGA A URL DO NAVEGADOR
            video_url = pyperclip.paste()

            print(video_url)
            print("VÍDEO ADICIONADO PARA DOWNLOAD...")
            videos_to_download.append(video_url)
            KEY_PRESS_COUNT = 0

    if key == keyboard.Key.f3:
        KEY_PRESS_COUNT += 1
        if KEY_PRESS_COUNT == 3:
            KEY_PRESS_COUNT = 0

            # INICIAR DOWNLOAD DOS VÍDEOS ADICIONADOS
            for i, video in enumerate(videos_to_download):
                print(f"INICIANDO DOWNLOAD DO VÍDEO {i+1}/{len(videos_to_download)}...")
                video_youtube_download(video)

            # LIMPAR LISTA DE VÍDEOS A SEREM BAIXADOS
            videos_to_download.clear()
# FUNÇÃO CHAMADA QUANDO UMA TECLA É PRESSIONADA :: END


# CRIA UM OUVINTE DE TECLADO :: START
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
# CRIA UM OUVINTE DE TECLADO :: END
