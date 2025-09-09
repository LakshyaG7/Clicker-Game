#Clicker Game

'''
Project by Lakshya Goenka and Aarush Bhat
Date- 07-09-2021
Project Name- Clicker Mining Game

'''

#Instructions for the game

'''

This is a Clicker game in which your aim is to find more resources.
You get elements or resources after every few hits on the mine depending on the rarity of the element.
These resources can be used to buy upgrades- Tools or Robots.
These upgrades can be used to increase the efficiency of the clicking.
You may get upgrades at any point during the game provided that you have adequate resources.
This is an endless game so you can play it till whenever you want and break your record every time.

Resources (Requirements)- 
1.  Stone- 1 hit
2.  Coal- 20 hits
3.  Silver- 50 hits
4.  Gold- 100 hits
5.  Platinum- 200 hits
6.  Emerald- 500 hits
7.  Ruby- 1000 hits
8.  Diamond- 2000 hits
9.  Void- 5000 hits
10. Imperium- 10000 hits

Each of these resources is linked to one of the upgrades as mentioned below and can be used to buy to it. 

Upgrades (Requirements)-
1.  Stone Pickaxe- 50 Stones
2.  Flame Thrower- 50 Coal
3.  Sledge Hammer- 50 Silver
4.  Jack Hammer- 50 Platinum
5.  Ruby Pickaxe- 50 Ruby
6.  Void Pickaxe- 50 Void
7.  Mining Drill- 50 Imperium
8.  Starter Robot- 50 Gold
9.  Pro Robot- 50 Emerald
10. Legendary Robot- 50 Diamond

'''


#Importing the Libraries

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random



#Setting up the Tkinter window

game=Tk()
game.title("Clicker Miner")
game.geometry("1500x1000")
game.resizable(0,0)


#Variables for all the items or elements

coal=0
diamond=0
ruby=0
emerald=0
gold=0
imperium=0
platinum=0
silver=0
stone=0
void=0


#Variables for incrementing the values

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0

counter=0
increment=1
cost_increase=1.2
amount=1


#Variables for cost of each tool

Stonepickaxe_C= 50
Flamethrower_C= 50
Sledgehammer_C= 50
Jackhammer_C= 50
Rubypickaxe_C=50
Voidpickaxe_C=50
Miningdrill_C=50
Starterrobot_C=50
Prorobot_C=50
Legendaryrobot_C=50


#Variables for no. of each tools

Stonepickaxe_T=0
Flamethrower_T=0
Sledgehammer_T=0
Jackhammer_T=0
Rubypickaxe_T=0
Voidpickaxe_T=0
Miningdrill_T=0
Starterrobot_T=0
Prorobot_T=0
Legendaryrobot_T=0


#Creating a canvas for all the GUI
canvas= Canvas(game,width=1500,height=1000)
canvas.pack()


#GUI

background= (Image.open('Clicker Game/GUI Base.png'))
resphoto1=background.resize((1450,950),Image.LANCZOS)
newimage1=ImageTk.PhotoImage(resphoto1)
canvas.create_image(750,500, image=newimage1)


#Images

#Image for the mine

Mine= (Image.open("Clicker Game/stone.png"))
resphoto=Mine.resize((500,485),Image.LANCZOS)
newimage=ImageTk.PhotoImage(resphoto)


#Images for tools' buttons

Stonepickaxe= (Image.open("Clicker Game/Stone Pickaxe_Label.png"))
resphoto12=Stonepickaxe.resize((125,125),Image.LANCZOS)
newimage12=ImageTk.PhotoImage(resphoto12)

Flamethrower= (Image.open("Clicker Game/Flame Thrower_Label.png"))
resphoto13=Flamethrower.resize((125,125),Image.LANCZOS)
newimage13=ImageTk.PhotoImage(resphoto13)

Sledgehammer= (Image.open("Clicker Game/Sledge Hammer_Label.png"))
resphoto14=Sledgehammer.resize((125,125),Image.LANCZOS)
newimage14=ImageTk.PhotoImage(resphoto14)

