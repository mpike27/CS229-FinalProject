from VideoScraper import VideoScraper
import numpy as np

FULL_VIDEO_PATH = 'Data/Training/Full_Vids'
sample_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM'), ("WolvesArsenal042419", "https://www.youtube.com/watch?v=DWYKhbawzQ8")]

def main():
    vs = VideoScraper()
    # for video_name, url in sample_urls:
    #     vs.download_from_url(url, video_name, FULL_VIDEO_PATH)
    data = vs.parseVideos(FULL_VIDEO_PATH)
    print(data)
    ''' At this point we should have the 30s segments saved as csv unlabeled'''


if __name__ == '__main__':
    main()
