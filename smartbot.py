#this is new file for the functions of chatbot
from subprocess import call
class SmartBot:
    def __init__(self):
        self.request_num = 0
        self.play_music = False
        self.play_youtube = False
        self.download_torrent = False
        self.download_video_site = False
        self.stop_music = False
        self.stop_youtube = False
        self.decrease_volume = False
        self.increase_volume = False
        self.stop_downloads = False

    def handle_request(self,request_num=None,request_string=None):
        if (request_num is None and request_string is not None and request_string.lower() is "hi" or 
                request_string.lower() is "smarty" or
                request_string.lower() is "hello"):
            response = ("Hello..what you want"
                        "1.play music"
                        "2.play something on youtube"
                        "3.download using torrent:P"
                        "4.download a video from someplace!!!"
                        "5.stop music"
                        "6.stop youtube"
                        "7.decrease volume"
                        "8.increase volume"
                        "9.stop downloads")
        elif (request_num is not None and
              request_num is 1):
            self.play_music = True
            play_music_func()
            response = "playing music.."
        elif (request_num is not None and
            request_num is 2):
            self.play_youtube = True
            play_youtube_func()
            response = "playing youtube.."
        elif (request_num is not None
            request_num is 3):
            self.download_torrent = True
            response = "what you want to download ?"
        elif (request_num is None and self.download_torrent is True
        )

        
    
     