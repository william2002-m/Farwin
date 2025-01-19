import asyncio
import re
import time
from logging import getLogger
from time import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFont
from pyrogram import enums, filters
from pyrogram.types import ChatMemberUpdated
import config
from JioSavaan import app
from JioSavaan.utils.database import get_assistant
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops
from pyrogram import filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pytz import timezone
from datetime import datetime
from pymongo import MongoClient
from config import MONGO_DB_URI

user_last_message_time = {}
user_command_count = {}
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

# --------------------------------------------------------------------------------- #


LOGGER = getLogger(__name__)

def convert_to_small_caps(text):
    # Mapping for regular letters to small caps
    mapping = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘϙʀꜱᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘϙʀꜱᴛᴜᴠᴡxʏᴢ",
    )
    return text.translate(mapping)


class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None


def circle(pfp, size=(80, 80), brightness_factor=10):
    pfp = pfp.resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.Resampling.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    
    
    border_size_violet = 5
    border_size_blue = 3   
    outline = Image.new("RGBA", (pfp.size[0] + 2 * border_size_violet, pfp.size[1] + 2 * border_size_violet), (0, 0, 0, 0))
    outline_draw = ImageDraw.Draw(outline)
    
    violet = (148, 0, 211, 255)  
    blue = (0, 0, 255, 255)      
    red = (19, 136, 8, 255)    
    
    outline_draw.ellipse((0, 0, outline.size[0], outline.size[1]), outline=violet, width=border_size_violet)
    outline_draw.ellipse((border_size_violet - border_size_blue, border_size_violet - border_size_blue,
                          outline.size[0] - (border_size_violet - border_size_blue),
                          outline.size[1] - (border_size_violet - border_size_blue)), 
                          outline=blue, width=border_size_blue)

    
    outline_draw.ellipse((border_size_violet, border_size_violet,
                          outline.size[0] - border_size_violet,
                          outline.size[1] - border_size_violet), 
                          outline=red, width=border_size_violet)

    outline.paste(pfp, (border_size_violet, border_size_violet), pfp)
    
    return outline

def welcomepic(user_id, user_username, user_names, chat_name, user_photo, chat_photo):
    background = Image.open("JioSavaan/assets/Well7.png")
    user_img = Image.open(user_photo).convert("RGBA")
    chat_img = Image.open(chat_photo).convert("RGBA")
    
    chat_img_circle = circle(chat_img, size=(190, 190), brightness_factor=1.2)
    user_img_circle = circle(user_img, size=(190, 190), brightness_factor=1.2)
    
    background.paste(chat_img_circle, (280, 260), chat_img_circle)
    background.paste(user_img_circle, (727, 260), user_img_circle)
    
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("JioSavaan/assets/font.ttf", size=32)

  
    red = (255, 153, 51)  
    pink = (255, 255, 255)   
    yellow = (19, 136, 8)

    draw.text((450, 443), f"Name:  {user_names}", fill=yellow, font=font)
    draw.text((450, 483), f"User Id:  {user_id}", fill=yellow, font=font)
    draw.text((450, 515), f"Username:  {user_username}", fill=yellow, font=font)
    
    background.save(f"downloads/welcome#{user_id}.png")
    return f"downloads/welcome#{user_id}.png"

welcomedb = MongoClient(MONGO_DB_URI)
status_db = welcomedb.welcome_status_db.status

async def get_welcome_status(chat_id):
    status = status_db.find_one({"chat_id": chat_id})
    if status:
        return status.get("welcome", "on")
    return "on"

async def set_welcome_status(chat_id, state):
    status_db.update_one(
        {"chat_id": chat_id},
        {"$set": {"welcome": state}},
        upsert=True
    )

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    user_id = message.from_user.id
    current_time = time()

    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            hu = await message.reply_text(
                f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**"
            )
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        state = message.text.split(None, 1)[1].strip().lower()
        current_status = await get_welcome_status(chat_id)

        if state == "off":
            if current_status == "off":
                await message.reply_text("ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ!")
            else:
                await set_welcome_status(chat_id, "off")
                await message.reply_text(f"ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ{message.chat.title}ʙʏ ʙᴏᴛ")
        elif state == "on":
            if current_status == "on":
                await message.reply_text("ᴇɴᴀʙʟᴇᴅ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ!")
            else:
                await set_welcome_status(chat_id, "on")
                await message.reply_text(f"ᴇɴᴀʙʟᴇᴅ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ{message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!")

