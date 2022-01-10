
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
# class for gui window to get user and pass
class gui:
     def __init__(self, master):
        self.master = master

         # labels for each entry
        tk.Label(self.master, text="Steam Username").grid(row=0)
        tk.Label(self.master, text="Steam Password").grid(row=1)
        tk.Label(self.master, text="Steam Guard").grid(row=2)

         # button widget
        self.steamUserW = tk.Entry(self.master)
        self.steamPassW = tk.Entry(self.master, show="*")
        self.steamGuard = tk.Entry(self.master, show="*")
        self.submit = tk.Button(self.master, text="Submit", command=self.assign)
        # bind the ENTER key to callback function
        #self.emailPassW.bind("<Return>", self.assign)
        #self.emailPassW.bind("<KP_Enter>", self.assign)
        # space out the widgets
        self.steamUserW.grid(row=0, column=1)
        self.steamPassW.grid(row=1, column=1)
        self.steamGuard.grid(row=2, column=1)
        self.submit.grid(row=3, column=1)

     # grabs the values in the entry boxes and assigns them to variable
     def assign(self, *args):
        self.steamUser = self.steamUserW.get()
        self.steamPass = self.steamPassW.get()
        self.steamGuard = self.steamGuard.get()
        self.close()

     # closes GUI window
     def close(self):
        self.master.destroy()

root = tk.Tk()
userGui = gui(root)
root.mainloop()
steamUser = userGui.steamUser
steamPass = userGui.steamPass
steamGuard = userGui.steamGuard

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

while True:
    driver.get("https://backpack.tf/u/76561198060059269")
    driver.implicitly_wait(10)
    actionChains = ActionChains(driver)
    elements = driver.find_elements(By.CSS_SELECTOR,"a.btn.btn-xs.btn-bottom.btn-default.listing-relist.listing-bump")
    try:
        for element in elements:
            actionChains.context_click(element).perform()
            driver.implicitly_wait(5)
    except:
        print("No relist items found")
        print("going to sleep")
    driver.refresh()

    with alive_bar(54000) as bar:
        for i in range(54000):
            time.sleep(0.05)
            bar()
