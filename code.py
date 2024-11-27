import os, time, sys, yt_dlp

def BANNER():
    return("YOUTUBE DOWNLOADER")

def download_audio(url, output_path="output"):
    # Configurações do yt-dlp para áudio
    ydl_opts = {
        'format': 'bestaudio/best',  # Seleciona o melhor áudio disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Nome do arquivo de saída
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extrai apenas o áudio
            'preferredcodec': 'mp3',  # Converte para MP3
            'preferredquality': '192',  # Qualidade (opcional, 192 kbps)
        }],
        'ffmpeg_location': r'bin/',  # Substitua pelo caminho da pasta 'bin' com ffmpeg.exe
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url, output_path="output"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Seleciona o melhor vídeo e áudio
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Nome do arquivo de saída
        'merge_output_format': 'mp4',  # Formato final após mesclar áudio e vídeo
        'ffmpeg_location': r'bin/',  # Substitua pelo caminho da pasta 'bin' com ffmpeg.exe
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

class main:
    def __init__(self):
        print(BANNER())

        self.get_input()

    def get_input(self):
        while True:
            cmd = input(" Enter a valid URL > ")
            if not cmd:
                print("you do not insert a valid URL...")
                time.sleep(3)
                return
            
            else:
                download_audio(url = cmd)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("exiting...")