Jackhammer= (Image.open("Clicker Game/Jack hammer_Label.png"))
resphoto15=Jackhammer.resize((125,125),Image.LANCZOS)
newimage15=ImageTk.PhotoImage(resphoto15)

Rubypickaxe= (Image.open("Clicker Game/Ruby Pickaxe_Label.png"))
resphoto16=Rubypickaxe.resize((125,125),Image.LANCZOS)
newimage16=ImageTk.PhotoImage(resphoto16)

Voidpickaxe= (Image.open("Clicker Game/Void Pickaxe_Button.png"))
resphoto17=Voidpickaxe.resize((125,125),Image.LANCZOS)
newimage17=ImageTk.PhotoImage(resphoto17)

Miningdrill= (Image.open("Clicker Game/Mining Drill_Label.png"))
resphoto18=Miningdrill.resize((125,125),Image.LANCZOS)
newimage18=ImageTk.PhotoImage(resphoto18)


#Automatic Clickers' buttons' Images

Starterrobot= (Image.open("Clicker Game/Starter Robot_Button.png"))
resphoto19=Starterrobot.resize((70,70),Image.LANCZOS)
newimage19=ImageTk.PhotoImage(resphoto19)

Prorobot= (Image.open("Clicker Game/Pro Robot_Label.png"))
resphoto20=Prorobot.resize((70,70),Image.LANCZOS)
newimage20=ImageTk.PhotoImage(resphoto20)

Legendaryrobot= (Image.open("Clicker Game/Legendary Robot_Label.png"))
resphoto21=Legendaryrobot.resize((70,70),Image.LANCZOS)
newimage21=ImageTk.PhotoImage(resphoto21)


#Images for showing total items in upgrades

STARTERrobot=(Image.open("Clicker Game/Starter Robot.png"))
resphoto22=STARTERrobot.resize((150,150),Image.LANCZOS)
newimage22=ImageTk.PhotoImage(resphoto22)

PROrobot= (Image.open("Clicker Game/Pro Robot.png"))
resphoto23=PROrobot.resize((150,150),Image.LANCZOS)
newimage23=ImageTk.PhotoImage(resphoto23)

LEGENDARYrobot= (Image.open("Clicker Game/Legendary Robot.png"))
resphoto24=LEGENDARYrobot.resize((150,150),Image.LANCZOS)
newimage24=ImageTk.PhotoImage(resphoto24)

STONEpickaxe= (Image.open("Clicker Game/Stone Pickaxe_Tool.png"))
resphoto25=STONEpickaxe.resize((100,100),Image.LANCZOS)
newimage25=ImageTk.PhotoImage(resphoto25)

FLAMEthrower= (Image.open("Clicker Game/Flame Thrower.png"))
resphoto26=FLAMEthrower.resize((200,200),Image.LANCZOS)
newimage26=ImageTk.PhotoImage(resphoto26)

SLEDGEhammer= (Image.open("Clicker Game/Sledge Hammer.png"))
resphoto27=SLEDGEhammer.resize((150,150),Image.LANCZOS)
newimage27=ImageTk.PhotoImage(resphoto27)

JACKhammer= (Image.open("Clicker Game/Jack Hammer.png"))
resphoto28=JACKhammer.resize((150,150),Image.LANCZOS)
newimage28=ImageTk.PhotoImage(resphoto28)

RUBYpickaxe= (Image.open("Clicker Game/Ruby Pickaxe_Tool.png"))
resphoto29=RUBYpickaxe.resize((100,100),Image.LANCZOS)
newimage29=ImageTk.PhotoImage(resphoto29)

VOIDpickaxe= (Image.open("Clicker Game/Void Pickaxe_Tool.png"))
resphoto30=VOIDpickaxe.resize((100,100),Image.LANCZOS)
newimage30=ImageTk.PhotoImage(resphoto30)

