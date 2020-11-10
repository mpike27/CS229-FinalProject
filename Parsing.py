import VideoScraper as vs
import numpy as np

train_path = 'Data/Training/CSV/'
sample_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM'), ("WolvesArsenal042419", "https://www.youtube.com/watch?v=DWYKhbawzQ8")]
clip_len = 30
query = "Full Soccer Match"

def main():
    # for video_name, url in sample_urls:
    #     vs.download_from_url(url, video_name, train_path)
    # vs.parseVideos(train_path, clip_len)
    vs.downloadVideos(query, train_path)
    ''' At this point we should have the 30s segments saved as csv unlabeled'''


if __name__ == '__main__':
    main()
