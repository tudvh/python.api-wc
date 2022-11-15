from lxml import html
import requests
from module.xu_li import lam_net_anh
from module import match


class team_class(object):
    # constructor
    def __init__(self, link_html):
        self.__link_html = link_html

    # method
    def get_name(self):
        name = self.__link_html[0].xpath('./th//a//text()')[0]
        return name

    def get_link_image(self):
        link_image = self.__link_html[0].xpath('./th//img/@src')[0]
        link_image = lam_net_anh(link_image, '5000')
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

    # export
    def get_all(self):
        self.name = self.get_name()
        self.image = self.get_link_image()
        self.position = self.get_position()
        self.played = self.get_played()
        self.won = self.get_won()
        self.drawn = self.get_drawn()
        self.lost = self.get_lost()
        self.goal_difference = self.get_goal_difference()
        self.points = self.get_points()


def get_all():
    page = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
    tree = html.fromstring(page.content)

    list_group = {}

    for i in range(7, 15):
        thtml = tree.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[{}]'.format(i))

        # lay ten group
        name_group = thtml[0].xpath(
            'preceding-sibling::h3/span[1]//text()')[-1]

        # lay doi
        list_team = []
        for j in range(2, 6):
            team = team_class(thtml[0].xpath('.//tr[{}]'.format(j)))
            team.get_all()
            team.__dict__.pop('_team_class__link_html')
            list_team.append(team.__dict__)

        # them vao list
        list_group[name_group] = list_team

    return list_group


def get_by_group(id_group):

    list_group = {
        'status':'Error',
        'message': 'Group is not correct'
    }

    if(not match.checkStage("Group_stage", id_group)):
        return list_group

    page = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
    tree = html.fromstring(page.content)

    h3html = tree.xpath('//h3/span[@id="{}"]'.format(id_group))[0]
    table = h3html.xpath('../following-sibling::table[1]')

    # lay ten group
    name_group = h3html.text

    list_group = {
        'status' : 'success',
        'data' : {}
    }

    # lay doi
    list_team = []
    for j in range(2, 6):
        team = team_class(table[0].xpath('.//tr[{}]'.format(j)))
        team.get_all()
        team.__dict__.pop('_team_class__link_html')
        list_team.append(team.__dict__)

    # them vao list
    list_group['data'][name_group] = list_team

    return list_group