MININGdrill= (Image.open("Clicker Game/Mining Drill.png"))
resphoto31=MININGdrill.resize((175,175),Image.LANCZOS)
newimage31=ImageTk.PhotoImage(resphoto31)


#Images for all the elements

Stone_item= (Image.open("Clicker Game/stone_item.png"))
resphoto2=Stone_item.resize((45,45),Image.LANCZOS)
newimage2=ImageTk.PhotoImage(resphoto2)
canvas.create_image(120,117, image=newimage2)

coal_item= (Image.open("Clicker Game/coal_item.png"))
resphoto3=coal_item.resize((45,45),Image.LANCZOS)
newimage3=ImageTk.PhotoImage(resphoto3)
canvas.create_image(120,167, image=newimage3)

silver_item= (Image.open("Clicker Game/silver_item.png"))
resphoto4=silver_item.resize((45,45),Image.LANCZOS)
newimage4=ImageTk.PhotoImage(resphoto4)
canvas.create_image(120,217, image=newimage4)

gold_item= (Image.open("Clicker Game/gold_item.png"))
resphoto5=gold_item.resize((45,45),Image.LANCZOS)
newimage5=ImageTk.PhotoImage(resphoto5)
canvas.create_image(120,267, image=newimage5)

platinum_item= (Image.open("Clicker Game/platinum_item.png"))
resphoto6=platinum_item.resize((45,45),Image.LANCZOS)
newimage6=ImageTk.PhotoImage(resphoto6)
canvas.create_image(120,317, image=newimage6)

emerald_item= (Image.open("Clicker Game/emerald_item.png"))
resphoto7=emerald_item.resize((45,45),Image.LANCZOS)
newimage7=ImageTk.PhotoImage(resphoto7)
canvas.create_image(120,367, image=newimage7)

ruby_item= (Image.open("Clicker Game/ruby_item.png"))
resphoto8=ruby_item.resize((45,45),Image.LANCZOS)
newimage8=ImageTk.PhotoImage(resphoto8)
canvas.create_image(120,417, image=newimage8)

diamond_item= (Image.open("Clicker Game/diamond_item.png"))
resphoto9=diamond_item.resize((45,45),Image.LANCZOS)
newimage9=ImageTk.PhotoImage(resphoto9)
canvas.create_image(120,467, image=newimage9)

void_item= (Image.open("Clicker Game/void_item.png"))
resphoto10=void_item.resize((45,45),Image.LANCZOS)
newimage10=ImageTk.PhotoImage(resphoto10)
canvas.create_image(120,517, image=newimage10)

imperium_item= (Image.open("Clicker Game/imperium_item.png"))
resphoto11=imperium_item.resize((45,45),Image.LANCZOS)
newimage11=ImageTk.PhotoImage(resphoto11)
canvas.create_image(120,567, image=newimage11)


#Labels

#Label for Game Title

titlelabel= tk.Label(game, text='CLICKER MINER',font=('Helvetica Bold',40),fg='White', bg='Brown')
titlelabel.place(x=575,y=25)

#Labels for Elements and Counter

counterlabel= tk.Label(game,text=('Mine Counter:'+ str(counter)),fg='white',bg='Brown',font=('Helvetica',15))
counterlabel.place(x=97,y=55)

stonelabel= tk.Label(game,text=('Stone= '+str(stone)),font=('Helvetica',15),fg='white',bg='Brown')
stonelabel.place(x=147,y=100)

coallabel= tk.Label(game,text=('Coal= '+str(coal)),font=('Helvetica',15),fg='white',bg='Brown')
coallabel.place(x=147,y=150)

silverlabel= tk.Label(game,text=('Silver= '+str(silver)),font=('Helvetica',15),fg='white',bg='Brown')
silverlabel.place(x=147,y=200)

goldlabel= tk.Label(game,text=('Gold= '+str(gold)),font=('Helvetica',15),fg='white',bg='Brown')
goldlabel.place(x=147,y=250)

