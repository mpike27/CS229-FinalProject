import urllib
from bs4 import BeautifulSoup
from pytube import YouTube
#import cv2
import os
import glob
import numpy as np
import sklearn
import pandas as pd
import cv2
import math
import Config

class VideoScraper:
    """
    The VideoScraper class is where we extract all of our videos from youtube.
    Once we are able to download the videos, we will parse them into a series of matrices so that we
    can perform learning techniques.
    """
    def __init__(self):
        """
        __init__
        --------
        The initialization creates an array to store the scraped videos
        --------
        Arguments:
        None
        --------
        Return: None
        """

    def downloadVideos(self, query, channel=""):
        """
        Method: downloadVideos
        ----------------------
        This method will scrape youtube according to the query, and will download all of the videos and store them in a list.
        If a channel is specified, the function will perform the search on the youtube channel's page.
        ----------------------
        Arguments:
        query - the string that we want to search on YouTube
        channel - Optional argument that indicates if you want to search on a given channel's page
        ----------------------
        Return: None
        """
        # def get_urls(text, limit=10):
        #     query = urllib.parse.quote(text)
        #     url = "https://www.youtube.com/results?search_query=" + query
        #     response = urllib.request.urlopen(url)
        #     html = response.read()
        #     soup = BeautifulSoup(html, 'html.parser')
        #     urls = []
        #     for i, vid in enumerate(soup.findAll(attrs={'class':'yt-uix-tile-link'})):
        #         if i < limit:
        #             urls.append('https://www.youtube.com' + vid['href'])
        #     print(f"Found {len(urls)} video links for {text}")
        # return urls
        pass

    def download_from_url(self, url, filename, path):
        """
        Method: download_from_url:
        --------------------------
        This method will download a youtube video from a given url and add it to the list of videos.
        --------------------------
        Arguments:
        url - the string form of a url
        --------------------------
        Return: None
        """
        try:
            YouTube(url).streams.first().download(filename=filename, output_path=path)
            print(f"Video {filename} downloaded successfully")
        except Exception as exc:
            print(f"Tried to download {filename}, but it did not work because {exc}...")

    def divideFullToClips(self, full_video_path):
        """
        Method: parseVideos
        ----------------------
        This method will break up each videos into a series of clips, and then format the data into a series of matrices.
        ----------------------
        Arguments:
        None
        ----------------------
        Return: numpy array containing the training data extracted from the youtube videos
        """
        videos = []
        try:
            cap = cv2.VideoCapture(full_video_path)
        except Exception as e:
            print(e)
        video_fps = cap.get(5)#frame rate

        clip = []
        while(cap.isOpened()):
            if (len(clip) == video_fps * Config.PLAY_LEN):
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate * Config.FPS) == 0):
                save_name = save_path + '/' + 'clip' + str(clip_num) + "/frame%d.tif" % count;count+=1
                cv2.imwrite(save_name, frame)
        cap.release()


        hasFrames = True
        frames = []
        while hasFrames:
            hasFrames, image = cap.read()
            frames.append(image)
        videos.append(frames)
        return videos


    def saveFrames(self, filename, video_path, save_path):

        clip_num = 1
        for video in os.listdir(video_path):
            print("Parsing ", video)
            try:
                os.mkdir(save_path + '/' + 'clip' + str(clip_num))
            except Exception as e:
                print(e)
            cap = cv2.VideoCapture(video_path + '/' + video)   # capturing the video from the given path
            frameRate = cap.get(5) #frame rate
            x=1
            count = 0
            while(cap.isOpened()):
                frameId = cap.get(1) #current frame number
                ret, frame = cap.read()
                if (ret != True):
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if (frameId % math.floor(frameRate * Config.FPS) == 0):
                    save_name = save_path + '/' + 'clip' + str(clip_num) + "/frame%d.tif" % count;count+=1
                    cv2.imwrite(save_name, frame)
            cap.release()
            clip_num += 1


    def makeDFMilestone(self):
        h_images = glob.glob("Data/Training/Frames/*.jpg")

        def makeFullMatchFrames(num):
            print("I will make %d images" %num)
            count = 0
            frame_interval = 1
            cap = cv2.VideoCapture('Data/Training/Full_Vids/WolvesManCity122719.mp4')   # capturing the video from the given path
            frameRate = cap.get(5) #frame rate
            x=1
            while(cap.isOpened()):
                frameId = cap.get(1) #current frame number
                ret, frame = cap.read()
                if (ret != True):
                    break
                if (frameId % math.floor(frameRate * frame_interval) == 0):
                    save_name = "Data/Training/Frames/Full/WolvesManCity122719frame%d.jpg" % count;count+=1
                    cv2.imwrite(save_name, frame)
                if count == num:
                    break
            cap.release()
        makeFullMatchFrames(len(h_images))
        n_images = glob.glob("Data/Training/Frames/Full/*.jpg")
        #print(h_images)
        # train_image_h = train_image_n = []
        # for i in range(len(h_images)):
        #     train_image_h.append(h_images[i])
        #     train_image_n.append(n_images[i])
        print("len(n_images): " , len(n_images))
        print("len(h_images): " , len(h_images))

        train_data_n = pd.DataFrame()
        train_data_n['image'] = n_images
        train_data_n['class'] = [0 for _ in range(len(n_images))]

        train_data_h = pd.DataFrame()
        train_data_h['image'] = h_images
        train_data_h['class'] = [1 for _ in range(len(h_images))]

        train_data = pd.concat([train_data_h, train_data_n])
        train_data = sklearn.utils.shuffle(train_data)

        train_data.to_csv('Data/Training/DF/train-milestone.csv', index=False)
