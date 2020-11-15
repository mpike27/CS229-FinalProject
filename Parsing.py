import VideoScraper as vs
import numpy as np
import os

train_path = 'Data/Training/CSV/'
test_path = 'Data/Testing/CSV/'
full_broad_urls = [("WolvesArsenal042419", "https://www.youtube.com/watch?v=DWYKhbawzQ8"), ("BarcaMallorca041720", "https://www.youtube.com/watch?v=rxslQS6KTS4")]
highlight_urls = [('EvertonManUtd110920H', 'https://www.youtube.com/watch?v=dM1j3XAhwIE'),
                  ('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y'),
                  ('BarBetis110920H', 'https://www.youtube.com/watch?v=KugeDpzfOBY'),
                  ('ChelSeffUtd110820H', 'https://www.youtube.com/watch?v=uyp75pH_mzU'),
                  ('ManUtdTot100520H', 'https://www.youtube.com/watch?v=dnjNhcMsT1c'),
                  ('SouTot092220H', 'https://www.youtube.com/watch?v=Wt-sXiQMGAc')]
clip_len = 10
train_query = "EPL Highlights"
fps = 2
dim = (256, 256)

def main():
    vs.downloadVideos(train_query, train_path, dim, clip_len=clip_len, fps=fps)
    for video_name, url in full_broad_urls:
        if vs.download_from_url(url, video_name, test_path):
            vs.parseVideo(test_path + video_name + '.mp4', dim, clip_len=clip_len, fps=fps)
            os.remove(test_path + video_name + '.mp4')


if __name__ == '__main__':
    main()