platinumlabel= tk.Label(game,text=('Platinum= '+str(platinum)),font=('Helvetica',15),fg='white',bg='Brown')
platinumlabel.place(x=147,y=300)

emeraldlabel= tk.Label(game,text=('Emerald= '+str(emerald)),font=('Helvetica',15),fg='white',bg='Brown')
emeraldlabel.place(x=147,y=350)

rubylabel= tk.Label(game,text=('Ruby= '+str(ruby)),font=('Helvetica',15),fg='white',bg='Brown')
rubylabel.place(x=147,y=400)

diamondlabel= tk.Label(game,text=('diamond= '+str(diamond)),font=('Helvetica',15),fg='white',bg='Brown')
diamondlabel.place(x=147,y=450)

voidlabel= tk.Label(game,text=('Void= '+str(void)),font=('Helvetica',15),fg='white',bg='Brown')
voidlabel.place(x=147,y=500)

imperiumlabel= tk.Label(game,text=('Imperium= '+str(imperium)),font=('Helvetica',15),fg='white',bg='Brown')
imperiumlabel.place(x=147,y=550)


#Labels for No. of each tool

stonepickaxe_L= tk.Label(game,text= Stonepickaxe_T, font=('Helvetica',12),fg='black',bg='white')
stonepickaxe_L.place(x=420,y=820)

flamethrower_L= tk.Label(game,text= Flamethrower_T, font=('Helvetica',12),fg='black',bg='white')
flamethrower_L.place(x=560,y=820)

sledgehammer_L= tk.Label(game,text= Sledgehammer_T, font=('Helvetica',12),fg='black',bg='white')
sledgehammer_L.place(x=700,y=820)

jackhammer_L= tk.Label(game,text= Jackhammer_T, font=('Helvetica',12),fg='black',bg='white')
jackhammer_L.place(x=840,y=820)

rubypickaxe_L= tk.Label(game,text= Rubypickaxe_T, font=('Helvetica',12),fg='black',bg='white')
rubypickaxe_L.place(x=980,y=820)

voidpickaxe_L= tk.Label(game,text= Voidpickaxe_T, font=('Helvetica',12),fg='black',bg='white')
voidpickaxe_L.place(x=1120,y=820)

miningdrill_L= tk.Label(game,text= Miningdrill_T, font=('Helvetica',12),fg='black',bg='white')
miningdrill_L.place(x=1260,y=820)


#Labels for cost of each tool

stonepickaxe_L_C= tk.Label(game,text=('Cost= ' + str(Stonepickaxe_C)), font=('Helvetica',12),fg='black',bg='white')
stonepickaxe_L_C.place(x=420,y=770)

flamethrower_L_C= tk.Label(game,text=('Cost= ' + str(Flamethrower_C)), font=('Helvetica',12),fg='black',bg='white')
flamethrower_L_C.place(x=560,y=770)

sledgehammer_L_C= tk.Label(game,text=('Cost= ' + str(Sledgehammer_C)), font=('Helvetica',12),fg='black',bg='white')
sledgehammer_L_C.place(x=700,y=770)

jackhammer_L_C= tk.Label(game,text=('Cost= ' + str(Jackhammer_C)), font=('Helvetica',12),fg='black',bg='white')
jackhammer_L_C.place(x=840,y=770)

rubypickaxe_L_C= tk.Label(game,text=('Cost= ' + str(Rubypickaxe_C)), font=('Helvetica',12),fg='black',bg='white')
rubypickaxe_L_C.place(x=980,y=770)

voidpickaxe_L_C= tk.Label(game,text=('Cost= ' + str(Voidpickaxe_C)), font=('Helvetica',12),fg='black',bg='white')
voidpickaxe_L_C.place(x=1120,y=770)

miningdrill_L_C= tk.Label(game,text=('Cost= ' + str(Miningdrill_C)), font=('Helvetica',12),fg='black',bg='white')
miningdrill_L_C.place(x=1260,y=770)


