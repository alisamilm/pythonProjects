import pytube

url = input("enter youtube video url:")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)