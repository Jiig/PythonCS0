from cs0 import *

setColor(BLUE)
setCaption("hello")

charlie = Circle(10, RED, 0,0) + Circle(10, YELLOW, 5,5) #+ Rectangle(10,15, AQUA,0, 10)
#print(type(charlie))
#add(sam, 326, 119)
#charlie += sam

b = Rectangle(10,15, AQUA, 5, 10)
c = Rectangle(10, 15, BROWN, 5, 15)
#add(charlie, 321, 114)

add(b)
add(c)



def printEvent(evt):
    print(str(evt))

def mouseDrag(evt):
    charlie.setLocation(evt.pos[0], evt.pos[1])

def mouseClick(evt):
    sendToBack(c)

def key(evt):
    if evt.key == KEY_A:
        sendForward(b)
    if evt.key == KEY_B:
        sendBackward(b)

mouseClickedEvent(mouseClick)

mouseReleasedEvent(printEvent)
#mouseMovedEvent(mouseClick)
mouseDraggedEvent(mouseDrag)
keyPressedEvent(key)
keyReleasedEvent(printEvent)

start(thread = False)
#start()

waitForClick()
count = 0
while(count < 500):
    if charlie.x > window.width:
        charlie.setLocation(0,0)
    charlie.move(2, 2)
    pause(25)
    count = count + 1
    #print(count)

stop()