#Labels for Robots

#Labels for no. of robots

starterrobot_L= tk.Label(game,text= Starterrobot_T, font=('Helvetica',15),fg='black',bg='white')
starterrobot_L.place(x=350,y=650)

prorobot_L= tk.Label(game,text= Prorobot_T, font=('Helvetica',15),fg='black',bg='white')
prorobot_L.place(x=350,y=750)

legendaryrobot_L= tk.Label(game,text= Legendaryrobot_T, font=('Helvetica',15),fg='black',bg='white')
legendaryrobot_L.place(x=350,y=850)


#Labels for cost of robots

starterrobot_L_C= tk.Label(game,text=('Cost= ' + str(Starterrobot_C)), font=('Helvetica',15),fg='black',bg='white')
starterrobot_L_C.place(x=180,y=650)

prorobot_L_C= tk.Label(game,text=('Cost= ' + str(Prorobot_C)), font=('Helvetica',15),fg='black',bg='white')
prorobot_L_C.place(x=180,y=750)

legendaryrobot_L_C= tk.Label(game,text=('Cost= ' + str(Legendaryrobot_C)), font=('Helvetica',15),fg='black',bg='white')
legendaryrobot_L_C.place(x=180,y=850)


#Labels for tools in use

#Line for division

canvas.create_line(1000, 100, 1000, 585, fill="black", width=6)


#Label for heading

Resources= tk.Label(game, text='UPGRADES', font=('Helvetiva',35),fg='White',bg='Brown')
Resources.place(x=1075,y= 100)


#Defining the main fucntions

#Mine Function

