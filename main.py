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
global mixingTeam
mixingTeam = False
global voting 
voting = False

helpEmb = discord.Embed(title = 'Commands:' , description = '**!champ** - To get a random champion\n**!counter champion**- To get the counter list of a champion\n**!rteam** - To make a team and then get a random champ and lane each\n**!drank player** - To get the rank of a player(replace player with summonerName)\n**!mix** - To mix players into two teams \n**!vote a, b, c...** - To make a poll where everyone can vote only once(replace a, b and c with what ever you want, the limit is 9 items).')
helpEmb.set_thumbnail(url= 'https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help-760x400.jpg')
helpEmb.color = discord.Color.blue()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.lower()    
    global sentMsg
    #sends a random champion
    if message.author == client.user:
        pass
    elif (msg.startswith('!champ')):
        await message.channel.send(randomizer.randomChamp())
    
    #sends a list of counters
    elif (msg.startswith('!counter')):
        champ = msg.removeprefix('!counter').strip()
        for champion in  getCounterList(champ):
            await message.channel.send(champion)

    #Makes an embed for your team with random champs and roles
    elif msg.startswith('!rteam'):
        randomizer.reset()
        randomizer.addPlayer(message.author.display_name)
        sentMsg = await message.channel.send(embed = randomizer.getTeamEmb())
        await sentMsg.add_reaction('✋')
        await sentMsg.add_reaction('▶️')
        await sentMsg.add_reaction('🚪')
    
    #Mixes up players in two teams
    elif msg.startswith('!mix'):
        randomizer.reset()
        randomizer.addPlayer(message.author.display_name)
        randomizer.mixEmb()
        sentMsg = await message.channel.send(embed = randomizer.getTeamEmb())
        await sentMsg.add_reaction('✋')
        await sentMsg.add_reaction('▶️')
        await sentMsg.add_reaction('🚪')
        global mixingTeam
        mixingTeam = True
    
    #Makes a poll
    elif msg.startswith('!vote'):
        randomizer.reset()
        votingItems = msg.removeprefix('!vote').strip().split(',')
        lenVI = len(votingItems)
        sentMsg = await message.channel.send(embed = randomizer.makePoll(votingItems))
        if lenVI == 1:
            await sentMsg.add_reaction('👍')
        else:
            for i in range(0, len(votingItems)):
                await sentMsg.add_reaction("%s\u20e3"%str(i+1))
        await sentMsg.add_reaction('🛑')
        global voting
        voting = True

    #Finds a summoner and send his rank to the chat
    elif msg.startswith('!drank'):
        summoner = msg.replace('!drank', '').strip()
        await message.channel.send('%s\'s rank'%summoner)
        for rank in getSummoner(summoner):
            await message.channel.send(rank)
    #Tells you all the commands
    elif msg.startswith('!help') or msg.startswith('!h'):
        await message.channel.send(embed = helpEmb)

@client.event
async def on_reaction_add(reaction, user):
    username = user.display_name
    if user != client.user:
        await reaction.remove(user)
        if reaction.emoji == '✋' and username not in randomizer.getPlayers():
            randomizer.addPlayer(username)
            await sentMsg.edit(embed = randomizer.getTeamEmb())

        elif reaction.emoji == '🚪' and username in randomizer.getPlayers():
            randomizer.removePlayer(user)
            await sentMsg.edit(embed = randomizer.getTeamEmb())

        elif reaction.emoji == '▶️' and len(randomizer.getPlayers()) >= 1:
            await reaction.message.delete()
            if mixingTeam == True and len(randomizer.getPlayers()) > 1:
                await reaction.message.channel.send(embed = randomizer.mixPlayers())
            else:
                for embed in randomizer.makeTeam():
                    await reaction.message.channel.send(embed = embed)
        elif reaction.emoji == '🛑':
            await reaction.message.delete()
            randomizer.reset()

        elif voting == True and reaction.emoji != '✋'  and username not in randomizer.getPlayers():
            randomizer.addPlayer(username)
            if reaction.emoji == '👍':
                randomizer.addVote(1)
            else:
                randomizer.addVote(reaction.emoji[0])
            await sentMsg.edit(embed = randomizer.refreshCount())



client.run(token)

