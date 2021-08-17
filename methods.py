from bs4 import BeautifulSoup
import requests

def getCounterList(champ):
    champName = champ[0].upper() + champ[1:]
    url = 'https://u.gg/lol/champions/%s/counter'%champ
    champList = []
    page = requests.get(url)
    htmlOfPage = BeautifulSoup(page.content, 'html.parser')
    try:
        counterList = htmlOfPage.find(class_='counters-list')
        champs = counterList.find_all(class_='counter-list-card')
        champList.append('Best picks VS %s'%champName)
        for champion in champs:
            champList.append(champion.find(class_='champion-name').text + ' - ' + champion.find(class_='win-rate').text )
    except AttributeError:
        if champName == 'Hmar' or champName == 'Khanzir' or champName == 'Haiwan' or champName == 'Calb' or champName == 'Db':
            champList.append('L\'unico %s qua sei tu'%champName)
        else:
            champList.append('Ma levati, chi vuoi trollare? %s non esiste!'%champName)
    return champList

  
def getSummoner(summoner):
    url = 'https://u.gg/lol/profile/euw1/%s/overview'%summoner
    page = requests.get(url)
    htmlOfPage = BeautifulSoup(page.content, 'html.parser')
    result = []
    try:
        ranks = htmlOfPage.find_all(class_='rank-tile')
        for rank in ranks:
            result.append(rank.find(class_='queue-type').text + ' - ' +  rank.find(class_='rank-text').text + '\n' + rank.find(class_='rank-wins').text)
    except AttributeError:
        if summoner == 'hmar' or summoner == 'khanzir' or summoner == 'haiwan' or summoner == 'calb' or summoner == 'db':
            result.append('L\'unico %s qua sei tu'%summoner)
        else:
            result.append('Ma levati, chi vuoi trollare? %s non esiste!'%summoner)
    return result


def getRunes(champion, role):
    url = 'https://u.gg/lol/champions/'+champion+'/build?role=' + role.lower()
    page = requests.get(url)
    htmlOfPage = BeautifulSoup(page.content, 'html.parser')
    runes = []
    pass
        
