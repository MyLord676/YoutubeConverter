import requests
# import html_to_mp3


def convertToMP3(url):
    r = requests.get("https://convert2mp3s.com/api/single/mp3?",
                     params={"url": url})
    # print(r.url)
    # print(r.status_code)
    # print(r.content)
    # print(r.text)
    return r


if __name__ == "__main__":
    convertToMP3("https://www.youtube.com/watch?v=O91DT1pR1ew")
