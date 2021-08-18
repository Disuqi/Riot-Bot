import discord
import os
import random
from dotenv import load_dotenv
from methods import *
from discord import *
from randomizer import *

load_dotenv()
intents = discord.Intents.all()
client = discord.Client(intents = intents)
token = os.getenv('TOKEN')


randomizer = Randomizer()
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()    
    global teamMsg
    #sends a random champion
    if (msg.startswith('!champ')):
        hisChamp = randomizer.randomChamp()
        if (hisChamp == 'Wukong'):
            hisChamp = 'MonkeyKing'
        await message.channel.send('https://static.u.gg/assets/lol/riot_static/11.16.1/img/champion/'+hisChamp+'.png')
    
    #sends a list of counters
    elif (msg.startswith('!counter')):
        champ = msg.replace('!counter', '').strip()
        for champion in  getCounterList(champ):
            await message.channel.send(champion)

    #Makes an embed for your team with random champs and roles
    elif msg.startswith('!team random'):
        randomizer.reset()
        randomizer.addPlayer(message.author.display_name)
        teamMsg = await message.channel.send(embed = randomizer.getTeamEmb())
        await teamMsg.add_reaction('✋')
        await teamMsg.add_reaction('▶️')
        await teamMsg.add_reaction('🚪')
    
    #Mixes up players in two teams
    elif msg.startswith('!mix'):
        randomizer.reset()
        randomizer.addPlayer(message.author.display_name)
        teamMsg = await message.channel.send(embed = randomizer.getTeamEmb())
        await teamMsg.add_reaction('✋')
        await teamMsg.add_reaction('▶️')
        await teamMsg.add_reaction('🚪')
        global mixingTeam
        mixingTeam = True
    #Tells you all the commands
    elif msg.startswith('!help'):
        await message.channel.send('!champ - To get a random champion\n!counter champion- To get the counter list of a champion\n!team random - To make a team and then get a random champ and lane each\n!drank player- To get the rank of a player')

@client.event
async def on_reaction_add(reaction, user):
    username = user.display_name
    if user != client.user:
        await reaction.remove(user)
        if reaction.emoji == '✋' and username not in randomizer.getPlayers():
            randomizer.addPlayer(username)
            await teamMsg.edit(embed = randomizer.getTeamEmb())

        elif reaction.emoji == '🚪' and username in randomizer.getPlayers():
            randomizer.removePlayer(user)
            await teamMsg.edit(embed = randomizer.getTeamEmb())

        elif reaction.emoji == '▶️' and len(randomizer.getPlayers()) >= 1:
            await reaction.message.delete()
            if mixingTeam == True:
                await reaction.message.channel.send(embed = randomizer.mixPlayers())
            else:
                for embed in randomizer.makeTeam():
                    await reaction.message.channel.send(embed = embed)


client.run(token)

