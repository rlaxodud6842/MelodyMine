import schedule
import YoutubeDownloader
import YoutubeScraper
import ScrapterController

def menu():
    while(True):
        user_select = input("If you type 'Q', scraping is start")
        if user_select != "Q" or user_select != "q":
            YS = YoutubeScraper.Scraper()
            SC.add_scrapter(YS)
        else:
            return SC.get_scrapter_list()

def scraping():
    scrapter_list = SC.get_scrapter_list()
    for ys in scrapter_list:
        if ys.is_new_video():
            new_url = ys.scrapping()
            print(new_url)
            # YD.downloading_video(new_url)
            YD.downloading_audio(new_url)
        else:
            print("No new Vedio")


if __name__ == "__main__":
    YD = YoutubeDownloader.YotubeDownLoader()
    SC = ScrapterController.ScrapterController()

    schedule.every(20).seconds.do(scraping)
    while True:
        schedule.run_pending()
