import os
import scrapetube
class Scraper():
    def __init__(self):
        self.get_chennel()
        self.old_videos_id = []
        self.new_videos_id = []

    def create_youtube_link(self,id_arr):
        youtube_link_arr = []
        for id in id_arr:
            youtube_link_arr.append('https://www.youtube.com/watch?v='+id)
        return youtube_link_arr

    def scrapping(self):
        if self.is_new_video():
            new_video_ID = self.get_new_videoID()
            self.old_videos_id = self.new_videos_id
            new_youtube_link = self.create_youtube_link(new_video_ID)
            return new_youtube_link
        else:
            return []

    def get_chennel(self):
        self.chennel = input("Put the channel need to scrap : ")
        # 나중에 배열이나, 딕셔너리로 받기
    def scrap_videos(self):
        video_id_arr = []
        videos = scrapetube.get_channel(self.chennel, limit=5, sort_by="newest")
        for video in videos:
            video_id_arr.append(video['videoId'])
        return video_id_arr
    def is_new_video(self):
        video_id_arr = self.scrap_videos()
        if not self.old_videos_id:
            #초기값이면 현재거 넣어주고 변한거 없다고 리턴
            self.old_videos_id = video_id_arr
            return False

        if self.old_videos_id != video_id_arr:
            self.new_videos_id = video_id_arr
            return True
        else:
            return False
    def get_new_videoID(self):
        old = set(self.old_videos_id)
        new = set(self.new_videos_id)
        return set(old) ^ set(new)