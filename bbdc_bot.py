from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # [modified by looi] for sleep function
import random # [modified by looi] for random function

# MODIFICATION NOTICE [inserted by looi]
# THIS script HAS BEEN MODIFIED BY LOOIWH FOR INFINITE LOOP
# IT WILL BASICALLY LOOP FOREVER UNTIL THE script FOUNDS A SLOT
# IF ONE OR MORE SLOTS ARE FOUND, THE script WILL QUICKLY BOOK IT AND STOP
# RESTART OR MODIFY THE script IF YOU WOULD LIKE TO BOOK MORE IN ONE RUN
# THIS script WILL NOT WORK IF CAPTCHA IS IMPLEMENTED!!
# script is also modified to provide a bit of noob-proofing
# attempts to restart the script will also be started after awhile
#
# script original github: https://github.com/rohit0718/BBDC-bot
#
# WARNING: to make it easier on the bbdc server and as an effort on
# preventing bbdc from noticing the hamering, there will be a random
# timer that will run between each search. it will run between 10 to
# 120 seconds randomly. dont be a bastard. 

print("[boot] modified script started")
print("[boot] script modified by looi")
print("[boot] this script has been modified for infinite loop")
print("[boot] please do not interact with the chrome browser")

# CHANGE THESE THREE VARIABLES [ORIGINAL script OWNER IDEA]
chromedriver_location = 'insert_chromedriver_location'
username = 'insert_nric'
password = 'insert_password'

# ADDITIONAL VARIABLES MADE BY LOOI
# CHANGE THESE VARIABLES FOR YOUR OWN LIKING
# follows original script intentions: 0 for 1st/Monday, 1 for 2nd/Tuesday
toBookMonths = [0, 1] # first two months
toBookSessions = [5] # slot 4 and 6
toBookDays = [0, 1, 2, 3, 4] # mondays to fridays


# checks if the required variables are unchanged
if username == 'insert_nric' or password == 'insert_password' or chromedriver_location == 'insert_chromedriver_location':
	print("[fatal] Please change the values in the script first before running it")
	exit()

def openPage(): # [modified by looi] everything is converted to a function here
	global browser, username, toBookMonths, toBookSessions, toBookDays, chromedriver_location
	browser = webdriver.Chrome(chromedriver_location)
	browser.get('https://info.bbdc.sg/members-login/')
	print("[preparation] website opened")
	v = 60
	print("[preparation] logging in as", username)
	idLogin = browser.find_element_by_id('txtNRIC')
	idLogin.send_keys(username)
	idLogin = browser.find_element_by_id('txtPassword')
	idLogin.send_keys(password)
	loginButton = browser.find_element_by_name('btnLogin')
	loginButton.click()
	print("[preparation] logged in successfully")
	# Switching to Left Frame and accessing element by text
	browser.switch_to.default_content()
	frame = browser.find_element_by_name('leftFrame')
	browser.switch_to.frame(frame)
	nonFixedInstructor = browser.find_element_by_link_text('Booking without Fixed Instructor')
	nonFixedInstructor.click()
	# Switching back to Main Frame and pressing 'I Accept'
	browser.switch_to.default_content()
	wait = WebDriverWait(browser, 300)
	wait.until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_name('mainFrame')))
	wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn"))).click()
	# Selection menu
	browser.switch_to.default_content()
	wait = WebDriverWait(browser, 300)
	wait.until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_name('mainFrame')))
	wait.until(EC.visibility_of_element_located((By.ID, "checkMonth")))
	for x in toBookMonths: # [modified by looi] simple for loop
		# 0 refers to first month, 1 refers to second month, and so on...
		months = browser.find_elements_by_id('checkMonth')
		months[x].click() # all months
	for x in toBookSessions: # [modified by looi] simple for loop
		# 0 refers to first session, 1 refers to second session, and so on...
		sessions = browser.find_elements_by_id('checkSes')
		sessions[x].click() # all sessions
	for x in toBookDays: # [modified by looi] simple for loop
		# 0 refers to first day, 1 refers to second day, and so on...
		days = browser. find_elements_by_id('checkDay')
		days[x].click() # all days
	print("[preparation] preparation complete!")


# Infinite loop here
count = 0
while 1:
	print("[preparation] executing openPage function")
	slot = 0
	try:
		openPage()
		print("[preparation] starting loop")
	except:
		print("[fatal] incorrect credentials? script could not open webpage properly")
		exit()
	try: # [modified by looi] infinite loop [mix of original and modified code]
		while 1:
			# Selecting Search
			count = count + 1
			print("[", count, "] starting attempt", count)
			print("[", count, "] searching for slots")
			browser.find_element_by_name('btnSearch').click()

			# Dismissing Prompt
			wait = WebDriverWait(browser, 10)
			v = random.randint(20,121)
			wait.until(EC.alert_is_present())
			alert_obj = browser.switch_to.alert
			alert_obj.accept()
			time.sleep(2) # give the system abit of wait time
			if len(browser.find_elements_by_id("TblSpan2")) == 1: # [modified by looi] detects if the slots are booked
				# Selecting Submit
				print("[", count, "] no available slots detected")
				print("[", count, "] delaying back button press for", int(v/5), "seconds")
				time.sleep(v/5)
				wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn"))).click()
				print("[", count, "] delaying for another", v, "seconds")
				time.sleep(v)
			else:
				print("[", count, "] slots detected, rushing the purchse!")
				# 0 refers to first slot, 1 refers to second slot, and so on...
				slots = browser.find_elements_by_name('slot')
				for slot in slots:	 # Selecting all checkboxes
					slot.click()
					browser.find_element_by_class_name('pgtitle').click()	 # clicking random element to hide hover effect
				# Selecting Submit
				browser.find_element_by_name('btnSubmit').click()
				# Selecting confirm
				wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Confirm']")))
				browser.find_element_by_xpath("//input[@value='Confirm']").click()
				print("[", count, "] Slot booked! Please check webpage for details")
				print("[", count, "] delaying back button press for", int(v/5), "seconds")
				if len(browser.find_elements_by_id("errtblmsg")) == 1:
					print("[", count, "] failed to sntach?")
				else:
					print("[", count, "] Slot booked! Please check webpage for details")
					slot = 1
				time.sleep(v/5)
				browser.quit()
				exit()
	except:
		if slot == 1:
			print("[notice] crlt + c to stop bot. Or leave it to continue booking more")
		else:
			print("[notice] script ran into some error? Crlt + C again to stop bot")
		print("[notice] attempting to restart script in", v + 11, "seconds..")
		time.sleep(v + 11)
		browser.quit()



