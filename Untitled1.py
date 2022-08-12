# all libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas

for pages in range(1,15,1): # range(start page, Total number of page, Increment the sequence)
    driver = webdriver.Chrome("F:\python\justdial\chromedriver.exe") # add chrome dirver
    driver.get("URL/page-"+ str(pages) +"") #add page URL
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ul = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'rsl')))
    li = ul.find_elements(By.CLASS_NAME,'cntanr')
    def strings_to_num(argument): 
        #phone number 
        switcher = { 
            'dc': '+',
            'fe': '(',
            'hg': ')',
            'ba': '-',
            'acb': '0', 
            'yz': '1', 
            'wx': '2',
            'vu': '3',
            'ts': '4',
            'rq': '5',
            'po': '6',
            'nm': '7',
            'lk': '8',
            'ji': '9'
        } 
        return switcher.get(argument, "nothing")
    numbersList = []
    nameList = []
    data = []
    for lis in li:
        title = lis.find_element(By.CLASS_NAME,"store-name")
        toolTip = lis.find_element(By.CLASS_NAME,"morehvr")
        hov = ActionChains(driver).move_to_element(toolTip)
        txt = hov.perform()
        address = lis.find_element(By.CLASS_NAME,"cont_fl_addr")
        mobile = lis.find_elements(By.CLASS_NAME,"mobilesv")

        myList = []
        for j in range(len(mobile)):
            mystring = mobile[j].get_attribute('class').split("-")[1]
            myList.append(strings_to_num(mystring))
        data.append({"Title":title.text,"Address":address.text,"Phone":"".join(myList)})
        # print(data) Print data
        df = pandas.DataFrame(data)
        df.to_csv("abrasive-belt-rajkot.csv",mode='a') # append fields
    driver.close()