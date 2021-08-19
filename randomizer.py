from discord import *
import random
import discord

class Randomizer:
    #All champions/characters in league of legends and the link for their icons
    champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Chogath", 'Corki', 'Darius', 'Diana', 'Dr. mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kaisa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Khazix", 'Kindred', 'Kled', "Kogmaw", 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "RekSai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Velkoz", 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
    link = 'https://static.u.gg/assets/lol/riot_static/11.16.1/img/champion/%s.png'
    #All the roles in the game, useful for later
    roles = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']
    #All the people participating in whatever it is
    players = []
    #The Embed used for randomizing a team or separeting two teams, here is = to nothing but later it will be initialized properly
    ranTeamEmb = None
    #The embed for the poll
    pollEmb = None
    #Dictonaty just for the colours
    laneColors = {
        'Top': discord.Colour.blue(),
        'Jungle': discord.Colour.teal(),
        'Mid': discord.Colour.dark_red(),
        'Bot': discord.Colour.orange(),
        'Support': discord.Colour.purple(), 
    }
    #Disctonary for votes
    voteCounter = {}
    votingItems = []

    def __init__(self):
        self.ranTeamEmb = Embed(title = 'ALL RANDOM TEAM', description = '**Players**👇 \n', colour = discord.Colour.red())
        self.ranTeamEmb.add_field(name='Rules', value= '✋ to join the team \n▶️ to start making the team \n🚪 to leave before starting')
        self.ranTeamEmb.set_thumbnail(url = 'https://media.giphy.com/media/xUOxfjsW9fWPqEWouI/giphy.gif')
        self.pollEmb = Embed(description = 'Vote', colour = discord.Colour.random())
        
    #Refreshes the embed. Useful when someone joins or leaves       
    def refreshEmbed(self):
        playersList = str('\n'.join(self.players))
        self.ranTeamEmb.description = '**Players**👇 \n' + playersList


    def randomChamp(self):
        hisChamp = random.choice(self.champions)
        if (hisChamp == 'Wukong'):
            hisChamp = 'MonkeyKing'
        return self.link%hisChamp

    def addPlayer(self, player):
        self.players.append(player)
    
    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players
    
    def getTeamEmb(self):
        self.refreshEmbed()
        return self.ranTeamEmb

    def mixPlayers(self):
        teamOne = []
        teamTwo = []
        turn = True
        while len(self.players) != 0:
            player = random.choice(self.players)
            self.players.remove(player)
            if turn:
                teamOne.append(player)
                turn = False
            else:
                teamTwo.append(player)
                turn = True
        strTeamOne = '\n'.join(teamOne)
        strTeamTwo = '\n'.join(teamTwo)
        embed = Embed(title = 'Team 1', description = strTeamOne, colour = discord.Colour.red())
        embed.add_field(name= 'Team 2', value = strTeamTwo)
        return embed

    def makeTeam(self):
        while len(self.players) > 5:
            del self.players[-1]
        playersEmb = []
        for player in self.players:
            hisRole = random.choice(self.roles)
            hisChamp = random.choice(self.champions)
            hisColour = self.laneColors.get(hisRole)
            hisEmb = Embed(title = player, description = '**'+hisChamp+' - '+hisRole+'**', color = hisColour)
            if(hisChamp == 'Wukong'):
                hisChamp = 'MonkeyKing'
            hisEmb.set_thumbnail(url = self.link%hisChamp)
            playersEmb.append(hisEmb)
            self.roles.remove(hisRole)
            self.champions.remove(hisChamp)
        return playersEmb
    
    def makePoll(self, votingItems):
        self.pollEmb = Embed(description = '**Vote here**')
        for i in range(0, len(votingItems)):
            self.voteCounter[i] = 0
            item = votingItems[i].capitalize()
            self.pollEmb.insert_field_at(index = i, name=str(i+1) +'.'+item, value='**'+str(self.voteCounter.get(i))+ '**')
            self.votingItems.append(item)
        return self.pollEmb

    def refreshCount(self):
        for i in range(0, len(self.votingItems)):
            self.pollEmb.set_field_at(index = i,name = str(i+1) +'.'+self.votingItems[i], value ='**'+str(self.voteCounter.get(i))+ '**' )
        return self.pollEmb
    
    def addVote(self, number):
        i = int(number) - 1
        self.voteCounter[i] += 1

    
    def reset(self):
        self.voteCounter = {}
        self.votingItems = []
        self.champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Chogath", 'Corki', 'Darius', 'Diana', 'Dr. mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kaisa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Khazix", 'Kindred', 'Kled', "Kogmaw", 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "RekSai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Velkoz", 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
        self.roles = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']
        self.players = []
        self.playersEmb = []