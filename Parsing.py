import VideoScraper as vs
import numpy as np
import os

train_path = 'Data/Training/CSV/'
test_path = 'Data/Testing/CSV/'
full_broad_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM'), ("WolvesArsenal042419", "https://www.youtube.com/watch?v=DWYKhbawzQ8")]
highlight_urls = [('EvertonManUtd110920H', 'https://www.youtube.com/watch?v=dM1j3XAhwIE'),
                  ('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y'),
                  ('BarBetis110920H', 'https://www.youtube.com/watch?v=KugeDpzfOBY'),
                  ('ChelSeffUtd110820H', 'https://www.youtube.com/watch?v=uyp75pH_mzU'),
                  ('ManUtdTot100520H', 'https://www.youtube.com/watch?v=dnjNhcMsT1c'),
                  ('SouTot092220H', 'https://www.youtube.com/watch?v=Wt-sXiQMGAc')]
clip_len = 30
query = "Full Soccer Match"

def main():
    for video_name, url in highlight_urls:
        vs.download_from_url(url, video_name, train_path)
        vs.parseVideo(train_path + video_name + '.mp4', clip_len)
        os.remove(train_path + video_name + '.mp4')
    # vs.downloadVideos(query, train_path)


if __name__ == '__main__':
    main()
