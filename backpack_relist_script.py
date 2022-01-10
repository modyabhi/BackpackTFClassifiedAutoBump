
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
        tk.Label(self.master, text="Steam Username").grid(column=0,row=0)
        tk.Label(self.master, text="Steam Password").grid(column=0,row=1)
        tk.Label(self.master, text ="SteamID64").grid(column=0,row=2)
        tk.Label(self.master, text="Steam Guard").grid(column=0,row=3)
        tk.Label(self.master, text="* required fields",fg = "red",justify = 'center').grid(column=1,row=4)

        for i in range(4):
            tk.Label(self.master, text="*",fg= "red").grid(column=1,row=i)

        #create vars to keep track of
        self.steamUser_var = tk.StringVar()
        self.steamPass_var = tk.StringVar()
        self.steamID64_var = tk.StringVar()
        self.steamGuard_var = tk.StringVar()

         # entry boxes for each label
        self.steamUserW = tk.Entry(self.master)
        self.steamPassW = tk.Entry(self.master, show="*")
        self.steamID64W = tk.Entry(self.master)
        self.steamGuardW = tk.Entry(self.master, show="*")
        self.submit = tk.Button(self.master, text="Submit", command=self.validate)
    
        # bind the ENTER key to callback function
        self.steamGuardW.bind("<Return>", self.assign)
        self.steamGuardW.bind("<KP_Enter>", self.assign)

    # space out the widgets
        self.steamUserW.grid(row=0, column=2)
        self.steamPassW.grid(row=1, column=2)
        self.steamID64W.grid(row=2, column=2)
        self.steamGuardW.grid(row=3, column=2)
        self.submit.grid(row=5, column=1)

     # grabs the values in the entry boxes and assigns them to variable
     def assign(self, *args):

        self.steamUser = self.steamUserW.get()
        self.steamPass = self.steamPassW.get()
        self.steamGuard = self.steamGuardW.get()
        self.steamID64 = self.steamID64W.get()
        self.close()

     # validates the entry boxes
     def validate(self, *args):
         if self.steamUser_var.get() and self.steamPass_var.get() and self.steamGuard_var.get() and self.steamID64_var.get():
            self.submit.config(state = "normal", command = self.assign)
            self.assign
         else:
            self.submit.config(state = "disabled")

     # closes GUI window
     def close(self):
        self.master.destroy()

root = tk.Tk()
userGui = gui(root)
root.wm_iconbitmap(r'2363211-game-gaming-play-steam-valve_85503.ico')
root.wm_title('Login')
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
profile_url = "https://backpack.tf/u/" + steamID64

while True:
    driver.get(profile_url)
    driver.implicitly_wait(10)
    actionChains = ActionChains(driver)
    elements = driver.find_elements(By.CSS_SELECTOR,"a.btn.btn-xs.btn-bottom.btn-default.listing-relist.listing-bump")
    try:
        for element in elements:
            actionChains.context_click(element).perform()
            time.sleep(5)
    except:
        print("No relist items found")
        print("going to sleep")
    driver.refresh()

    with alive_bar(54000) as bar:
        for i in range(54000):
            time.sleep(0.05)
            bar()
