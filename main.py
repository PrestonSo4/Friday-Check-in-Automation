import selenium, pyautogui as p, time, keyboard, win32api, win32con
from selenium import webdriver
from getpass import getpass
un = input('Enter your username for synergy: ')
pw = getpass('Enter your password for synergy:')
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
    driver.find_element_by_xpath(xpath).send_keys(text)
def zoom(iterations, symbol):
    p.keyDown('ctrl')
    for i in range(iterations):
        p.press(symbol)
    p.keyUp('ctrl')
def clickImage(file):
    import time
    time.sleep(1)
    image = p.locateOnScreen(file)
    imageX, imageY = p.center(image)
    p.click(imageX, imageY)
    time.sleep(1)
    
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://wa-bsd405-psv.edupoint.com/PXP2_Login.aspx')
moveClick(1248,450,.5)
sendText('//*[@id="ctl00_MainContent_username"]', un)
sendText('//*[@id="ctl00_MainContent_password"]', pw)
driver.find_element_by_xpath('//*[@id="ctl00_MainContent_Submit1"]').click()
clickImage('Grade_Book_Button.png')
zoom(2, '-')
time.sleep(2)
#loc= p.locateOnScreen('Grades.png', confidence=0.6)
#gX, gY = loc
p.keyDown('win')
p.keyDown('shift')
p.press('s')
p.keyUp('win')
p.keyUp('shift')
#p.moveTo(startX, startY)

#screenshot coords: move right - 513,move down - 581
"""
--LAYOUT--

Driver gets page: https://wa-bsd405-psv.edupoint.com/PXP2_Login.aspx 
Clicks 'I am student' button
Enters login information
Clicks sign in
Clicks 'Gradebook' button
Zooms out to 80% Zoom
Presses keys: 'CTRL+SHIFT+S'
Takes screenshot at specific coords (I have to get pyautogui to hold mouse down)
Goes to: https://bsd405.sharepoint.com/:o:/r/sites/Section_df6688a0-c5d8-4d46-9b97-ccca24375f14/_layouts/15/Doc.aspx?sourcedoc=%7BEB5E2917-A691-40E9-8E8B-0A2CDCA5030C%7D&file=2020-FY-P7-Advisory%203%20Notebook&action=edit&mobileredirect=true&wdorigin=Sharepoint&RootFolder=%2Fsites%2FSection_df6688a0-c5d8-4d46-9b97-ccca24375f14%2FSiteAssets%2F2020-FY-P7-Advisory%203%20Notebook&web=1&ct=1617479094686&wdOrigin=OFFICECOM-WEB.START.MRU&cid=2bfb33b6-e868-42dc-9703-cd714cd75f18
Look for the 'So, Preston D (Student)' tab
Click on 'So, Preston D (Student) tab 
Look for the 'Friday Check-in' button 
Click on Friday Check-in button 
Click on specific date coords
click on specific coords within the page
Presses keys 'CTRL+C'
Driver.Close()
--End--
"""