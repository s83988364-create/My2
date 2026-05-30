import asyncio
import time
import random
import json
import os
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType, ChatMemberStatus
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

#=============== CONFIG ================
API_ID = 39035274
API_HASH = "6a0b24e16c4bea2bbc975b7dbb0c1e64"
BOT_TOKEN = "8931408596:AAHpQAeA0iLWLQjrltfJ1RZYfrh5HNrSbGQ"
OWNER_ID = 8722144519
BOT_USERNAME = "ll_SUPRRME_XD_ll_BOT"

#=============== CUSTOM LINES ================
CUSTOM_LINES = [

    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    "bahenklodo tumhari maa meri setting",
    "bahenklodo tumhari maa meri setting",
    "teri mummy randi h randi bsdk",
    "teri mummy ki pussy m scooter dalduga",
    "teri mummy ki pussy me cum krduga randi maa k bache",
    "tera khandan hi randiyo ka h",
    "teri dadi ki pussy me mera lund",
    "teri mummy ko chodkr ulta ltkakr uske muh me loda deduga",
    "teri mummy ko deepthroat deduga madarchod k bache",
    "✌️✌️tera papa bhi randi ki aulad h bsdk",
    "teri mummy ko yoga sikhaduga aur usko different styles me choduga",
    "tera papa hu mai teri mummy ka bf jis s vo chudkr gyi thi",
    "teri maa ki pussy me scooter dalduga bahen k lode🤣🤣",
    "teri maa ki chut me bihari gutka khakr thuk kr chale gye the🔥🔥",
    "💀💀teri maa ka bosda randi k beej",
    "✌️✌️teri maa ki chut me 2finger dekr uska paani nikalduga0",
    "🔥🔥teri maa k muh me gass pipe dekr uski gaand me fire lgakr tere baap ki gaand jalauga",
    "😂😍😍teri randi maa ko chodkr maine gb road pr beach diya tha",
    "🙌🙌teri mummy k haath divar pr lgvadiye the 10bihariyo ne",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰ℙ𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
]

# =============== DUMMY SERVER FOR RENDER ================

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

    def log_message(self, format, *args):
        pass


def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


# Start server thread for Render
threading.Thread(target=run_server, daemon=True).start()

app = Client(
    "fast_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

#=============== DATA STORAGE ================
sudo_users = {OWNER_ID}
muted_users = set()
spam_active = False
spam_target = None
spam_count = 0
sticker_spam_active = False
custom_stickers = []

# Variables for custom lines spam
custom_spam_active = False
custom_spam_task = None

#=============== SHAYARI STORAGE ================
shayari_data = {
    "love": [],
    "sad": [],
    "birthday": [],
    "general": []
}

#=============== DEFAULT SHAYARI ================
default_shayari = {
    "love": [
        "❤️ प्यार में यूं मिलते हैं दिल,\nजैसे सागर में मिलती है नदी।\nतुमसे मिलकर लगता है,\nये दुनिया है सबसे हसीन! 💕",
        "💝 तेरी एक मुस्कान,\nबदल देती है मेरी पहचान।\nतू है तो मैं हूं,\nतू नहीं तो कुछ नहीं! 🌹"
    ],
    "sad": [
        "🥀 टूटे दिल का दर्द,\nसमझता है कोई और।\nहंसते हुए चेहरे के पीछे,\nदेखता है कोई और! 😢",
        "💔 अकेले बैठे हैं हम,\nतेरी यादों के सहारे।\nतू नहीं तो क्या हुआ,\nहै तेरी तस्वीर हमारे पास! 🥺"
    ],
    "birthday": [
        "🎂 जन्मदिन मुबारक हो आपको,\nहर खुशी हो आपके संग।\nखुशियां हों आपके पास इतनी,\nजितने आसमान में हैं बादल! 🎉",
        "🎈 हर पल खुशियों से भरा हो,\nहर दिन नया उजियारा हो।\nआपका जीवन फूलों जैसा महके,\nहर सपना हकीकत में ढले! 🌟"
    ],
    "general": [
        "💫 जिंदगी एक सफर है,\nअलग-अलग रंग लिए।\nकभी हंसी तो कभी आंसू,\nकभी प्यार तो कभी गम लिए! 🌈",
        "🌙 तन्हाई में अक्सर मिलता है सुकून,\nहवाओं में बसती हैं कहानियां।\nहर दर्द कहता है एक किस्सा,\nहर खुशी में छिपी होती है जवानियां! ⭐"
    ]
}

#=============== LOAD DATA ================
def load_data():
    global sudo_users, custom_stickers, shayari_data

    try:
        if os.path.exists("sudo_users.json"):
            with open("sudo_users.json", "r") as f:
                sudo_users = set(json.load(f))

        if os.path.exists("custom_stickers.json"):
            with open("custom_stickers.json", "r") as f:
                custom_stickers = json.load(f)

        if os.path.exists("shayari_data.json"):
            with open("shayari_data.json", "r") as f:
                shayari_data = json.load(f)

    except Exception as e:
        print(f"Error loading data: {e}")


def save_data():
    with open("sudo_users.json", "w") as f:
        json.dump(list(sudo_users), f)

    with open("custom_stickers.json", "w") as f:
        json.dump(custom_stickers, f)

    with open("shayari_data.json", "w") as f:
        json.dump(shayari_data, f)

#=============== INIT SHAYARI ================
def init_shayari():
    for category in default_shayari:
        if not shayari_data.get(category):
            shayari_data[category] = default_shayari[category]

    save_data()

#=============== BUTTONS ================
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me Baby", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🏠 My Home", callback_data="home")],
        [InlineKeyboardButton("👑 My Master", url="https://t.me/ll_SUPRRME_XD_ll")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⚡ Get Sudo", url="https://t.me/ll_SUPRRME_XD_ll")]
    ])
    return keyboard

