from pytube import YouTube

def convertToMP3(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    return video.download(output_path="./temp")

if __name__ == "__main__":
    convertToMP3("https://www.youtube.com/watch?v=O91DT1pR1ew")