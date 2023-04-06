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



API_ID = int(getenv("API_ID", "18302370"))
API_HASH = getenv("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = getenv("BOT_TOKEN", "5924932917:AAFHC6sQkot3C1GHeurOuY_K3eG-75KJ7LY")

ADMINS = []
for usr in environ.get('ADMINS', "5821736028 1957296068").split():
    ADMINS.appemd (int(usr))

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
    db.add_user(message.from_user.id)
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
    add_group(chat.id)
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    img = "https://telegra.ph/file/b959b8e70ea930e739728.jpg"
    add_user(user.id)
    #nothingenter
    await client.send_photo(user.id,img, "**Hello {} Welcome To 🌸 {} 🌸\n\nPowerd By :@CinemavillaAutoAccept**".format(message.from_user.mention, message.chat.title))

    
@Client.on_message(filters.command("acceptedlist") & filters.user(ADMINS))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)
    



    
@Client.on_message(filters.command("bcast") & filters.user(ADMINS))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

    
  


    
      
Client.start()
print("Bot Started!")

idle()


Client.stop()
print("Bot Stopped!")
    
    