#=============== CUSTOM LINES SPAM FUNCTION ================
async def custom_spam_loop(client, chat_id, target_user_id, count):
    global custom_spam_active
    
    target_user = await client.get_users(target_user_id)
    mention = target_user.mention
    
    for i in range(count):
        if not custom_spam_active:
            break
        
        line = random.choice(CUSTOM_LINES)
        
        try:
            await client.send_message(chat_id, f"{mention} {line}")
            await asyncio.sleep(0.3)  # Delay to avoid flood
        except Exception as e:
            print(f"Custom spam error: {e}")
            break

#=============== CUSTOM LINES SPAM COMMAND ================
@app.on_message(filters.command("r", prefixes=["."]) & filters.group)
async def custom_r_command(client, message: Message):
    global custom_spam_active, custom_spam_task
    
    # Check sudo permission
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return
    
    # Check if replied to a user
    if not message.reply_to_message:
        await message.reply_text("❌ Please reply to a user and use: .r <count>")
        return
    
    # Parse command
    parts = message.text.split()
    
    if len(parts) != 2:
        await message.reply_text("❌ Usage: .r <count>\nExample: .r 10")
        return
    
    try:
        count = int(parts[1])
        
        if count > 200:
            await message.reply_text("❌ Max limit is 200!")
            return
        
        if count < 1:
            await message.reply_text("❌ Count must be at least 1!")
            return
            
    except ValueError:
        await message.reply_text("❌ Invalid number! Please provide a valid count.")
        return
    
    target_user = message.reply_to_message.from_user
    chat_id = message.chat.id
    
    # Stop any existing spam
    if custom_spam_active:
        custom_spam_active = False
        if custom_spam_task:
            custom_spam_task.cancel()
        await asyncio.sleep(0.5)
    
    # Start new spam
    custom_spam_active = True
    
    # Send confirmation
    await message.reply_text(
        f"✅ Custom lines spam started!\n"
        f"🎯 Target: {target_user.first_name}\n"
        f"🔢 Count: {count}\n"
        f"📝 Using {len(CUSTOM_LINES)} custom lines\n"
        f"⚡ Use .stopr to stop!"
    )
    
    # Run spam in background
    custom_spam_task = asyncio.create_task(
        custom_spam_loop(client, chat_id, target_user.id, count)
    )
    
    # Wait for completion
    try:
        await custom_spam_task
        if custom_spam_active:
            await message.reply_text(f"✅ Custom lines spam completed! Sent {count} messages.")
    except asyncio.CancelledError:
        pass
    finally:
        custom_spam_active = False

