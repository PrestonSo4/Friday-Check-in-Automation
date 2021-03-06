import selenium, pyautogui as p, time, keyboard, win32api, win32con
from selenium import webdriver
from datetime import date
from getpass import getpass
date = date.today()
un = 's-sop' #Use this for ease of access. If you just want to run the code faster
#un = input('Enter your username for synergy: ')
pw = '' #Use this for ease of access. If you just want to run the code faster
pw = getpass('Enter your password for synergy:')
email = un + '@bsd405.org'
#! I suggest assign the username and email but not password !#
#quarter = 'Quarter1'
#quarter = 'Quarter2'
quarter = 'Quarter3'
#quarter = 'Quarter4'
def pClick(): 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def moveClick(x,y, time):
    import time
    p.moveTo(x,y)
    time.sleep(0.5)
    pClick()
def sendText(xpath, text):
    from time import sleep
    while True:
        try:
            driver.find_element_by_xpath(xpath).send_keys(text)
            break
        except:
            sleep(0.01)            
def zoom(iterations, symbol):
    p.keyDown('ctrl')
    for i in range(iterations):
        p.press(symbol)
    p.keyUp('ctrl')
def clickImage(file, con):
    from time import sleep
    time.sleep(1)
    while True:
        try:
            imageX, imageY = p.locateCenterOnScreen(file, confidence=con)
            p.moveTo(imageX,imageY)
            pClick()
            break
        except:
            sleep(0.01)
    
    time.sleep(1)
def finalStage(file, con):

    imageX, imageY = p.locateCenterOnScreen(file, confidence=con)
    p.moveTo(imageX, imageY)
    p.scroll(100)
    for i in range(45):
        p.move(0,17)
        time.sleep(0.09)
        pClick()
def pickQuarter(quarter):
    from time import sleep
    sleep(0.5)
    clickImage('Quarter_Button.png', 0.98)
    clickImage(quarter+'.png',0.98)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://wa-bsd405-psv.edupoint.com/PXP2_Login.aspx')
moveClick(1248,450,.5)
sendText('//*[@id="ctl00_MainContent_username"]', un)
sendText('//*[@id="ctl00_MainContent_password"]', pw)
driver.find_element_by_xpath('//*[@id="ctl00_MainContent_Submit1"]').click()
clickImage('Grade_Book_Button.png',0.7)
zoom(2, '-')

pickQuarter(quarter)
while True:
    try:
        startX, startY = p.locateCenterOnScreen('Grades.png', confidence=0.98) #I'm using the locate image function so that the coords wont have to change depending on screensize
        break
    except:
        print('Not found')
        time.sleep(0.01)

startX -= 140 #getting the top left corner of image by dividing the screenshot size by 2 and subtracting it
startY += 20
p.keyDown('win') #Toggling the shortcut for taking screenshots (WIN + SHIFT + 's')
p.keyDown('shift') #I'm holding down the keys so the shortcut will work.
p.press('s')
p.keyUp('win') #Releasing keys
p.keyUp('shift') #Releasing keys
pClick()
time.sleep(1)
p.moveTo(startX, startY) #Going to the top left coords
p.drag(513,581, 1, button='left') #Dragging to the specified screenshot size
#screenshot coords: move right - 513,move down - 581

driver.get('https://bsd405.sharepoint.com/:o:/r/sites/Section_df6688a0-c5d8-4d46-9b97-ccca24375f14/_layouts/15/Doc.aspx?sourcedoc=%7BEB5E2917-A691-40E9-8E8B-0A2CDCA5030C%7D&file=2020-FY-P7-Advisory%203%20Notebook&action=edit&mobileredirect=true&wdorigin=Sharepoint&RootFolder=%2Fsites%2FSection_df6688a0-c5d8-4d46-9b97-ccca24375f14%2FSiteAssets%2F2020-FY-P7-Advisory%203%20Notebook&web=1&ct=1617479094686&wdOrigin=OFFICECOM-WEB.START.MRU&cid=2bfb33b6-e868-42dc-9703-cd714cd75f18')
sendText('//*[@id="i0116"]', email)
clickImage('Next.png', 0.7)
sendText('//*[@id="i0118"]', pw)
clickImage('Sign_in.png',0.7)
time.sleep(0.5)
pClick()
clickImage('So_ Preston_D_(Student)_Tab.png', 0.7)
clickImage('Friday_Check_in_Tab.png', 0.7)
time.sleep(0.5)
finalStage('Start_Landmark.png', 0.98)
time.sleep(2)
clickImage('Grade_Landmark.png', 0.98)
p.move(-40, 40)
p.doubleClick()
p.keyDown('ctrl')
p.press('v')
p.keyUp('ctrl')
print('All Done!')
time.sleep(10)
driver.close()
"""
--LAYOUT--

Driver gets page: https://wa-bsd405-psv.edupoint.com/PXP2_Login.aspx ???
Clicks 'I am student' button ???
Enters login information ???
Clicks sign in ???
Clicks 'Gradebook' button ???
Zooms out to 80% Zoom ???
Presses keys: 'WIN+SHIFT+S' ???
Takes screenshot at specific coords (I have to get pyautogui to hold mouse down) ???
Goes to: https://bsd405.sharepoint.com/:o:/r/sites/Section_df6688a0-c5d8-4d46-9b97-ccca24375f14/_layouts/15/Doc.aspx?sourcedoc=%7BEB5E2917-A691-40E9-8E8B-0A2CDCA5030C%7D&file=2020-FY-P7-Advisory%203%20Notebook&action=edit&mobileredirect=true&wdorigin=Sharepoint&RootFolder=%2Fsites%2FSection_df6688a0-c5d8-4d46-9b97-ccca24375f14%2FSiteAssets%2F2020-FY-P7-Advisory%203%20Notebook&web=1&ct=1617479094686&wdOrigin=OFFICECOM-WEB.START.MRU&cid=2bfb33b6-e868-42dc-9703-cd714cd75f18 ???
Look for the 'So, Preston D (Student)' tab ???
Click on 'So, Preston D (Student) tab  ???
Look for the 'Friday Check-in' button  ???
Click on Friday Check-in button  ???
Click on specific date coords ???
click on specific coords within the page ???
Presses keys 'CTRL+C' ???
Driver.Close() ???
--End--
"""