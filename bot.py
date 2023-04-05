from os import environ
from pyrogram import idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep
from approvedb import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from pyrogram.types import Message, User, ChatJoinRequest
from info import LOG_CHANNEL, ACC_SND_LOG, CAPTION_TEXT
from datetime import date, datetime 
import pytz


API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = environ.get('BOT_TOKEN', "6035089548:AAEND3aHeh6uTSVcERkuA7yGFOz6R8GU6nM")
SESSION = environ.get('SESSION', "")
TIME = environ.get('TIME', 600)
GROUPS = []
for grp in environ.get('GROUPS', "-1001784914514").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get('ADMINS', "1957296068").split():
    ADMINS.append(int(usr))
ACC_ALL_CHAT = "-1001866499414"
START_MSG = "<b>Hᴇʏ {} Iᴀᴍ Pʀɪᴠᴀᴛᴇ Bᴏᴛ Mᴀꜱᴛᴇʀ Oғ Tᴏ Uꜱᴇ Aᴜᴛᴏ Dᴇʟᴇᴛᴇ Aᴜᴛᴏ Aᴄᴄᴇᴘᴛ Aɴᴅ Mᴏʀᴇ...</b>\n<b>Iᴀᴍ Oғғɪᴄɪᴀʟʏ Wᴏʀᴋɪɴɢ Fᴏʀ Fɪʟɪᴍ Hᴏᴍᴇ Gʀᴏᴜᴘ</b>\n<b>Dᴏɴ'ᴛ Wᴀꜱᴛᴇ Yᴏᴜʀ Tɪᴍᴇ Tᴏ Aᴅᴅɪɴɢ Yᴏᴜʀ Gʀᴏᴜᴘ.. Iᴀᴍ Wᴏʀᴋꜱ Oɴʟʏ Mʏ Gʀᴏᴜᴘ</b>"





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
    add_user(message.from_user.id)
    buttons = [[
        InlineKeyboardButton('Oᴡɴᴇʀ', user_id='1957296068'),
        InlineKeyboardButton('Gʀᴏᴜᴘ', url='https://t.me/MaSTeR_filims')
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
    img = random.choice(gif)
    add_user(user.id)
    #nothingenter
    await client.send_video(user.id,img, "**Hello {}!\nYour Request To Join {} was approved👍\n\n⚠️click /start to see my power Powered By @sinimapremi **".format(message.from_user.mention, message.chat.title))
    if ACC_SND_LOG == "on":
        await client.send_message(LOG_CHANNEL, "**#New_Approval\n\n Name: {} \n\n Chat: {} \n\n By**".format(message.from_user.mention, message.chat.title))
            
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

    
  

@
    chnl = await User.create_channel("Channel Title", "Channel Description")
    await User.set_chat_photo(chat_id=chnl.id, photo="https://graph.org/file/0fab719eb1576a17830eb.jpg")
                             
    await message.reply_text(f"id : {chnl.id}")


@Client.on_message(filters.command('linkdls') & filters.private)
async def start(bot, message):
    data = message.text
    command, cid, clink = data.split(" ")  
    mrn = await Client.get_chat_invite_link(chat_id=f'{cid}', invite_link=f'{clink}')
    await message.reply_text(f"details : {mrn}")
                                           
@Client.on_callback_query(filters.regex(r"^time"))
async def pm_next_page(bot, query):
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%I:%M:%S %p")
    await query.answer(f"Hᴇʏ Bʀᴏ👋\n\nCᴜʀʀᴇɴᴛ Tɪᴍᴇ Iɴ Iɴᴅɪᴀ : {time}", show_alert=True)

@Client.on_callback_query(filters.regex(r"^date"))
async def pm_next_parge(bot, query):
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%I:%M:%S %p")
    await query.answer(f"Tᴏᴅᴀʏ 🎗 \n 🗓 : {today}", show_alert=True)


      
Client.start()
print("Bot Started!")

idle()


Client.stop()
print("Bot Stopped!")
    
    