def mine():
    global counter
    global increment
    global amount

    global stone
    global coal
    global silver
    global gold
    global platinum
    global emerald
    global ruby
    global diamond
    global void
    global imperium
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i

    counter+= increment
    counterlabel.config(text='Mine Counter:'+str(counter))
    
    stone+= increment
    stonelabel.config(text=('Stone= '+str(stone)))
    while a>=0:
        a+=increment
        if a==20:
            coal+=amount
            coallabel.config(text=('Coal= '+str(coal)))
            a=0
            break
        elif a>20 and a<=100:
            coal+=(random.randint(1,5))
            coallabel.config(text=('Coal= '+str(coal)))
            a=0
            break
        elif a>100 and a<=500:
            coal+=(random.randint(6,20))
            coallabel.config(text=('Coal= '+str(coal)))
            a=0
            break
        elif a>500:
            coal+=(random.randint(21,50))
            coallabel.config(text=('Coal= '+str(coal)))
            a=0
            break      
        break

    while b>=0:
        b+=increment
        if b==50:
            silver+=amount
            silverlabel.config(text=('Silver= '+str(silver)))
            b=0
            break
        elif b>50 and b<=250:
            silver+=(random.randint(1,5))
            silverlabel.config(text=('Silver= '+str(silver)))
            b=0
            break
        elif b>250 and b<=1250:
            silver+=(random.randint(6,20))
            silverlabel.config(text=('Silver= '+str(silver)))
            b=0
            break
        elif b>1250:
            silver+=(random.randint(21,50))
            silverlabel.config(text=('Silver= '+str(silver)))
            b=0
            break    
        break

    while c>=0:
        c+=increment
        if c==100:
            gold+=amount
            goldlabel.config(text=('Gold= '+str(gold)))
            c=0
            break    
        elif c>100 and c<=500:
            gold+=(random.randint(1,5))
            goldlabel.config(text=('Gold= '+str(gold)))
            c=0
            break  
        elif c>500 and c<=2500:
            gold+=(random.randint(6,20))
            goldlabel.config(text=('Gold= '+str(gold)))
            c=0
            break  
        elif c>2500:
            gold+=(random.randint(21,50))
            goldlabel.config(text=('Gold= '+str(gold)))
            c=0
            break  
        break

    while d>=0:
        d+=increment
        if d==200:
            platinum+=amount
            platinumlabel.config(text=('Platinum= '+str(platinum)))
            d=0
            break
        elif d>200 and d<=1000:
            platinum+=(random.randint(1,5))
            platinumlabel.config(text=('Platinum= '+str(platinum)))
            d=0
            break 
        elif d>1000 and d<=5000:
            platinum+=(random.randint(6,20))
            platinumlabel.config(text=('Platinum= '+str(platinum)))
            d=0
            break    
        elif d>5000:
            platinum+=(random.randint(21,50))
            platinumlabel.config(text=('Platinum= '+str(platinum)))
            d=0
            break  
        break

    while e>=0:
        e+=increment
        if e==500:
            emerald+=amount
            emeraldlabel.config(text=('Emerald= '+str(emerald)))
            e=0
            break 
        elif e>500 and e<=2500:
            emerald+=(random.randint(1,5))
            emeraldlabel.config(text=('Emerald= '+str(emerald)))
            e=0
            break
        elif e>2500 and e<=12500:
            emerald+=(random.randint(6,20))
            emeraldlabel.config(text=('Emerald= '+str(emerald)))
            e=0
            break
        elif e>12500:
            emerald+=(random.randint(21,50))
            emeraldlabel.config(text=('Emerald= '+str(emerald)))
            e=0
            break    
        break

    while f>=0:
        f+=increment
        if f==1000:
            ruby+=amount
            rubylabel.config(text=('Ruby= '+str(ruby)))
            f=0
            break    
        elif f>1000 and f<=5000:
            ruby+=(random.randint(1,5))
            rubylabel.config(text=('Ruby= '+str(ruby)))
            f=0
            break 
        elif f>5000 and f<=25000:
            ruby+=(random.randint(6,20))
            rubylabel.config(text=('Ruby= '+str(ruby)))
            f=0
            break
        elif f>25000:
            ruby+=(random.randint(21,50))
            rubylabel.config(text=('Ruby= '+str(ruby)))
            f=0
            break
        break

    while g>=0:
        g+=increment
        if g==2000:
            diamond+=amount
            diamondlabel.config(text=('Diamond= '+str(diamond)))
            g=0
            break
        elif g>2000 and g<=10000:
            diamond+=(random.randint(1,5))
            diamondlabel.config(text=('Diamond= '+str(diamond)))
            g=0
            break  
        elif g>10000 and g<=50000:
            diamond+=(random.randint(6,20))
            diamondlabel.config(text=('Diamond= '+str(diamond)))
            g=0
            break  
        elif g>50000:
            diamond+=(random.randint(21,50))
            diamondlabel.config(text=('Diamond= '+str(diamond)))
            g=0
            break    
        break

    while h>=0:
        h+=increment
        if h==5000:
            void+=amount
            voidlabel.config(text=('Void= '+str(void)))
            h=0
            break    
        elif h>5000 and h<=25000:
            void+=(random.randint(1,5))
            voidlabel.config(text=('Void= '+str(void)))
            h=0
            break
        elif h>25000 and h<=125000:
            void+=(random.randint(6,20))
            voidlabel.config(text=('Void= '+str(void)))
            h=0
            break
        elif h>125000:
            void+=(random.randint(21,50))
            voidlabel.config(text=('Void= '+str(void)))
            h=0
            break
        break

    while i>=0:
        i+=increment
        if i==10000:
            imperium+=amount
            imperiumlabel.config(text=('Imperium= '+str(imperium)))
            i=0
            break   
        elif i>10000 and i<=50000:
            imperium+=(random.randint(1,5))
            imperiumlabel.config(text=('Imperium= '+str(imperium)))
            i=0
            break 
        elif i>50000 and i<=250000:
            imperium+=(random.randint(6,20))
            imperiumlabel.config(text=('Imperium= '+str(imperium)))
            i=0
            break
        elif i>250000:
            imperium+=(random.randint(21,50))
            imperiumlabel.config(text=('Imperium= '+str(imperium)))
            i=0
            break
        break


