from pytube import YouTube
import sys

if len(sys.argv) != 2:
    print("Enter YouTube video link -only")
    exit()
link = str(sys.argv[1])
try:
    yt = YouTube(link)
    def download_video():
        yd = yt.streams.get_highest_resolution()
        if yd is not None:
            print("Downloading...")
            yd.download("./Downloads")
            print("Download Successful!")
        else:
            print("Error Occured!")
        
    print("Video title: ",yt.title)
    download_video()
except:
    print("Invalid Link")

 