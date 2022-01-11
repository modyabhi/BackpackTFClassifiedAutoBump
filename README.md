# BackpackTFClassifiedAutoBump

A python script to automatically bump your backpackTF classified trades every 45-50 minutes without the need to be a premium member. It also includes a small GUI for auth through the backpack steam login [credit to Justin Liang script](http://justin-liang.com/personal_projects/steam_automation_script.pdf).

## Dependencies

* Python 3.6 or higher
* alive_bar
* tkinter
* selenium 
* [chromedriver](https://chromedriver.chromium.org/downloads) tested on ChromeDriver 97.0.4692.71
* steam auth code (keep it handy from your mobile authentication)
* your steamID64 - https://steamid.io/

**Note: You will only need to login in once when you run the program, if you close the automated browser or exit the application you will need to reauth again**

## Getting started

Assuming you have python installed, lets start by installing depedencies

```python
pip install selenium
pip install aliver_bar
pip install tk
```

* create a new folder
* download chromedriver
* download the entire code from this repo
* place both chromedrive & code in the same folder

## Running

Open up a terminal in the folder where you've saved the code and run the below command:

`python backpack_relist_script.py`

Use your steam credentials and your steam guard code to launch the authentication process. 

![logo]
[logo]:https://imgur.com/EmRzlGe

### Disclaimer

I take no responsibility if you get banned from backpack.tf or incur any form of loss due to running this script. Please visit backpack.tf TOS to ensure you are not in violation.
This project is for educational purposes only. Backpack.tf is funded through donations and provides majority of their services for free. Support them if you wish to have a more automated way of bumping your trades.