#Defining the function of tool buttons

def stonepickaxe_F():
    global stone
    global Stonepickaxe_C
    global increment
    global cost_increase
    global Stonepickaxe_T
    if stone>= Stonepickaxe_C:
        stone-=Stonepickaxe_C
        stonelabel.config(text= 'Stone= '+str(stone))
        increment+=1
        Stonepickaxe_C= int(Stonepickaxe_C*cost_increase)
        stonepickaxe_L_C.config(text='Cost= '+ str(Stonepickaxe_C))
        Stonepickaxe_T+=1
        stonepickaxe_L.config(text=Stonepickaxe_T)
        canvas.create_image(1060,225, image=newimage25)

def flamethrower_F():
    global coal
    global Flamethrower_C
    global increment
    global cost_increase
    global Flamethrower_T
    if coal>= Flamethrower_C:
        coal-=Flamethrower_C
        coallabel.config(text= 'Coal= '+str(coal))
        increment+=5
        Flamethrower_C= int(Flamethrower_C*cost_increase)
        flamethrower_L_C.config(text='Cost= '+ str(Flamethrower_C))
        Flamethrower_T+=1
        flamethrower_L.config(text=Flamethrower_T)
        canvas.create_image(1180,225, image=newimage26)

def sledgehammer_F():
    global silver
    global Sledgehammer_C
    global increment
    global cost_increase
    global Sledgehammer_T
    if silver>= Sledgehammer_C:
        silver-=Sledgehammer_C
        silverlabel.config(text= 'Silver= '+str(silver))
        increment+=10
        Sledgehammer_C= int(Sledgehammer_C*cost_increase)
        sledgehammer_L_C.config(text='Cost= '+ str(Sledgehammer_C))
        Sledgehammer_T+=1
        sledgehammer_L.config(text=Sledgehammer_T)
        canvas.create_image(1300,225, image=newimage27)

def jackhammer_F():
    global platinum
    global Jackhammer_C
    global increment
    global cost_increase
    global Jackhammer_T
    if platinum>= Jackhammer_C:
        platinum-=Jackhammer_C
        platinumlabel.config(text= 'Platinum= '+str(platinum))
        increment+=50
        Jackhammer_C= int(Jackhammer_C*cost_increase)
        jackhammer_L_C.config(text='Cost= '+ str(Jackhammer_C))
        Jackhammer_T+=1
        jackhammer_L.config(text=Jackhammer_T)
        canvas.create_image(1180,325, image=newimage28)

def rubypickaxe_F():
    global ruby
    global Rubypickaxe_C
    global increment
    global cost_increase
    global Rubypickaxe_T
    if ruby>= Rubypickaxe_C:
        ruby-=Rubypickaxe_C
        rubylabel.config(text= 'Ruby= '+str(ruby))
        increment+=200
        Rubypickaxe_C= int(Rubypickaxe_C*cost_increase)
        rubypickaxe_L_C.config(text='Cost= '+ str(Rubypickaxe_C))
        Rubypickaxe_T+=1
        rubypickaxe_L.config(text=Rubypickaxe_T)
        canvas.create_image(1060,425, image=newimage29)

def voidpickaxe_F():
    global void
    global Voidpickaxe_C
    global increment
    global cost_increase
    global Voidpickaxe_T
    if void>= Voidpickaxe_C:
        void-=Voidpickaxe_C
        voidlabel.config(text= 'Void= '+str(void))
        increment+=1000
        Voidpickaxe_C= int(Voidpickaxe_C*cost_increase)
        voidpickaxe_L_C.config(text='Cost= '+ str(Voidpickaxe_C))
        Voidpickaxe_T+=1
        voidpickaxe_L.config(text=Voidpickaxe_T)
        canvas.create_image(1180,425, image=newimage30)

