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

    def download_video(self,URL):
        DESTINATION_PATH = self.set_path()
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': DESTINATION_PATH
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])
    def download_audio(self,URL):
        DESTINATION_PATH = self.set_path()
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
    def set_path(self):
        path = os.path.join(self.path, '%(title)s')
        path = os.path.join(path, '%(title)s.%(ext)s')
        return path
    def get_url(self):
        URL = input("Put the URL what you want : ")
        return URL
    def downloading_audio(self,url_arr):
        for URL in url_arr:
            self.download_audio(URL)
            time.sleep(10)
    def downloading_video(self,url_arr):
        for URL in url_arr:
            self.download_video(URL)
            time.sleep(10)