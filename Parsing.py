from VideoScraper import VideoScraper
import numpy as np

FULL_VIDEO_PATH = 'Data/Training/Full_Vids'
FRAMES_PATH = 'Data/Training/Frames/'
CLIPS_PATH = 'Data/Training/Clips'
# sample_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM')]
sample_urls = [('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y')]
# sample_urls = [('ManUtdTot100520H', 'https://www.youtube.com/watch?v=dnjNhcMsT1c')]


def main():
    vs = VideoScraper()
    for video_name, url in sample_urls:
        # if video already downloaded, print already downloaded and skip
        # vs.download_from_url(url, video_name, FULL_VIDEO_PATH)


        vs.saveFrames(video_name,
                      CLIPS_PATH + '/' + video_name,
                      FRAMES_PATH + '/' + video_name)
        # input("Continue? Press enter to continue:")
        # vs.makeDFMilestone()


    # data = vs.parseVideos(FULL_VIDEO_PATH)
    #print(data)
    print("SIIIIII")
    ''' At this point we should have the 30s segments saved as csv unlabeled'''


if __name__ == '__main__':
    main()
