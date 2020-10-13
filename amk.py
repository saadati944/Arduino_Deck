import time
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

def getKey(inp):
    if inp=='shift':
        return key.shift
    if inp=='enter':
        return key.enter
    if inp=='ctrl':
        return key.ctrl
    if inp=='cmd':
        return key.cmd
    else:
        for k in key:
            if str(k)[4:]==inp:
                return k
    return key.space

def getKey(inp):
    if inp=='shift':
        return key.shift
    if inp=='enter':
        return key.enter
    if inp=='ctrl':
        return key.ctrl
    if inp=='cmd':
        return key.cmd
    else:
        for k in key:
            if str(k)[4:]==inp:
                return k
    return key.space



def execute(lines):
    nextconfig=''
    for line in lines:
        if line=='' or line[0]=='#':
            continue
        if line[-1]=='\n':
            line=line[:-1]
        if line.startswith('type:'):
            try:
                a=line[5:]
                #print('typing',a)
                keyboard.type(a)
            except:
                pass
                #print("can't execute" ,line)
        elif line.startswith('sleep:'):
            try:
                a=line[6:]
                #print('sleeping',a)
                time.sleep(float(a))
            except:
                pass
                #print("can't execute" ,line)
        elif line.startswith('down:'):
            try:
                a=line[5:]
                #print('pressing',a)
                if len(a)==1:
                    keyboard.press(a)
                else:
                    keyboard.press(getKey(a))
            except:
                pass
                #print("can't execute" ,line)
        elif line.startswith('up:'):
            try:
                a=line[3:]
                #print('releasing',a)
                if len(a)==1:
                    keyboard.release(a)
                else:
                    keyboard.release(getKey(a))
            except:
                pass
                #print("can't execute" ,line)
        elif line.startswith('goto:'):
            try:
                a=line[5:]
                x=int(a[:a.index(',')])
                y=int(a[a.index(',')+1:])
                mouse.position=(x,y)
                #print('going to',x,',',y)
            except:
                pass
                #print("can't execute" ,line)
        elif line.startswith('move:'):
            try:
                a=line[5:]
                x=int(a[:a.index(',')])
                y=int(a[a.index(',')+1:])
                mouse.move(x,y)
                #print('moving by',x,',',y)
            except:
                pass
                #print("can't execute" ,line)
        elif line=='click:left':
            try:
                mouse.click(button.left)
                #print('left clicking (on mouse)')
            except:
                pass
                #print("can`t execute" ,line)
        elif line=='click:right':
            try:
                mouse.click(button.right)
                #print('right clicking (on mouse)')
            except:
                pass
                #print("can`t execute" ,line)
        elif line=='click:middle':
            try:
                mouse.click(button.middle)
                #print('middle clicking (on mouse)')
            except:
                pass
                #print("can`t execute" ,line)
        elif line=='mousedown:left':
            try:
                mouse.press(button.left)
                #print('mousedown left')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='mouseup:left':
            try:
                mouse.release(button.left)
                #print('mouseup left')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='mousedown:right':
            try:
                mouse.press(button.right)
                #print('mousedown right')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='mouseup:right':
            try:
                mouse.release(button.right)
                #print('mouseup right')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='mousedown:middle':
            try:
                mouse.press(button.middle)
                #print('mousedown middle')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='mouseup:middle':
            try:
                mouse.release(button.middle)
                #print('mouseup middle')
            except:
                pass
                #print("can't execute" ,line)
        elif line=='exit':
            exit()
        elif line.startswith('<') :
            nextconfig=line[1:]
    return nextconfig
