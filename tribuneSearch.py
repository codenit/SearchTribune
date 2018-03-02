from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def autoTribune():

    baseUrl = "http://www.tribuneindia.com/"

    drivers = webdriver.Chrome()
    drivers.maximize_window()
    drivers.get(baseUrl)
    drivers.implicitly_wait(10)

    theDate = drivers.find_element(By.ID, "ctl00_header1_timespan").text
    print('News for: ','\033[4m',theDate,'\033[0m','\n')

    flashNews = drivers.find_elements(By.XPATH,"//div[@id='ctl00_topmenubar1_newsflash']//li")
    for n in flashNews:
        print("News Flash: ", n.text,'\n')
        break

    headlines = drivers.find_element(By.XPATH,"//div[@id='ctl00_ContentPlaceHolder1_toplead_news1_dvtopleadmain']//a" ).text
    synopsis = drivers.find_element(By.ID, "synop").text
    print("Today's main Headline is: ",'\n','\t','\033[1m',headlines,'\033[0m','\n')
    print("Synopsis: ",'\n','\t', '\033[36m',synopsis,'\033[0m','\n')

    try:
        response = input("Want to read full story?(y/n) ").lower(),'\n'

        if response == 'y':
            drivers.find_element(By.ID, "plusicon").click()

            fullArticle = drivers.find_element(By.ID, "fullart").text
            print('\033[96m',fullArticle,'\033[0m','\n')
            print('*'*60,'\n')
    except:
        pass

    try:
        bResponse = input("To read bulletins press(y/n): ").lower()
        if bResponse == 'y':

            bulletins = drivers.find_elements(By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_toplead_news1_dvtopleadbottom']//h2/a")
            summary = drivers.find_elements(By.XPATH, "//div[@id='ctl00_ContentPlaceHolder1_toplead_news1_dvtopleadbottom']//p")

            for b,s in zip(bulletins,summary):

                print('\033[1m',b.text,'\033[0m','\n', '\033[36m', s.text,'\033[0m','\n')
    except:
        pass

autoTribune()
