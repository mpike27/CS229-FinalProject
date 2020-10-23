from VideoScraper import VideoScraper
import numpy as np

FULL_VIDEO_PATH = 'Data/Training/Full_Vids'
FRAMES_PATH = 'Data/Traininng/Frames/'
# sample_urls = [('WolvesManCity122719', 'https://www.youtube.com/watch?v=9CeYDWG5wlM')]
sample_urls = [('WolvesManCity122719H', 'https://www.youtube.com/watch?v=OtdjPcLMP5Y')]


def main():
    vs = VideoScraper()
    for video_name, url in sample_urls:
        # if video already downloaded, print already downloaded and skip
        #vs.download_from_url(url, video_name, FULL_VIDEO_PATH)


        frame_interval = 30  #s - 1 frame every 30 seconds
        vs.saveFrames(video_name,
                      FULL_VIDEO_PATH + '/' + video_name + '.mp4',
                      FRAMES_PATH,
                      frame_interval)
        input("Continue? Press enter to continue:")
        vs.makeDFMilestone()


    #data = vs.parseVideos(FULL_VIDEO_PATH)
    #print(data)
    print("SIIIIII")
    ''' At this point we should have the 30s segments saved as csv unlabeled'''


if __name__ == '__main__':
    main()
