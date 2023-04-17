import re
from os import environ
import os
#try
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

LOG_CHANNEL = environ.get('LOG', '-1001913972599')

ACC_SND_LOG =environ.get('SND', 'on')
                         
ACC_DB = environ.get('DB', 'mongodb+srv://Mst:Mst@cluster0.0sjrq6j.mongodb.net/?retryWrites=true&w=majority')

DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))

CAPTION_TEXT = environ.get('C_CAPTION', '{file_name}')
                          
                           
