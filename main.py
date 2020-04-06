#!/usr/bin/python3


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



br=webdriver.Safari(executable_path='/usr/bin/safaridriver')
br.get("http://online.agah.com/")
sleep(2)

user=br.find_element_by_id("username")

user.click()
user.send_keys(“[user]”)

psw=br.find_element_by_id("password")
psw.click()
psw.send_keys(“[Password]”)
#____________________________> Captcha
import os
os.system('rm 1.txt')
while 1:
    if os.path.exists('1.txt'):
        break
    else:
        sleep(1)

o=open('1.txt','r')
oo=o.readline()
o.close()
os.system('rm 1.txt')
cph=oo.split('\n')[0]

#__________________________
wcph=br.find_element_by_id("captcha")
wcph.click()
wcph.send_keys(cph)

#____________________________> LogIn Submit:
btn=br.find_element_by_id("submit-btn")
btn.click()



#_________________________> Sale Operation
os.system('rm 2.txt')
while 1:
    sleep(1)
    if os.path.exists('2.txt'):
        break
def sale():
    try:
        kh=br.find_element_by_xpath("//div[@id='mwoPanels']/div/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div/div/div/div/div/i")
        kh.click()
    except:
        print('\nKharid Error')
    #------------------------> Select Price
    #_______________________________________________________________________________________________________
    q=1
    while 1:
        q+=1
        if q ==10:
            break
        try:
            pr = br.find_element_by_xpath("(//input[@type='text'])[9]")
            pr.click()
            pr.send_keys('10000')
            break
        except:
            print('\nPrice Error')

    #-------------------------> Value
    try:
        vl=br.find_element_by_xpath("//div[2]/div/p/span")
        vl.click()
    except:
        print('\nVolume Error')
    #--------------------------> Last Order to Buy
    #sleep(5)
    try:
        buy=br.find_element_by_xpath("//button[contains(.,' خرید')]")
        buy.click()
        info1=br.find_element_by_xpath("//div[@id='toast-container']/div/div/p")
        info1.click()
        info2=br.find_element_by_xpath("//div[@id='toast-container']/div[2]/div")
        info2.click()
    except:
        print('\nBTN Click Error')

q=1
while 1:
    sale()
    q+=1
    if q>=200:
        break




#sleep(10)
br.close()
