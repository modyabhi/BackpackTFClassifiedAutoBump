# BackpackTFClassifiedAutoBump
 
A python script to automatically bump your backpackTF classified trades every 45-50 minutes. It also includes a small GUI for auth through the backpack steam login [credit to Justin Liang script](http://justin-liang.com/personal_projects/steam_automation_script.pdf).

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

create a folder and place the [backpack_relist_script.py](https://github.com/modyabhi/BackpackTFClassifiedAutoBump/blob/main/backpack_relist_script.py) into the folder, download the chromedriver and place it in the same folder 

## Running

run the script from your terminal, it's an infinite loop until you close or break the loop.