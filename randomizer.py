from discord import *
import random
import discord

class Randomizer:
#Makes the first Embed for people to join the team
    champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Chogath", 'Corki', 'Darius', 'Diana', 'Dr. mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kaisa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Khazix", 'Kindred', 'Kled', "Kogmaw", 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "RekSai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Velkoz", 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
    roles = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']
    players = []
    ranTeamEmb = None
    laneColors = {
        'Top': discord.Colour.blue(),
        'Jungle': discord.Colour.teal(),
        'Mid': discord.Colour.dark_red(),
        'Bot': discord.Colour.orange(),
        'Support': discord.Colour.purple(), 
    }


    def __init__(self):
        self.ranTeamEmb = Embed(title = 'ALL RANDOM TEAM', description = '**Players**👇 \n', colour = discord.Colour.red())
        self.ranTeamEmb.add_field(name='Rules', value= '✋ to join the team \n▶️ to start making the team \n🚪 to leave before starting')
        self.ranTeamEmb.set_thumbnail(url = 'https://media.giphy.com/media/xUOxfjsW9fWPqEWouI/giphy.gif')

    #Refreshes the embed. Useful when someone joins or leaves       
    def refreshEmbed(self):
        playersList = str('\n'.join(self.players))
        self.ranTeamEmb.description = '**Players**👇 \n' + playersList


    def randomChamp(self):
        return random.choice(self.champions)

    def addPlayer(self, player):
        if len(self.players) < 5:
            self.players.append(player)
    
    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players
    
    def getTeamEmb(self):
        self.refreshEmbed()
        return self.ranTeamEmb

    def makeTeam(self):
        playersEmb = []
        for player in self.players:
            hisRole = random.choice(self.roles)
            hisChamp = random.choice(self.champions)
            hisColour = self.laneColors.get(hisRole)
            hisEmb = Embed(title = player, description = '**'+hisChamp+' - '+hisRole+'**', color = hisColour)
            hisEmb.set_thumbnail(url = 'https://static.u.gg/assets/lol/riot_static/11.16.1/img/champion/'+hisChamp+'.png')
            playersEmb.append(hisEmb)
            self.roles.remove(hisRole)
            self.champions.remove(hisChamp)
        return playersEmb

    def reset(self):
        self.champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Chogath", 'Corki', 'Darius', 'Diana', 'Dr. mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kaisa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Khazix", 'Kindred', 'Kled', "Kogmaw", 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "RekSai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'TahmKench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Velkoz", 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
        self.roles = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']
        self.players = []
        self.playersEmb = []