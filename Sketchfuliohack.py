import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import keyboard
import os
os.system('cls')
print('\033[2;36;40m')
print(""" 
 _   _ _____ ___________ ___________  ___  _     _ _____             
| | | |  ___/  ___| ___ |  ___| ___ \/ _ \| |   ( /  ___|            
| | | | |__ \ `--.| |_/ | |__ | |_/ / /_\ | |   |/\ `--.             
| | | |  __| `--. |  __/|  __||    /|  _  | |      `--. \            
\ \_/ | |___/\__/ | |   | |___| |\ \| | | | |____ /\__/ /            
 \___/\____/\____/\_|   \____/\_| \_\_| |_\_____/ \____/             
                                                                     
                                                                     
 _____ _   _______ _____ _____ _   _______ _   _ _      _____ _____  
/  ___| | / |  ___|_   _/  __ | | | |  ___| | | | |    |_   _|  _  | 
\ `--.| |/ /| |__   | | | /  \| |_| | |_  | | | | |      | | | | | | 
 `--. |    \|  __|  | | | |   |  _  |  _| | | | | |      | | | | | | 
/\__/ | |\  | |___  | | | \__/| | | | |   | |_| | |______| |_\ \_/ / 
\____/\_| \_\____/  \_/  \____\_| |_\_|    \___/\_____(_\___/ \___/  
                                                                     
                                                                     
 _   _  ___  _____ _   __                                            
| | | |/ _ \/  __ | | / /                                            
| |_| / /_\ | /  \| |/ /                                             
|  _  |  _  | |   |    \                                             
| | | | | | | \__/| |\  \                                            
\_| |_\_| |_/\____\_| \_/                                            
                                                                     
                                                                     
 __                                                                  
 \ \                                                                 
(_| |                                                                
  | |                                                                
 _| |                                                                
(_| |                                                                
 /_/                                                                 
                                                                     """)




playername = "nick" #the nickname of the player
url = input("paste URL here>> ")
driver = webdriver.Firefox(executable_path=r'geckodriver.exe') #launches selenium using the gecko webdriver
driver.set_window_size(1024,768)
os.system('cls')
print('\033[2;32;40m')
driver.get(url)
set_name = driver.find_element_by_id("nick") #the id element of the name input field in skribbl.io 
set_name.send_keys(playername)
game_mode = input("Free draw? Play? Custome Game?(f/p/c)>> ")
try:
    if game_mode == "p":
        time.sleep(2)
        button = driver.find_element_by_id("play")
        button.click()
    elif game_mode == "c":
        time.sleep(2)
        button = driver.find_element_by_id("private")
        button.click()
    elif game_mode == "f":
        time.sleep(2)
        button = driver.find_element_by_id("practice")
        button.click()
    else:
        print("not choosing gamemode")


except:
    print("not choosing gamemode")

while True:
    try:
        print('\033[2;32;40m')
        os.system('cls')
        failsafe = str(input("Activate emergency guesser. Note that this is less efficient?(y/n)>> "))
        
        time.sleep(3)
        chat_function = driver.find_element_by_id("gameChatInput")
        chat_function.click()
        if failsafe == "y":
            print('\033[2;31;40m')
            print("Activating emergency guesser.")
            word_length = int(input("word length>> ")) #small bug where you need to specify 1 more than the original word length
            with open('Everysinglewordever.txt', 'r') as z:
                for word in z:
                    if len(word) == word_length:
                        print(word)
                        chat_function.send_keys(word)
                        chat_function.send_keys(Keys.RETURN)
                        time.sleep(0.65)
                        if keyboard.is_pressed('q'):
                            print('\033[2;31;40m')
                            print("breaking...")
                            break
        else:
            print("Not activating emergency guesser.")
            word_length = int(input("word length>> ")) #small bug where you need to specify 1 more than the original word length
            letter_found = str(input("input a letter>> "))#input the letter you see in the word as the game progresses
            index_of_letter = int(input("pls input a index of letter>> "))#input the index of the word. first index of the word is 0
            with open('Everysinglewordever.txt', 'r') as f:
                for word in f:
                    if len(word) == word_length:
                        if letter_found in word:
                            if letter_found == word[index_of_letter]: #returns the word that has the letter in the required index e.g returns word dog if letter o is index 1 and the word length is 3
                                print(word)
                                chat_function.send_keys(word)
                                chat_function.send_keys(Keys.RETURN)
                                time.sleep(0.65)
                                if keyboard.is_pressed('q'):
                                    print('\033[2;31;40m')
                                    print("breaking...")
                                    break
        

               
                

    
    except:
        print("error")
driver.quit()

    

    
    
                    
                    
                   

                

    
