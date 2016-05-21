# nano-web-crawler
  
# Brief  
A nano web crawler that downloads videos from youtube according to a search query and extracts video frames every 'x time'.  
  
    
## Python Script
- Search query keywords are defined in an array.  
- A downloader thread is created and started per search query keyword in the array.   
- Downloaded videos are saved in a previously define path in the system.   
  
## C++ code
- Reads downloaded files.  
- Captrues frames every 'x μs'.  
- Saves frames in JPEG format.  
  
## Libraries
- Pafy Python library: downloading YouTube content and retrieve metadata.  
http://pythonhosted.org/Pafy  
- Google ajax search api: for searching for videos. (last day of operation was September 29, 2014; after developemnt)  
https://developers.google.com/web-search/
- Opencv C++ library (core + highgui modules): for processing video and capturing frames.  
http://opencv.org/
