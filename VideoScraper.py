import urllib
from bs4 import BeautifulSoup
from pytube import YouTube
import cv2
import os
import glob
import numpy as np

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

    def download_from_url(url, filename, path):
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
            video = YouTube(url)
            output_file = video.download(filename, output_path=path)
            print(f"Video {url} downloaded successfully")
        except Exception as exc:
            print(f"Tried to download {url}, but it did not work because {exc}...")

    def parseVideos(self, path):
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
        for video in os.listdir(path):
            cap = cv2.VideoCapture(video)
            hasFrames = True
            frames = []
            while hasFrames:
                hasFrames, image = cap.read()
                frames.append(image)
            videos.append(frames)
        return videos
