import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time
import webbrowser

def hit(key):
    pyautogui.keyDown(key)
    return

#def draw():
    
#def screenshot():
def isCollide(data):
    # for birds
    for i in range(190,200):
        for j in range(260,310):
            if data[i, j] < 100 :
                hit('down')
                return    

    for i in range(180,200):
        for j in range(310,370):
            if data[i, j] < 100 :
                hit('up')
                return 
 
    return 
        

if __name__ == "__main__":
    print("Hey Dino game is about to start in 3 seconds")
    time.sleep(2)
    #webbrowser.open_new_tab('chrome://dino')
    #hit("up")
    while True:

        image = ImageGrab.grab().convert('L')
        data  = image.load()
        isCollide(data)
        #    hit("up")
        #print(asarray(image))
        
        # for cactus
        
    '''
        for i in range(190,210):
            for j in range(310,370):
               data[i, j] = 0  
        #for birds
        for i in range(180,200):
            for j in range(260,310):
               data[i, j] = 171   

    
        image.show()
        break
'''
    