@app.on_chat_member_updated(filters.group, group=-4)
async def greet_new_members(_, member: ChatMemberUpdated):
    try:
        chat_id = member.chat.id

        welcome_status = await get_welcome_status(chat_id)
        if welcome_status == "off":
            return

        chat = await app.get_chat(chat_id)
        user = member.new_chat_member.user
        user_id = user.id
        user_mention = user.mention

        chat_name = chat.title if chat.title else "Anjan Group"
        user_username = f"@{user.username}" if user.username else "No Username"
        user_name = user.first_name if user.first_name else "No Name"
        user_names = user.first_name if user.first_name and re.match("^[A-Za-z0-9 ]+$", user.first_name) else "New Member"
       
        ist = timezone('Asia/Kolkata')
        joined_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

        if member.new_chat_member and not member.old_chat_member:
            try:
                users_photo = await app.download_media(
                    user.photo.big_file_id, file_name=f"pp{user.id}.png"
                )
                user_photo = users_photo if users_photo else "assets/nodp.png"
            except AttributeError:
                user_photo = "assets/nodp.png"
            
            try:
                groups_photo = await app.download_media(
                    member.chat.photo.big_file_id, file_name=f"chatpp{chat_id}.png"
                )
                chat_photo = groups_photo if groups_photo else "assets/nodp.png"
            except AttributeError:
                chat_photo = "assets/nodp.png"
            
            welcomeimg = welcomepic(user_id, user_username, user_names, chat_name, user_photo, chat_photo)
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton(f"{convert_to_small_caps('๏ add me in new group ๏')}", url=f"https://t.me/{app.username}?startgroup=true")]]
            )

            if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
                try:
                    await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
                except Exception as e:
                    LOGGER.error(e)

try:
    # Replace this with actual user fetching logic
    user = None  # Simulating user fetching logic; replace with actual logic
    # Simulate fetching user data (this is where an error might occur)
    if user is None:  # Check if user is None (or handle based on your fetching logic)
        raise ValueError("User not found")  # Simulating an error for demonstration

    # If user is found, construct the welcome text
    welcome_text = (
        f"◦•●◉✿ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒃𝒂𝒃𝒚 ✿◉●•◦\n\n"
        f"▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰\n"
        f"👤 𝑵𝒂𝒎𝒆 ➥ {user.first_name}\n"
        f"🆔 𝑼𝒔𝒆𝒓 𝑰𝑫 ➥ {user.id}\n"
        f"🔗 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 ➥ @{user.username}\n"
        f"📩 𝑴𝒆𝒏𝒕𝒊𝒐𝒏 ➥ {user.mention}\n"  
        f"🌱 𝑪𝒉𝒂𝒕 𝑻𝒊𝒕𝒍𝒆 ➥ {chat_name}\n"
        f"🕒 𝑱𝒐𝒊𝒏𝒆𝒅 𝐴t ➥ {joined_time}\n\n"
        f"❖ 𝐵𝐸𝐿𝐿𝐸𝐶𝐼𝐴𝐷𝐸 ➥ 𝐵𝐸𝐿𝐿𝐸𝐶𝐼𝐴𝐷𝐸\n"
        f"▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰"
    )
except ValueError as ve:
    # Handle the case where the user was not found
    welcome_text = (
        f"◦•●◉✿ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒃𝒂𝒃𝒚 ✿◉●•◦\n\n"
        f"▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰\n"
        f"👤 𝑵𝒂𝒎𝒆 ➥ Unknown User\n"
        f"🆔 𝑼𝒔𝒆𝒓 𝑰𝑫 ➥ Unknown\n"
        f"🔗 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 ➥ @unknown\n"
        f"📩 𝑴𝒆𝒏𝒕𝒊𝒐𝒏 ➥ @unknown\n"  
        f"🌱 𝑪𝒉𝒂𝒕 𝑻𝒊𝒕𝒍𝒆 ➥ {chat_name}\n"
        f"🕒 𝑱𝒐𝒊𝒏𝒆𝒅 𝐴t ➥ {joined_time}\n\n"
        f"❖ 𝐵𝐸𝐿𝐿𝐸𝐶𝐼𝐴𝐷𝐸 ➥ 𝐵𝐸𝐿𝐿𝐸𝐶𝐼𝐴𝐷𝐸\n"
        f"▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰"
    )
except Exception as e:
    # Handle any other unexpected exceptions
    welcome_text = "An unexpected error occurred."

# Now you can use welcome_text as needed
print(welcome_text)
            await app.send_photo(chat_id, photo=welcomeimg, caption=welcome_text, reply_markup=reply_markup)

    except Exception as e:
        LOGGER.error(e)
        return
