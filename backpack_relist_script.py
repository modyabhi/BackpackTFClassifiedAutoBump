
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from alive_progress import alive_bar
import tkinter as tk
from tk_gui import gui

root = tk.Tk()
userGui = gui(root)
root.mainloop()

try:
    steamUser = userGui.steamUser
    steamPass = userGui.steamPass
    steamGuard = userGui.steamGuard
    steamID64 = userGui.steamID64
except:
    print("No inputs found")
    exit()

# open up log-in screen
chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://backpack.tf/login")


# enter username and password and mobile auth
username = driver.find_element(By.ID,"steamAccountName")
username.send_keys(steamUser)
time.sleep(1)
password = driver.find_element(By.ID,"steamPassword")
time.sleep(1)
password.send_keys(steamPass, Keys.TAB, Keys.ENTER)
time.sleep(1)
auth = driver.find_element(By.ID,"twofactorcode_entry")
auth.send_keys(steamGuard)
time.sleep(1)
auth.send_keys(Keys.ENTER)

driver.implicitly_wait(10)

try:
    sign_in = driver.find_element(By.ID,"imageLogin")
    sign_in.send_keys(Keys.ENTER)
except:
    print("Signing in was not required")

time.sleep(5)

#infinite loop to check every 2700 seconds for items to bump
actionChains = ActionChains(driver)


while True:
    driver.implicitly_wait(10)
    x=1
    i=1
    while x>0:
        trade_url="https://backpack.tf/classifieds?page={}&steamid={}".format(i,steamID64)
        driver.get(trade_url)
        time.slee(5)
        elements = driver.find_elements(By.CSS_SELECTOR,"a.btn.btn-xs.btn-bottom.btn-default.listing-relist.listing-bump")
        x = len(elements)
        print("{} pages of listings".format(i))
        print("{} items to bump".format(x))
        time.sleep(1)
        for element in elements:
            actionChains.context_click(element).perform()
            time.sleep(5)
        i+=1

    driver.get("https://backpack.tf/classifieds?page=i&steamid={}".format(steamID64))
    print("Relisting complete")
    print("Sleeping for 2700 seconds")

    with alive_bar(54000) as bar:
        for i in range(54000):
            time.sleep(0.05)
            bar()