#=============== STOP CUSTOM SPAM ================
@app.on_message(filters.command("stopr", prefixes=["."]) & filters.group)
async def stop_custom_spam(client, message: Message):
    global custom_spam_active, custom_spam_task
    
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return
    
    if custom_spam_active:
        custom_spam_active = False
        if custom_spam_task:
            custom_spam_task.cancel()
        await message.reply_text("🛑 Custom lines spam stopped!")
    else:
        await message.reply_text("⚠️ No active custom lines spam to stop!")

#=============== START COMMAND ================
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user

    await message.reply_text(
        f"🔥 Welcome {user.first_name}! 🔥\n\n"
        f"I'm a powerful group management bot.\n\n"
        f"Use buttons below to explore!",
        reply_markup=get_main_keyboard()
    )

#=============== BUTTON CALLBACK HANDLER ================
@app.on_callback_query()
async def button_callback(client, callback_query):
    data = callback_query.data

    if data == "help":
        help_text = """
🤖 BOT COMMANDS 🤖

📊 Utility:
• .alive - Check bot status
• .ping - Check bot speed
• .speed - Bot response time

💬 Shayari:
• .love - Love shayari
• .sad - Sad shayari
• .shayari - General shayari
• .birthday - Birthday wishes
• .addshayari - Add shayari

⚡ Sudo Commands:
• .mute - Mute user globally
• .unmute - Unmute user
• .sticker - Sticker spam
• .stopraid - Stop sticker spam
• .spam - Spam user with custom message
• .stopspam - Stop custom spam
• .r <count> - Send random custom lines to replied user
• .stopr - Stop custom lines spam

👑 Owner Only:
• .addsticker - Add sticker
• .addsudo - Add sudo user
• .removesudo - Remove sudo user
• .sudolist - List sudo users
• .mutelist - List muted users

💫 Custom Lines Active: {len(CUSTOM_LINES)} lines
"""

        await callback_query.message.edit_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    elif data == "back":
        await callback_query.message.edit_text(
            "🔥 Welcome Back! 🔥\n\nUse buttons below to explore!",
            reply_markup=get_main_keyboard()
        )

    elif data == "home":
        await callback_query.message.edit_text(
            f"🏠 My Home\n\n"
            f"📊 Bot Stats:\n"
            f"• Sudo Users: {len(sudo_users)}\n"
            f"• Muted Users: {len(muted_users)}\n"
            f"• Stickers: {len(custom_stickers)}\n"
            f"• Custom Lines: {len(CUSTOM_LINES)}\n"
            f"• Status: Active 🟢\n\n"
            f"👑 Owner: {OWNER_ID}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    await callback_query.answer()

#=============== UTILITY COMMANDS ================
@app.on_message(filters.command("alive", prefixes=[".", "/"]) & filters.group)
async def alive_command(client, message: Message):
    await message.reply_text("✅ Bot is Online! 🚀")


@app.on_message(filters.command("ping", prefixes=[".", "/"]) & filters.group)
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("🏓 Pinging...")
    end = time.time()

    ping_time = round((end - start) * 1000)

    await msg.edit_text(f"🏓 Pong!\n⏱️ {ping_time}ms")


@app.on_message(filters.command("speed", prefixes=[".", "/"]) & filters.group)
async def speed_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("⚡ Checking speed...")
    end = time.time()

    response_time = round((end - start) * 1000)

    await msg.edit_text(
        f"⚡ Bot Speed\n📡 Response Time: {response_time}ms\n🚀 Status: Super Fast!"
    )

#=============== SUDO CHECK ================
def is_sudo(user_id):
    return user_id in sudo_users

#=============== MUTE COMMAND ================
@app.on_message(filters.command("mute", prefixes=[".", "/"]) & filters.group)
async def mute_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not message.reply_to_message:
        await message.reply_text("❌ Please reply to a user to mute them!")
        return

    target_user = message.reply_to_message.from_user
    mention = target_user.mention

    muted_users.add(target_user.id)
    save_data()

    await message.reply_text(f"✅ {mention} has been muted!")

#=============== UNMUTE COMMAND ================
@app.on_message(filters.command("unmute", prefixes=[".", "/"]) & filters.group)
async def unmute_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not message.reply_to_message:
        await message.reply_text("❌ Please reply to a user to unmute them!")
        return

    target_user = message.reply_to_message.from_user
    mention = target_user.mention

    if target_user.id in muted_users:
        muted_users.remove(target_user.id)
        save_data()

        await message.reply_text(f"✅ {mention} has been unmuted!")

    else:
        await message.reply_text(f"❌ {target_user.first_name} is not muted!")

#=============== MUTELIST COMMAND ================
@app.on_message(filters.command("mutelist", prefixes=[".", "/"]) & filters.group)
async def mutelist_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not muted_users:
        await message.reply_text("📝 No users are muted currently!")
        return

    muted_list = "🔇 Muted Users List\n\n"

    for user_id in muted_users:
        try:
            user = await client.get_users(user_id)
            muted_list += f"• {user.first_name} ({user_id})\n"

        except:
            muted_list += f"• Unknown User ({user_id})\n"

    await message.reply_text(muted_list)

#=============== STICKER SPAM ================
@app.on_message(filters.command("sticker", prefixes=[".", "/"]) & filters.group)
async def sticker_spam_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    global sticker_spam_active

    parts = message.text.split()

    if len(parts) != 2:
        await message.reply_text("❌ Usage: .sticker <count>\nExample: .sticker 50")
        return

    try:
        count = int(parts[1])

        if count > 100:
            await message.reply_text("❌ Max limit is 100!")
            return

    except:
        await message.reply_text("❌ Please provide a valid number!")
        return

    if not custom_stickers:
        await message.reply_text("❌ No stickers added yet!\nUse .addsticker to add stickers.")
        return

    sticker_spam_active = True

    for i in range(count):
        if not sticker_spam_active:
            break

        sticker = random.choice(custom_stickers)

        await message.reply_sticker(sticker)

        await asyncio.sleep(0.1)

    sticker_spam_active = False

#=============== STOP RAID ================
@app.on_message(filters.command("stopraid", prefixes=[".", "/"]) & filters.group)
async def stop_raid_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    global sticker_spam_active

    sticker_spam_active = False

    await message.reply_text("🛑 Sticker raid stopped!")

#=============== SHAYARI COMMANDS ================
@app.on_message(filters.command("love"))
async def love_command(client, message: Message):

    if shayari_data["love"]:
        shayari = random.choice(shayari_data["love"])

        await message.reply_text(f"💕 Love Shayari 💕\n\n{shayari}")


@app.on_message(filters.command("sad"))
async def sad_command(client, message: Message):

    if shayari_data["sad"]:
        shayari = random.choice(shayari_data["sad"])

        await message.reply_text(f"🥀 Sad Shayari 🥀\n\n{shayari}")


@app.on_message(filters.command("shayari"))
async def general_shayari_command(client, message: Message):

    if shayari_data["general"]:
        shayari = random.choice(shayari_data["general"])

        await message.reply_text(f"✨ Shayari ✨\n\n{shayari}")


@app.on_message(filters.command("birthday"))
async def birthday_command(client, message: Message):

    if shayari_data["birthday"]:
        shayari = random.choice(shayari_data["birthday"])

        await message.reply_text(f"🎂 Birthday Shayari 🎂\n\n{shayari}")

#=============== ADD SHAYARI ================
@app.on_message(filters.command("addshayari"))
async def add_shayari_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can add shayari!")
        return

    parts = message.text.split(" ", 2)

    if len(parts) < 3:
        await message.reply_text("❌ Usage: .addshayari <love/sad/birthday/general> <shayari>")
        return

    category = parts[1].lower()
    shayari_text = parts[2]

    if category in shayari_data:
        shayari_data[category].append(shayari_text)

        save_data()

        await message.reply_text(f"✅ Shayari added to {category} category!")

    else:
        await message.reply_text("❌ Category must be: love, sad, birthday, or general")

#=============== SPAM COMMAND ================
@app.on_message(filters.command("spam", prefixes=[".", "/"]) & filters.group)
async def spam_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not message.reply_to_message:
        await message.reply_text("❌ Reply to a user and use: .spam <count> <message>")
        return

    parts = message.text.split(" ", 2)

    if len(parts) < 3:
        await message.reply_text("❌ Usage: .spam <count> <message>")
        return

    try:
        count = int(parts[1])

        if count > 100:
            await message.reply_text("❌ Max limit is 100!")
            return

    except:
        await message.reply_text("❌ Invalid number!")
        return

    global spam_active

    target = message.reply_to_message.from_user
    mention = target.mention
    custom_text = parts[2]

    spam_active = True

    for i in range(count):
        if not spam_active:
            break

        await message.reply_text(f"{mention} {custom_text}")

        await asyncio.sleep(0.1)

    spam_active = False

    await message.reply_text(f"✅ Spam completed: {count} times!")

#=============== STOP SPAM ================
@app.on_message(filters.command("stopspam", prefixes=[".", "/"]) & filters.group)
async def stop_spam_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    global spam_active

    spam_active = False

    await message.reply_text("🛑 Spam stopped!")

#=============== ADD STICKER ================
@app.on_message(filters.command("addsticker", prefixes=[".", "/"]) & filters.group)
async def add_sticker_command(client, message: Message):

    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can use this command!")
        return

    if not message.reply_to_message or not message.reply_to_message.sticker:
        await message.reply_text("❌ Please reply to a sticker to add it!")
        return

    sticker_id = message.reply_to_message.sticker.file_id

    custom_stickers.append(sticker_id)

    save_data()

    await message.reply_text(
        f"✅ Sticker added!\nTotal stickers: {len(custom_stickers)}"
    )

#=============== ADD SUDO ================
@app.on_message(filters.command("addsudo", prefixes=[".", "/"]) & filters.group)
async def add_sudo_command(client, message: Message):

    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add sudo users!")
        return

    user_id = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id

    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])

        except:
            await message.reply_text("❌ Invalid user ID!")
            return

    if user_id:
        sudo_users.add(user_id)

        save_data()

        user = await client.get_users(user_id)

        await message.reply_text(f"✅ {user.first_name} added as sudo user!")

    else:
        await message.reply_text("❌ Reply to a user or provide user ID!")

