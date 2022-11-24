from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import datetime
from time import sleep


def check_exists_by_xpath(xpath, browser):
    data = 'khong co du lieu'
    try:
        data = browser.find_element('xpath', xpath).text
    except NoSuchElementException:
        return False
    return data


def lay_data():
    thoi_gian_chay = datetime.datetime.now()

    options = Options()
    options.add_argument('--window-size=700,700')
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.get("https://en.wikipedia.org/wiki/2022_FIFA_World_Cup")

    xp = '//*[@id="mw-content-text"]/div[1]/div[18]/table/tbody/tr[2]/td[3]/div/ul/li/a'

    d = browser.find_element('xpath', xp).text

    # while True:
    #     sleep(1)
    #     d = check_exists_by_xpath(xp, browser)
    #     if not d == False:
    #         break

    thoi_gian_kt = datetime.datetime.now()

    browser.close()

    list_a = []
    list_a.append(d)
    list_a.append(str(abs(thoi_gian_kt - thoi_gian_chay)))

    return list_a
