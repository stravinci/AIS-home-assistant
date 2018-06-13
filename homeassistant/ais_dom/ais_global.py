"""
Support for functionality to cache some data for AI-Speaker.
"""
import socket

# LV settings
G_EMPTY_OPTION = "-"

# TTS settings
GLOBAL_TTS_RATE = 1
GLOBAL_TTS_PITCH = 1
GLOBAL_TTS_VOICE = 'pl-pl-x-oda-local'

# audio nature
G_AN_RADIO = "Radio"
G_AN_PODCAST = "Podcast"
G_AN_MUSIC = "Music"
G_AN_AUDIOBOOK = "AudioBook"
G_AN_NEWS = "News"

GLOBAL_MY_IP = None


def get_my_global_ip():
    if GLOBAL_MY_IP is None:
        set_global_my_ip()
    return GLOBAL_MY_IP


def set_global_my_ip():
    global GLOBAL_MY_IP
    GLOBAL_MY_IP = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
              if not ip.startswith('127.')] or [[(s.connect(('8.8.8.8', 53)),
              s.getsockname()[0], s.close()) for s in
              [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]])
              + ['no IP found'])[0]


set_global_my_ip()

