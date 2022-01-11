import tkinter as tk
# class for gui window to get user and pass
class gui:
     def __init__(self, master):
        self.master = master
        self.master.title("Backpack.tf Relist Script")
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.master.iconbitmap(r'2363211-game-gaming-play-steam-valve_85503.ico')

        Labels = ["Steam Username:", "Steam Password:", "SteamID64:", "Steam Guard:"]
        for idx in range(len(Labels)):
           tk.Label(self.master, text=Labels[idx],anchor='e',width=15).grid(column=0,row=idx)

        #create vars to keep track of
        self.steamUser_var = tk.StringVar()
        self.steamPass_var = tk.StringVar()
        self.steamID64_var = tk.StringVar()
        self.steamGuard_var = tk.StringVar()

         # entry boxes for each label
        self.steamUserW = tk.Entry(self.master,textvariable=self.steamUser_var)
        self.steamPassW = tk.Entry(self.master, show="*",textvariable=self.steamPass_var)
        self.steamID64W = tk.Entry(self.master,textvariable=self.steamID64_var)
        self.steamGuardW = tk.Entry(self.master, show="*",textvariable=self.steamGuard_var)
        self.submit = tk.Button(self.master, text="Submit", command=self.validate)

         #validate variables
        self.steamUser_var.trace('w',self.validate)
        self.steamPass_var.trace('w',self.validate)
        self.steamID64_var.trace('w',self.validate)
        self.steamGuard_var.trace('w',self.validate)

        # bind the ENTER key to callback function
        self.steamGuardW.bind("<Return>", self.assign)
        self.steamGuardW.bind("<KP_Enter>", self.assign)

    # space out the widgets
        self.steamUserW.grid(row=0, column=1)
        self.steamPassW.grid(row=1, column=1)
        self.steamID64W.grid(row=2, column=1)
        self.steamGuardW.grid(row=3, column=1)
        self.submit.grid(row=5, columnspan=2)
        tk.Label(self.master, text="* required fields",fg='red').grid(row=4,columnspan=2)
        for i in range(4):
         tk.Label(self.master, text="*",fg= "red",anchor = 'w',width=5).grid(column=2,row=i)

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
         else:
            self.submit.config(state = "disabled")

     # closes GUI window
     def close(self):
        self.master.destroy()