#=============== REMOVE SUDO ================
@app.on_message(filters.command("removesudo", prefixes=[".", "/"]) & filters.group)
async def remove_sudo_command(client, message: Message):

    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can remove sudo users!")
        return

    user_id = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id

    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])

        except:
            await message.reply_text("❌ Invalid user ID!")
            return

    if user_id and user_id in sudo_users and user_id != OWNER_ID:
        sudo_users.remove(user_id)

        save_data()

        user = await client.get_users(user_id)

        await message.reply_text(
            f"✅ {user.first_name} removed from sudo users!"
        )

    else:
        await message.reply_text(
            "❌ User not found in sudo list or cannot remove owner!"
        )

#=============== SUDO LIST ================
@app.on_message(filters.command("sudolist", prefixes=[".", "/"]) & filters.group)
async def sudo_list_command(client, message: Message):

    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not sudo_users:
        await message.reply_text("📝 No sudo users found!")
        return

    sudo_list = "👑 Sudo Users List\n\n"

    for user_id in sudo_users:
        try:
            user = await client.get_users(user_id)

            sudo_list += f"• {user.first_name}\n ┗ ID: {user_id}\n"

        except:
            sudo_list += f"• Unknown User\n ┗ ID: {user_id}\n"

    await message.reply_text(sudo_list)

