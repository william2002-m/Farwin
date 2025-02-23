import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "27758016"
API_HASH = "8d34cfffe27ab461eabbf0091b1a27df"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7929316278:AAErd_5Qy2i3UktIopt_wyfRQLudUe8Lvz0"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://tennyson2002:tennyson2002@cluster0.h1vm3.mongodb.net/?retryWrites=true&w=majority&appName=Cluste0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002381091141"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "7364852621"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = "amrita44"
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = "HRKU-a19e584b-5b15-4b76-b429-258cbfc20a8e"

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Block2002/Amrita",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_ARCHITECT_II")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Tamil_Chat_TSS")

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
STRING1 = "BQC86fAAmKPgcZQyo-KYBNDCwhj4A6MFaGhrpft7RFDmEtl2V_r7J6oy6E7re0pHPRLf7AMMTSbDZeXelqMjZNQxkYYlHL6Owo_2qZOBybJdLyBcH0DeY6HyLevSCWiEFEA_oYmfMudAEm60GuWqUkNpBBzT-RnLGRToXLt5WLGAt8Ii9TYiEUhz-Rsnihzllvkc_I0dQ7tMpMSF1f5Z5VfPYdZIPO_MJyiv_fX_viHW5k6ZXNNxXVJk9bue_-GoWhakjOUESty_UIW6KSCI6kQPWF-MPQMF2sx5BC9khRtt1Yn-QGwBkzfqXQLKXJGSplTxzDQAX0AQyJFv-GZmJ7yCLdEnGAAAAAHKf4CbAA"
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
