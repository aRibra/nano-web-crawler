import pafy
import urllib.request
import json
import os
import threading
import time


homeDir = '/home/python_workspace/retrieved_videos'
overallDownloadingTime = 0

if not os.path.exists(homeDir):
            os.mkdir(homeDir)

### Top of Function 'search' ###
def search(searchWord):

    startTime = time.time()
    print(searchWord, 'Downloader Thread started: ', startTime)
    
    encoded = urllib.request.pathname2url(searchWord)#adds percent for every space

    rawData = urllib.request.urlopen('http://ajax.googleapis.com/ajax/services/search/video?v=1.0&q='+encoded+'site:youtube.com').read().decode("utf-8")
    jsonData = json.loads(rawData)
    searchResults = jsonData['responseData']['results']

    counter = 0
    for er in searchResults:
        title = er['title']
        videoUrl = er['url']
        video = pafy.new(videoUrl)
        best = video.getbest(preftype="3gp")

        print (title)
        print (videoUrl)
        print (best.resolution, best.extension)
        print('\n')

        parentDirPath = homeDir + '/' + searchWord
    
        if not os.path.exists(parentDirPath):
            os.mkdir(parentDirPath)
    
        videoFolder = counter    
        videoFolderPath = parentDirPath + '/video' + str(videoFolder)
        print (videoFolderPath)
    
        if not os.path.exists(videoFolderPath):
           os.mkdir(videoFolderPath)

        newThread = threading.Thread(target=download, args=(best, videoFolderPath,))
        newThread.daemon = True
        newThread.start()
        
##        best.download(filepath = videoFolderPath, quiet = True)

        counter += 1;
    
    endTime = time.time() - startTime
    
    global overallDownloadingTime
    overallDownloadingTime += endTime
    
    print(searchWord + ' Downloading finished: ', endTime)
    print ('\n\n\n')
    
    ### End of Function 'search' ###

### Top of Function 'download' ###
def download(best, videoFolderPath):
    best.download(filepath = videoFolderPath, quiet = True)
    
    ### End of Function 'download' ###
    


### MAIN EXECUTION ###
if __name__ == "__main__":
    
    objects = ['bear', 'flower', 'eagle', 'kangaroo', 'snake', 'bird']

    for obj in objects:
        newThread = threading.Thread(target=search, args=(obj,)) # the comma (obj,) is mandatory here
        newThread.daemon = True
        newThread.start()
        newThread.join()
        print ('\n\n\n')

    print('Download Time: ', overallDownloadingTime)






    
