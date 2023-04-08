## **YOUTUBE VIDEO DOWNLOADER**
#
Este é um script em Python que permite baixar vídeos do YouTube em alta resolução. Ele usa biblioteca PyAutoGUI para copiar a URL do navegador, a biblioteca pynput para ouvir as teclas pressionadas pelo usuário e a biblioteca pytube para baixar o vídeo.

### **Como usar**
#
Pressione **(F2)** para adicionar a URL do vídeo que você deseja baixar. Você pode adicionar quantos vídeos quiser.
Pressione **(F3)** para iniciar o download dos vídeos adicionados. Os vídeos serão salvos em uma pasta chamada downloads.

### **Requisitos**
#
Antes de executar o programa, você deve instalar as seguintes bibliotecas Python:

* PYTHON 3.11.2
* PIP 23.0.1
* PYNPUT 1.7.6
* PYINSTALLER 5.9.0

Além disso, as seguintes bibliotecas também são necessárias e serão instaladas automaticamente pelo pip:

* PyTube
* PyAutoGUI
* unidecode

Você também deve ter o ffmpeg instalado em seu sistema.

### **Dependências**
#
* pytube
* pynput
* unidecode

Você pode instalar as dependências usando o seguinte comando no terminal:

~~~shell
pip install pytube pynput unidecode
~~~

### **Utilização**
#
Para utilizar o programa, execute o arquivo ***`youtube_downloader.py`***. O programa irá aguardar que você pressione as teclas de atalho **(F2)** e **(F3)** para adicionar URLs de vídeo para download e iniciar o download dos vídeos adicionados, respectivamente.

### **Funções**
#
O código do programa inclui duas funções principais:

* ***`text_no_especial_char(text)`***: Esta função recebe um texto como entrada e retorna o mesmo texto sem caracteres especiais e com todas as letras em maiúsculo.
* ***`video_youtube_download(video_url)`***: Esta função é responsável por baixar o vídeo do YouTube usando o link fornecido como entrada. Ele obtém o título do vídeo, a melhor qualidade de vídeo disponível e define o nome do arquivo de saída como o título do vídeo + ".mp4". O vídeo é salvo na pasta "downloads" e o progresso do download é exibido em tempo real.


### **Licença**
#
Este programa é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

## ***RODAR/TESTAR O CÓDIGO***
#

### COM TERMINAL
~~~shell
python main.py
~~~
### SEM TERMINAL
~~~shell
pythonw main.py
~~~

## **COMPILAÇÃO**

~~~shell
pip install pyinstaller==5.9.0
~~~
~~~shell
pip show pyinstaller
~~~

### PARA EXECUTÁVEL COM TERMINAL
~~~shell
pyinstaller --onefile --name YoutubeVideoDownloader main.py
~~~

### PARA EXECUTÁVEL SEM TERMINAL COM ARQUIVOS EXTRAS
~~~shell
pyinstaller --noconsole --name YoutubeVideoDownloader main.py
~~~

### PARA EXECUTÁVEL SEM TERMINAL SEM ARQUIVOS EXTRAS
~~~shell
pyinstaller --onefile --noconsole --add-data "D:\ProgramFiles\Python\Python311\Lib\site-packages\pyperclip\pyperclip.dll;." --name YoutubeVideoDownloader main.py
~~~
~~~shell
pyinstaller --onefile --noconsole --name YoutubeVideoDownloader main.py
~~~
