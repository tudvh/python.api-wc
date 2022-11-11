from lxml import html
import requests, json

def getAll():
    page = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
    tree = html.fromstring(page.content)

    list_group = {}

    for i in range(7, 13):
        thtml = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[{}]'.format(i))

        # lay ten group
        ten_group = thtml[0].xpath('preceding-sibling::h3//text()')[-1]

        # lay ten doi
        list_ten_doi = thtml[0].xpath('.//tr[position()>1]/th//a//text()')
        
        # them vao list
        list_group.update({ten_group : list_ten_doi})

    return list_group