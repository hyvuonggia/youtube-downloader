import pytube

DESTINATION_FOLDER = 'D:\\Gia Hy\\Videos'

video_list = []

print("Enter URLs (ENTER to start downloading): ")

while True:
    url = input("")
    if url == "":
        break
    video_list.append(url)


for x, video in enumerate(video_list):
    try:
        print(f"Downloading video {x + 1}...")
        v = pytube.YouTube(video)
        stream = v.streams.get_by_itag(22)
        stream.download(DESTINATION_FOLDER)
        print("DONE \n")
    except AttributeError:
        print("FAILED (this video contains copyright sound)\n")
    except (pytube.exceptions.RegexMatchError, KeyError):
        print("FAILED (please specify youtube video's URL)\n")
    except ConnectionAbortedError:
        print("FAILED (internet interrupted)")

input("=====FINISHED DOWNLOAD=====")
