import os
import time
import yt_dlp

class YotubeDownLoader():
    def __init__(self):
        self.path = self.create_downloads_folder()
    def create_downloads_folder(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        downloads_path = os.path.join(script_directory, "downloads")
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)
        return downloads_path

    def download_video(self,URL,name):
        DESTINATION_PATH = self.set_path(name)
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': DESTINATION_PATH
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])
    def download_audio(self,URL,name):
        DESTINATION_PATH = self.set_path(name)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': DESTINATION_PATH
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])
    def set_path(self,name):
        path = os.path.join(self.path, name)
        path = os.path.join(path, '%(title)s.%(ext)s')
        return path