import schedule
import YoutubeDownloader
import YoutubeScraper

def scraping():
    if YS.is_new_video():
        new_url = YS.scrapping()
        print(new_url)
        # YD.downloading_video(new_url)
        YD.downloading_audio(new_url)
    else:
        print("No new Vedio")

if __name__ == "__main__":
    YS = YoutubeScraper.Scraper()
    YD = YoutubeDownloader.YotubeDownLoader()

    scraping()

    schedule.every(20).seconds.do(scraping)
    while True:
        schedule.run_pending()
