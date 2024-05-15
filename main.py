import schedule
import YoutubeDownloader
from tools import YoutubeScraper
from tools import ScrapterController

def setup():
    GET_INFO = 1
    QUIT = 2
    
    while(True):
        user_select = int(input("1 : Type chennel and name \n2 : Stop type chennel and start scraping \n"))
        if user_select == GET_INFO:
            YS = YoutubeScraper.Scraper()
            SC.add_scrapter(YS)
        elif user_select == QUIT:
            break

def scraping():
    scrapter_list = SC.get_scrapter_list()
    for ys in scrapter_list:
        if ys.is_new_video():
            new_url_arr = ys.scrapping()
            for url in new_url_arr:
                #YD.download_video(url,ys.get_name())
                YD.download_audio(url,ys.get_name())
        else:
            print(ys.get_name()+" is No new Videos!")

if __name__ == "__main__":
    YD = YoutubeDownloader.YotubeDownLoader()
    SC = ScrapterController.ScrapterController()
    setup()

    schedule.every(1).days.do(scraping)
    while True:
        schedule.run_pending()