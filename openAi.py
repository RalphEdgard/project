import mouse 
import webbrowser
import keyboard 
import time 
import pyautogui
import io 
import os 

previousBatch=""
textForAi = ""
count = 0
refreshPage = False
successfulRequest=False
errorText=""
url = "https://chat.openai.com/chat/b7f7927f-ac64-4a24-87a5-1e6604093486"


webbrowser.open(url)
time.sleep(4)

mouse.move(1055, 922)
mouse.click('left')
keyboard.write("make sure to provide the most concise responses possible.")
keyboard.send("enter")

time.sleep(10)

def cleanErrorFile():
    # Empties the error file
    time.sleep(2)
    pyautogui.hotkey('win', 'm')
    time.sleep(2)
    pyautogui.press('win')
    time.sleep(2)
    keyboard.write('ErrorTex')
    time.sleep(2)
    keyboard.send('enter')
    time.sleep(2)
    pyautogui.hotkey('win','up')
    mouse.click('left')
    mouse.click('left')
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    keyboard.write('a')

    # Close the notepad window 
    pyautogui.hotkey('win','up')
    time.sleep(2)
    mouse.move(1892, 2)
    time.sleep(2)
    mouse.click('left')
    mouse.click('left')
    time.sleep(2)
    mouse.move(830, 590)
    time.sleep(2)
    mouse.click('left')
    mouse.click('left')
    time.sleep(2)
    os.system('cmd /c "taskkill/im Notepad.exe"')

    # opens google window again 
    pyautogui.hotkey('win', 'tab')
    time.sleep(2)
    mouse.move(713, 377)
    time.sleep(2)
    mouse.click('left')
    mouse.click('left')
    time.sleep(2)
    mouse.click('left')
    mouse.click('left')

#Train the open ai to listen to instructions 
while True:
    # This portion is going to be use to train the ai 
    with io.open('inputForProgram.txt','r', encoding='utf-8', errors='ignore') as file:
        cleanErrorFile()
        for line in file:     
            for word in line.split():
                textForAi = textForAi + word + " "
                count = count + 1
                if count%250 == 0:
                    with open('ErrorText.txt', encoding="utf8") as f:
                        print("Getting Previous text....")
                        previousBatch=previousBatch + textForAi + " "
                        while 'There was an error generating a response' in f.read() or 'Too many requests in 1 hour. Try again later.' in f.read():

                            print("Error: Program will try again in 2 minutes....")
                            print(time.sleep(120))

                            print("will refresh the page....")
                            pyautogui.hotkey('ctrl','r')

                            print("Cleaning File....")
                            cleanErrorFile()
                            
                            time.sleep(2)
                            mouse.move(1055, 922)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            keyboard.write(previousBatch, delay=0.025)
                            time.sleep(2)
                            keyboard.send("enter")

                            # Gets all text from screen and saves it in the ErrorText.txt file 
                            time.sleep(3)
                            mouse.move(461, 912)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','a')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl', 'c')
                            time.sleep(2)
                            pyautogui.hotkey('win', 'm')
                            time.sleep(2)
                            pyautogui.press('win')
                            time.sleep(2)
                            keyboard.write('ErrorTex')
                            time.sleep(2)
                            keyboard.send('enter')
                            time.sleep(2)
                            pyautogui.hotkey('win','up')
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','a')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','v')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','s')

                            # Close the notepad window

                            time.sleep(2) 
                            pyautogui.hotkey('win','up')
                            time.sleep(2)
                            mouse.move(1892, 2)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            os.system('cmd /c "taskkill/im Notepad.exe"')

                            # opens google window again 
                            time.sleep(2)
                            pyautogui.hotkey('win', 'tab')
                            time.sleep(2)
                            mouse.move(713, 377)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                        
                        if 'There was an error generating a response' in f.read() or 'Too many requests in 1 hour. Try again later.' not in f.read(): 
                            
                            previousBatch=""      
                            
                            numToTakeAway = count
                            time.sleep(2)
                            mouse.move(1055, 922)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            keyboard.write(textForAi, delay=0.025)
                            time.sleep(2)
                            keyboard.send("enter")
                            textForAi=""

                            # Gets all text from screen and saves it in the ErrorText.txt file 
                            time.sleep(3)
                            mouse.move(461, 912)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','a')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl', 'c')
                            time.sleep(2)
                            pyautogui.hotkey('win', 'm')
                            time.sleep(2)
                            pyautogui.press('win')
                            time.sleep(2)
                            keyboard.write('ErrorTex')
                            time.sleep(2)
                            keyboard.send('enter')
                            time.sleep(2)
                            pyautogui.hotkey('win','up')
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','a')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','v')
                            time.sleep(2)
                            pyautogui.hotkey('ctrl','s')

                            # Close the notepad window 
                            time.sleep(2)
                            pyautogui.hotkey('win','up')
                            time.sleep(2)
                            mouse.move(1892, 2)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            os.system('cmd /c "taskkill/im Notepad.exe"')

                            # opens google window again 
                            time.sleep(2)
                            pyautogui.hotkey('win', 'tab')
                            time.sleep(2)
                            mouse.move(713, 377)
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                            time.sleep(2)
                            mouse.click('left')
                            mouse.click('left')
                
            if line == '':
                break