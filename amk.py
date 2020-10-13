
key=None
button=None
keyboard=None
mouse=None

def setupKeyboard():
    global keyboard,key
    from pynput.keyboard import Key, Controller
    keyboard=Controller()
    key=Key
def setupMouse():
    global mouse,button
    from pynput.mouse import Button, Controller
    mouse = Controller()
    button=Button