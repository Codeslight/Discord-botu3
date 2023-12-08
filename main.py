import discord
from discord.ext import commands
from bot_mantik import *
import math
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
h_d_k={
    "Clouds":"Bulutlu",
    "Wind" : "Rüzgarlı",
    "Snow" : "Karlı",
    "Rain" :"Yağmurlu",
    "Sunny" : "Güneşli",
    "Mist" : "Sisli",
    "Clear" : "Açık hava"   
}
api_key = "ff4d0f71153fc14f03f0ef1410af08a9" 
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    

def hava(sehir):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data["weather"][0]["main"] in h_d_k:
        return h_d_k[data["weather"][0]["main"]]
    else:
        return data["weather"][0]["main"]


@bot.command()
async def hava_d(ctx,sehir):
    await ctx.send(hava(sehir))
  bot.run("Lütfen tokeninizi buraya giriniz.")
