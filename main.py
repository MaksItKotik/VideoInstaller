#
# Author : Maks Makaliuk
# Email : m.makaliuk@gmail.com
# Date: 18.02.2021
# Version: 1.0
# Time: 18:26
# User: Maks Makaliuk
#
# This program I made for dowload YouTube videos
#

import eel
from pytube import YouTube


eel.init('web')

@eel.expose
def dowload(url):
	video = YouTube(url)

	video_title = "Title: "+video.title
	video_previu = video.thumbnail_url
	
	dow_fil = video.streams.filter(progressive="True", res="720p")

	eel.video_return(video_title, video_previu)

	dow_fil.first().download()


eel.start('index.html', size = (1300, 800))

