import pyautogui as p
import time as t
t.sleep(1)

a=1073,639
a_new=1100,630
a_p=1088,649

e=575,658
g=892,443
move=192,387

red=(255,223,146)
exit2=(17,83,223)
gadTime=0

#Point1=(x=104, y=94)
#RGB1=(red=88, green=90, blue=107)
#print(p.position())

move_count=0


for i in range(5000):
    print(i)
    if(not p.pixelMatchesColor(1100,630,red)):
        p.click(a)
        t.sleep(0.1)
        if(move_count<=10):
            p.mouseDown(192,387)
            p.moveRel(-30,-30,0.3,p.easeInQuad)
            t.sleep(2)
            p.mouseUp()
            move_count+=1
    elif(p.pixelMatchesColor(1100,630,(227,63,39))):
         move_count=0
    else:
        gadTime=95
        
    if(gadTime<=300):
        gadTime+=1
        if(gadTime%100==0):
            p.click(g)
    t.sleep(1)
    
    '''
    if(not p.pixelMatchesColor(877,612,(97,247,255))):
        t.sleep(1)
        if(not p.pixelMatchesColor(877,612,(97,247,255))):
            p.click(572,659)
    t.sleep(0.2)
    '''
#p.click(e)
#print(p.position())

