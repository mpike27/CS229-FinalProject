from VideoScraper import VideoScraper
import numpy as np
import os
import sys
from os.path import isfile, join, isdir
import Config
USAGE = 'Usage: python Parsing.py --{train/test}'
TRAINING_VIDEO_DOWNLOAD_PATH = 'Data/Training/Clips/'
TRAINING_FRAMES_PATH = 'Data/Training/Frames/'
CLIPS_PATH = 'Data/Training/Clips/'
## Naming of videos is 'TeamTeamMMDDYY' + 'H'(if highlight)
# sample_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM')]
# sample_urls = [('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y')]
training_urls = [('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y'),
                 ('ManUtdTot100520H', 'https://www.youtube.com/watch?v=dnjNhcMsT1c'),
                 ('CheSheUtd110820H', 'https://www.youtube.com/watch?v=uyp75pH_mzU'),
                 ('EveLiv101720H', 'https://www.youtube.com/watch?v=8mEe6o9M144'),
                 ('ArsAvl110920H', 'https://www.youtube.com/watch?v=AMKLc_TMhdI'),
                 ('LivSheUtd102520H', 'https://www.youtube.com/watch?v=GNnGxyiwOIs'),
                 ('NewUtdEve110220H', 'https://www.youtube.com/watch?v=rGEl1_Qhlp4'),
                 ('BriManUtd092720H', 'https://www.youtube.com/watch?v=WuNnPvPqANU')]
testing_urls = [('WolvesManUtd031619F', 'https://www.youtube.com/watch?v=KMq-ZsSbnVA')]

def main(test):
    vs = VideoScraper()
    if not test:  # parse training set
        urls = training_urls
        video_download_path = 'Data/Training/Clips/'
        frames_path = 'Data/Training/Frames/'
        clips_path =  'Data/Training/Clips/'
    else:  # parse testing set
        urls = testing_urls
        video_download_path = 'Data/Testing/Clips/'
        frames_path = 'Data/Testing/Frames/'
        clips_path =  'Data/Testing/Clips/'
    for video_name, url in urls:
        # if video already downloaded, print already downloaded and skip
        if not isdir(video_download_path + video_name):
            full_mp4_path = vs.download_from_url(url, video_name, video_download_path + video_name)
            if len(full_mp4_path) != 0:  # if full_mp4_path is '', means that download failed
                print('Splitting ', video_name)
                os.system('python video-splitter/ffmpeg-split.py -f %s -s %d'
                            %(full_mp4_path, Config.PLAY_LEN))
                os.remove(full_mp4_path)
        else:
            print("Skipped download of ", video_name)

        # if video already parsed into frames, skip parsing
        if not isdir(frames_path + video_name):
            vs.saveFrames(video_name,
                          clips_path + video_name,
                          frames_path + video_name)
        else:
            print("Skipped making frames for ", video_name)

        # input("Continue? Press enter to continue:")
        # vs.makeDFMilestone()


    # data = vs.parseVideos(FULL_VIDEO_PATH)
    #print(data)
    print("SIIIIII")
    ''' At this point we should have the 30s segments saved as csv unlabeled'''


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(USAGE)
        exit()
    if sys.argv[1] != '--test' and sys.argv[1] != '--train':
        print(USAGE)
        exit()
    main(sys.argv[1] == '--test')
