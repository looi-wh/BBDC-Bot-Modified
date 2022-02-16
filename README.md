# BBDC-Bot-Modified
a modified script based on https://github.com/rohit0718/BBDC-bot.
the original script was not made to run indifinitely, so i added my own codes into it

# Original script features
- auto logs into the bbdc webpage
- selects everything for month, session and day
- and books every slots for you
- only run once per try
- this script did alot of the basics. if it didnt exists, this modification would not exists

# Added features due to my modification
- selects user-specified month, session and day
- auto retry failed attempts
- random delays between each attempts [to prevent hammering on the server]
- auto restart script when an unexpected error occurs
- added more verbose
- minor adjustments and error detection
- little bit of noob proofing
- [new] no longer requires webdriver to be downloaded manually
- [new] additional anti anti bot features


# Requirements
- python3
- python modules "selenium" and "webdriver_manager"
- google chrome

# Editing the script
- edit the script with your favourite editor
- find the following section and edit it.
```
username = 'insert_username'
password = 'insert_password'
```
- chromedriver_location must specify the file itself. simply stating the directory wont work
- edit the additional variables to select which slots to book
- it is a list variable, meaning you can always enter more than 1 slots at once

# Running it
simply run
```
python3 bbdc_bot.py
```