#=============== MESSAGE HANDLER ================
@app.on_message(filters.group)
async def message_handler(client, message: Message):

    try:
        if not message.from_user:
            return

        log_text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
        log_text += f"User: {message.from_user.first_name} [{message.from_user.id}] | "
        log_text += f"Group: {message.chat.title} | "

        if message.text:
            log_text += f"Text: {message.text[:100]}"

        elif message.sticker:
            log_text += "Sticker sent"

        print(log_text)

    except:
        pass

    if not message.from_user:
        return

    user_id = message.from_user.id

    # OWNER PROTECTION
    if user_id == OWNER_ID:
        return

    # SUDO PROTECTION
    if user_id in sudo_users:
        return

    # DELETE MUTED USER MESSAGE
    if user_id in muted_users:
        try:
            await message.delete()

        except:
            pass

#=============== MAIN ================
def main():

    load_data()
    init_shayari()

    if OWNER_ID not in sudo_users:
        sudo_users.add(OWNER_ID)
        save_data()

    print("🚀 Bot Started Successfully!")
    print("✅ All features loaded!")
    print("📝 Check logs for group messages")
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"📊 Sudo Users: {len(sudo_users)}")
    print(f"💫 Custom Lines Loaded: {len(CUSTOM_LINES)}")

    app.run()


if __name__ == "__main__":
    main()