def miningdrill_F():
    global imperium
    global Miningdrill_C
    global increment
    global cost_increase
    global Miningdrill_T
    if imperium>= Miningdrill_C:
        imperium-=Miningdrill_C
        imperiumlabel.config(text= 'Imperium= '+str(imperium))
        increment+=4000
        Miningdrill_C= int(Miningdrill_C*cost_increase)
        miningdrill_L_C.config(text='Cost= '+ str(Miningdrill_C))
        Miningdrill_T+=1
        miningdrill_L.config(text=Miningdrill_T)
        canvas.create_image(1300,425, image=newimage31)

#Defining the function of robots

def starterrobot_F():
    global gold
    global Starterrobot_C
    global increment
    global cost_increase
    global Starterrobot_T
    if gold>= Starterrobot_C:
        gold-=Starterrobot_C
        goldlabel.config(text= 'Gold= '+str(gold))
        Starterrobot_C= int(Starterrobot_C*cost_increase)
        starterrobot_L_C.config(text='Cost= '+ str(Starterrobot_C))
        Starterrobot_T+=1
        starterrobot_L.config(text=Starterrobot_T)
        increment+=10*Starterrobot_T
        canvas.create_image(1060,325, image=newimage22)

def prorobot_F():
    global emerald
    global Prorobot_C
    global increment
    global cost_increase
    global Prorobot_T
    if emerald>= Prorobot_C:
        emerald-=Prorobot_C
        emeraldlabel.config(text= 'Emerald= '+str(emerald))
        Prorobot_C= int(Prorobot_C*cost_increase)
        prorobot_L_C.config(text='Cost= '+ str(Prorobot_C))
        Prorobot_T+=1
        prorobot_L.config(text=Prorobot_T)
        increment+=40*Prorobot_T
        canvas.create_image(1300,325, image=newimage23)

def legendaryrobot_F():
    global diamond
    global Legendaryrobot_C
    global increment
    global cost_increase
    global Legendaryrobot_T
    if diamond>= Legendaryrobot_C:
        diamond-=Legendaryrobot_C
        diamondlabel.config(text= 'Diamond= '+str(diamond))
        Legendaryrobot_C= int(Legendaryrobot_C*cost_increase)
        legendaryrobot_L_C.config(text='Cost= '+ str(Legendaryrobot_C))
        Legendaryrobot_T+=1
        legendaryrobot_L.config(text=Legendaryrobot_T)
        increment+=200*Legendaryrobot_C
        canvas.create_image(1180,575, image=newimage24)


#Creating all the buttons to be used

#Mining button

btn=Button(game, text='', image = newimage, command=mine)
btn.place(x=420,y=100)


#Tools' Buttons

btn1= Button(game, text='', image=newimage12, command= stonepickaxe_F)
btn1.place(x=420,y=630)

btn2= Button(game, text='', image=newimage13, command= flamethrower_F)
btn2.place(x=560,y=630)

btn3= Button(game, text='', image=newimage14, command= sledgehammer_F)
btn3.place(x=700,y=630)

btn4= Button(game, text='', image=newimage15, command= jackhammer_F)
btn4.place(x=840,y=630)

btn5= Button(game, text='', image=newimage16, command= rubypickaxe_F)
btn5.place(x=980,y=630)

btn6= Button(game, text='', image=newimage17, command= voidpickaxe_F)
btn6.place(x=1120,y=630)

btn7= Button(game, text='', image=newimage18, command= miningdrill_F)
btn7.place(x=1260,y=630)


#Robots' Buttons

btn8= Button(game, text='', image=newimage19, command= starterrobot_F)
btn8.place(x=100,y=635)

btn9= Button(game, text='', image=newimage20, command= prorobot_F)
btn9.place(x=100,y=730)

btn10= Button(game, text='', image=newimage21, command= legendaryrobot_F)
btn10.place(x=100,y=825)


#Closing the Tkinter window

game.mainloop()