import requests
from lxml import html

#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
#sys.path.insert(1, 'python.api-wc/module')
from module import xu_li



class Team(object):
    def __init__(self):
        self.icon=None
        self.name=None
        
    def setName(self,name):
        self.name=name
    def setIcon(self,icon):
        self.icon=icon   

class Goal(object):
    def __init__(self):
        self.player=None
        self.timeG=None
        self.type=None
    def setPlayer(self,player):
        self.player=player
    def setTimeG(self,timeG):
        self.timeG=timeG
    def setType(self,type):
        self.type=type

class Match(object):
    def __init__(self):
        self.scorePen=None
    def setDate(self,date):
        self.date = date
    def setTime(self,time):
        self.time = time
    def setScore(self,score):
        self.score=score
    def setHomeT(self,homeT:object):
        self.homeT=homeT
    def setHomeG(self,homeG:list):
        self.homeG=homeG
    def setAwayT(self,awayT:object):
        self.awayT=awayT
    def setAwatG(self,awayG:list):
        self.awayG=awayG
    def setScorePen(self,scorePen):
        self.scorePen=scorePen
    def setStage(self,stage):
        self.stage=stage




def getAllMatch(todo):
    listMatch=[]
    url = "https://en.wikipedia.org/wiki/2022_FIFA_World_Cup#Schedule"
    page = requests.get(url)
    document = html.fromstring(page.content)
    data = document.xpath(
        '//*[@class="footballbox"]')
    
    for line in data:
        m=Match()
        #Lấy ngày đấu
        date = line.xpath(
            './/span[@class="bday dtstart published updated"]//text()')
        #Lấy giờ đấu
        time = line.xpath('.//div[@class="ftime"]//text()')
        #Lấy múi giờ
        utc = line.xpath('.//div[@class="ftime"]//a[2]//text()')
        #Chuyển qua việt nam
        
        if(len(utc)==0):
            utc=[]
            utc.append('UTC+3')
               
        kq=str(xu_li.formatTime(date[0],time[0],utc[0])).split(' ')      
        m.setDate(kq[0])
        m.setTime(kq[1])
        #Lấy đôi nhà
        hTeam=Team()
        hometeam = line.xpath(
            './/th[@class="fhome"]//span//a//text()|.//th[@class="fhome"]//span//text()')  
        hTeam.setName(hometeam[0])
        iconhome = line.xpath(
            './/th[@class="fhome"]//span[@class="flagicon"]//img//@src')
        if(len(iconhome)!=0): 
            hTeam.setIcon(xu_li.lam_net_anh(iconhome[0],'500'))
        m.setHomeT(hTeam.__dict__)
        #Lấy tỉ số
        score = line.xpath('.//th[@class="fscore"]//a//text()')
        m.setScore(score[0])

        #Lấy đội khách
        aTeam=Team()
        awayteam = line.xpath(
            './/th[@class="faway"]//span//a//text()|.//th[@class="faway"]//span//text()')
        
        aTeam.setName(awayteam[len(awayteam)-1])
        iconaway = line.xpath(
            './/th[@class="faway"]//span[@class="flagicon"]//img//@src')
        if(len(iconaway)!=0):
            aTeam.setIcon(xu_li.lam_net_anh(iconaway[0],'500'))
        m.setAwayT(aTeam.__dict__)

        #Lấy bàn thắng home Team
        listHomeG=[]
        gHome=line.xpath('.//tbody//tr[2]//td[@class="fhgoal"]//li')
        #gHome=data[7].xpath('.//tbody//tr[2]//td[@class="fhgoal"]//li')
        
        for g in gHome:
            
            time = g.xpath('./span[@class="fb-goal"]/span/text()')
            i=1
            for x in time:
                if(not(")" in x or "(" in x)): 
                    goal = Goal()
                    player = g.xpath('./a/text()')
                    goal.setPlayer(player[0])
                    goal.setTimeG (x)
                    typegoal=g.xpath('./span[@class="fb-goal"]/span[{}]/a/text()'.format(i))
                    i=i+1
                    if(len(typegoal)):
                        goal.setType(typegoal[0])
                    listHomeG.append(goal.__dict__)
                 
            
        m.setHomeG(listHomeG)

        #Lấy bàn thắng đội khách
        listAwayG=[]
        gAway=line.xpath('.//tbody//tr[2]//td[@class="fagoal"]//li')

        for g in gAway:

            time = g.xpath('./span[@class="fb-goal"]/span/text()')

            for x in time:
                if(not(")" in x or "(" in x)):
                    goal = Goal()
                    player = g.xpath('./a/text()')
                    goal.setPlayer(player[0])
                    goal.setTimeG(x)
                    typegoal=g.xpath('./span[@class="fb-goal"]/span/a/text()')
                    if(len(typegoal)):
                        goal.setType(typegoal[0])
                    listAwayG.append(goal.__dict__)
        m.setAwatG(listAwayG)
        test=line.xpath('preceding-sibling::h3//span[@class="mw-headline"]//text()')[-1]
        m.setStage(test)
        listMatch.append(m.__dict__)

        #Láy tỉ số pen
        scorePen=line.xpath('.//tbody//tr[4]/th/text()')
        if(len(scorePen)!=0):
            m.setScorePen(scorePen[0])   
    
    return listMatch



print(getAllMatch(1)[0]['homeT']['name'])
