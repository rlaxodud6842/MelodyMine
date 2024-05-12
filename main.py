import schedule
import YoutubeDownloader
import YoutubeScraper

def scraping():
    if YS.scrapping():
        new_url = YS.scrapping()
        # YD.downloading_video(new_url)
        YD.downloading_audio(new_url)
    else:
        print("No new Vedio")

if __name__ == "__main__":
    YS = YoutubeScraper.Scraper()
    YD = YoutubeDownloader.YotubeDownLoader()

    schedule.every(1).days.do(scraping)
    while True:
        schedule.run_pending()
