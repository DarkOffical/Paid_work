from os import environ, getenv 
from pyrogram import idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from pyrogram.types import Message, User, ChatJoinRequest
from approvedb import db
import time


API_ID = int(getenv("API_ID", "18302370"))
API_HASH = getenv("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = getenv("BOT_TOKEN", "5924932917:AAFHC6sQkot3C1GHeurOuY_K3eG-75KJ7LY")

ADMINS = []
for usr in environ.get('ADMINS', "5821736028 1957296068").split():
    ADMINS.append (int(usr))

START_MSG = "<b>Hᴇʟʟᴏ Iᴀᴍ Pʀɪᴠᴀᴛᴇ Bᴏᴛ CɪɴᴇMᴀVɪLLᴀ™ Oғɪᴄᴄɪᴀʟʏ Mᴀᴅᴇᴅ Fᴏʀ Aᴜᴛᴏ Aᴄᴄᴇᴘᴛ Iɴ Cʜᴀɴɴᴇʟꜱ..</b>"




Client = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins={"root": "plugins"},
             workers=300
             )
gif = [
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4'
]

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    user = message.from_user.id
    if not await db.is_user_exist(user):
        await db.add_user(user)  
    buttons = [[
        InlineKeyboardButton('Oᴡɴᴇʀ', user_id='5821736028'),
        InlineKeyboardButton('Cʜᴀɴɴᴇʟ', url='https://t.me/+Vb7QOqxBNHRmYzZk')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=START_MSG.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
    )
    
        
        

    
@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client: Client, message: Message):
    chat=message.chat # Chat
    #🥳🥳🔥
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)    
    img = "https://telegra.ph/file/b959b8e70ea930e739728.jpg"
    #1🔥12🍚👌🏻
    #nothingenter
    await client.send_photo(user.id,img, "**Hello {} Welcome To 🌸 {} 🌸\n\nPowerd By :@CinemavillaAutoAccept**".format(message.from_user.mention, message.chat.title))

@Client.on_message(filters.command("users") & filters.user(ADMINS))
async def list(bot, message):
    total_users = await db.total_users_count()
    await message.reply_text(f"Total Users Started : {total_users}")

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def verupikkals(bot, message):    
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0
    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")

      
Client.start()
print("Bot Started!")

idle()


Client.stop()
print("Bot Stopped!")
    
    
