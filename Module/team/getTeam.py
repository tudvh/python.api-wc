from lxml import html
import requests
from copy import deepcopy

class team_class:
    __teamOBJ = {}
    #constructor
    def __init__(self, link_html):
        self.__link_html = link_html
    #method
    def get_name(self):
        name = self.__link_html[0].xpath('./th//a//text()')[0]
        return name
    def get_link_image(self):
        link_image = self.__link_html[0].xpath('./th//img/@src')[0]
        return link_image
    def get_position(self):
        position = self.__link_html[0].xpath('./td[1]//text()')[0]
        return position[0]
    def get_played(self):
        played = self.__link_html[0].xpath('./td[2]//text()')[0]
        return played[0]
    def get_won(self):
        won = self.__link_html[0].xpath('./td[3]//text()')[0]
        return won[0]
    def get_drawn(self):
        drawn = self.__link_html[0].xpath('./td[4]//text()')[0]
        return drawn[0]
    def get_lost(self):
        lost = self.__link_html[0].xpath('./td[5]//text()')[0]
        return lost[0]
    def get_goal_difference(self):
        goal_difference = self.__link_html[0].xpath('./td[6]//text()')[0]
        return goal_difference[0]
    def get_points(self):
        points = self.__link_html[0].xpath('./td[9]//text()')[0]
        return points[0]
    #export
    def xuat_mang(self):
        self.__teamOBJ['name'] = self.get_name()
        self.__teamOBJ['image'] = self.get_link_image()
        self.__teamOBJ['position'] = self.get_position()
        self.__teamOBJ['played'] = self.get_played()
        self.__teamOBJ['won'] = self.get_won()
        self.__teamOBJ['drawn'] = self.get_drawn()
        self.__teamOBJ['lost'] = self.get_lost()
        self.__teamOBJ['goal difference'] = self.get_goal_difference()
        self.__teamOBJ['points'] = self.get_points()
        return self.__teamOBJ


def getAll():
    page = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
    tree = html.fromstring(page.content)

    list_group = {}

    for i in range(7, 15):
        thtml = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[{}]'.format(i))

        # lay ten group
        name_group = thtml[0].xpath('preceding-sibling::h3/span[1]//text()')[-1]

        # lay doi
        list_team = []
        for j in range(2, 6):
            team_html = thtml[0].xpath('.//tr[{}]'.format(j))
            team = team_class(team_html)
            list_team.append(team.xuat_mang().copy())
        
        # them vao list
        list_group[name_group] = list_team

    return list_group

print(getAll())