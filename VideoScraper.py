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
        self.videos = []

    def downloadVideos(self, query, channel=""):
        """
        Method: downloadVideos
        ----------------------
        This method will scrape youtube according to the query, and will download all of the videos and store them in a list.
        If a channel is specified, the function will perform the search on the youtube channel's page.
        ----------------------
        Arguments:
        query: the string that we want to search on YouTube
        channel: Optional argument that indicates if you want to search on a given channel's page
        ----------------------
        Return: None
        """
        pass

    def parseVideos(self):
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
        pass
