import urllib
from bs4 import BeautifulSoup
from pytube import YouTube
import cv2
import os
import glob
import numpy as np

def downloadVideos(query, path, channel="", maxNumVids=100, clip_len=30):
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
    search = urllib.parse.quote(query)
    print(search)
    url = "https://www.youtube.com/results?search_query=" + search
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for i, vid in enumerate(soup.findAll(attrs={'class':'yt-uix-tile-link'})): #Line that doesn't work
        if i >= maxNumVids:
            break
        filename = vid['href']
        download_from_url('https://www.youtube.com' + filename, filename, path)
        parseVideo(path, filename, clip_len)
        os.remove(path + filename)

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
        YouTube(url).streams.first().download(filename=filename, output_path=path)
        print(f"Video {filename} downloaded successfully")
    except Exception as exc:
        print(f"Tried to download {filename}, but it did not work because {exc}...")

def parseVideo(path, clip_len=30):
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
    # for video in os.listdir(path + vid_path):
    counter = 0
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # print(f"FPS is {fps}")
    hasFrames = True
    frames = []
    allFrames = []
    while True:
        hasFrames, image = cap.read()
        if not hasFrames:
            break
        grayImg  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        compr_img = cv2.resize(grayImg, (int(grayImg.shape[0] * 0.1), int(grayImg.shape[1] * 0.1)))
        if counter % fps == 0:
            frames.append(compr_img)
        if len(frames) == clip_len:
            allFrames.append(frames)
            frames = []
        counter += 1
    np.save(path[:-4], np.array(allFrames))
    print(f"Video {path} was parsed successfully")
