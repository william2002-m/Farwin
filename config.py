import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "27758016"
API_HASH = "8d34cfffe27ab461eabbf0091b1a27df"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7632736990:AAEciuOcUzLVKKBYEwsmpcVLVpsbCEkKBX0"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://cookies2002boy:cookies2002boy@cluster0.bc2ox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002381091141"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "7364852621"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = "farwin04"
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = "HRKU-a19e584b-5b15-4b76-b429-258cbfc20a8e"

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/william2002-m/Farwin",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_ARCHITECT_II")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TamilChatNL")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "700"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQC86fAAnWkH4HHxKsfwL6TOfhrngNf9D3D1f1tYeqDIc-NvI9HSyxfJPQTX6wSN7efTcfZ0Z3bUEVhKGNJBVY6apB9UYhL22B5adwsbdHliI2mnr2Ezmetb3Yx-P31kYL7Bdx0hy3t-gkdJw8Fmwn8Wkqr2Mr-iAHqNSu6-Wl3arie_bTNZwfQ2aPhsaM_6r0YDo06EZgMf4zu6IPJCUr1Hwv_44OnMkF2WlShuu-QvcdB_ORlO1gFAB_VWKP8GggvgLN_iBFtj8OwWPExkPvqE4Q6D63zB49-7fmzEOSR9HTW7JK38ce2e8ToKbeY6hbIUg42_UxCd3sKjj4AfZDYBd_3-OQAAAAHjgUoeAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/rEw.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/r2A.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/rw8.jpg"
STATS_IMG_URL = "https://envs.sh/r2j.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/CLg.jpeg"
TELEGRAM_VIDEO_URL = "https://envs.sh/CLg.jpeg"
STREAM_IMG_URL = "https://envs.sh/CLg.jpeg"
SOUNCLOUD_IMG_URL = "https://envs.sh/CLg.jpeg"
YOUTUBE_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/CLg.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/CLg.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 800**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
