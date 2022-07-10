#this is for the module
import tkinter as tk
from tkinter import *

x_len=0
y_len=0
screen_x=0
screen_y=0
pixel_x=0
pixel_y=0
framec=0

pixels=[]
sprites=[]
backgrounds=[]
list1=[]
list2=[]
list3=[]

class Pixel():
 def __init__(self, window_name, color, pixel_name):
  self.window_name=window_name
  self.color=color
  self.pixel_name=pixel_name
 def stamp(self):
  tk.canvas.itemconfigure(self.pixel_name, fill=self.color) 
 
class Sprite():
 def __init__(self, x, y, size, sprite):
  self.x=x
  self.y=y
  self.size=size
  self.sprite=sprite
  sprites.append(self)
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for i in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or sprite_y>pixel_y-1:
    break
   if self.sprite[i]=='n':
    current_x=sprite_x
    current_y+=self.size
    continue
   if self.sprite[i]==0:
    current_x+=self.size
    continue
   if current_x>pixel_x-1 or current_x<0 or current_y>pixel_y-1 or current_y<0:
    current_x+=1
    continue
   for q in range(self.size):
    for b in range(self.size-1):
     if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
      pixels[current_y*pixel_x+current_x].color=self.sprite[i]
      pixels[current_y*pixel_x+current_x].stamp()
     current_x+=1
    if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
     pixels[current_y*pixel_x+current_x].color=self.sprite[i]
     pixels[current_y*pixel_x+current_x].stamp()
    current_y+=1
    current_x-=self.size-1
   current_y-=self.size
   current_x+=self.size
 def unrender(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for i in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or sprite_y>pixel_y-1:
    break
   if self.sprite[i]=='n':
    current_x=sprite_x
    current_y+=self.size
    continue
   if self.sprite[i]==0:
    current_x+=self.size
    continue
   if current_x>pixel_x-1 or current_x<0 or current_y>pixel_y-1 or current_y<0:
    current_x+=1
    continue
   for q in range(self.size):
    for b in range(self.size-1):
     if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
      try:
       pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
       pixels[current_y*pixel_x+current_x].stamp()
      except:
       pixels[current_y*pixel_x+current_x].color='black'
       pixels[current_y*pixel_x+current_x].stamp()
     current_x+=1
    if current_x<pixel_x-1 and current_x>0 and current_y<pixel_y-1 and current_y>0:
     try:
      pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
      pixels[current_y*pixel_x+current_x].stamp()
     except:
      pixels[current_y*pixel_x+current_x].color='black'
      pixels[current_y*pixel_x+current_x].stamp()
    current_y+=1
    current_x-=self.size-1
   current_y-=self.size
   current_x+=self.size

class Background():
 def __init__(self, x, y, sprite0, sprite):
  self.x=x
  self.y=y
  self.sprite0=sprite0
  self.sprite=sprite
 def render(self):
  sprite_x=round(self.x)
  sprite_y=round(self.y)
  current_x=sprite_x
  current_y=sprite_y
  for q in range(len(self.sprite)):
   if sprite_x>pixel_x-1 or current_y>pixel_y-1:
    break
   if current_x-sprite_x>self.sprite0-1:
    current_x=sprite_x
    current_y+=1
    try:
     pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
     pixels[current_y*pixel_x+current_x].stamp()
    except:
     pixels[current_y*pixel_x+current_x].color='black'
     pixels[current_y*pixel_x+current_x].stamp()
    current_x+=1
    continue
   if current_x>pixel_x-1 or current_y<0:
    current_x=sprite_x
    current_y+=1
   if current_x<0:
    current_x=0
    continue
   try:
     pixels[current_y*pixel_x+current_x].color=backgrounds[0].sprite[current_x-backgrounds[0].x+((current_y-backgrounds[0].y)*backgrounds[0].sprite0)]
     pixels[current_y*pixel_x+current_x].stamp()
   except:
     pixels[current_y*pixel_x+current_x].color='black'
     pixels[current_y*pixel_x+current_x].stamp()
   current_x+=1

def qdee(window_name, scrn_x, scrn_y, pixl_x, pixl_y):
 global x_len
 global y_len
 global pixel_x
 global pixel_y
 global screen_x
 global screen_y
 screen_x=scrn_x
 screen_y=scrn_y
 pixel_x=pixl_x
 pixel_y=pixl_y
 x_len=screen_x/pixel_x
 y_len=screen_y/pixel_y
 pixels.clear()
 tk.canvas=Canvas(window_name, height=screen_y, width=screen_x)
 tk.canvas.pack(fill=BOTH)
 for i in range(pixel_y):
  for q in range(pixel_x):
   pixel_name=str(q)+'-'+str(i)
   pixel_name=tk.canvas.create_rectangle(q*x_len, screen_y-(i*y_len), q*x_len+x_len, screen_y-(i*y_len-y_len), fill = 'black', width = 0) 
   pixel_name=Pixel(window_name, '#000000', pixel_name)
   pixel_name.stamp()
   pixels.append(pixel_name)
 background=Background(0,0,pixel_x, '#000000')
 backgrounds.clear()
 backgrounds.append(background)

def adsprite(sprite_name, x, y, sprite):
 sprite_name=Sprite(x, y, sprite)
 sprites.append(sprite_name)
 
def adbackground(x, y, sprite0, sprite):
 for i in range(len(backgrounds)):
  backgrounds[0].x=x
  backgrounds[0].y=y
  backgrounds[0].sprite0=sprite0
  backgrounds[0].sprite=sprite
  break

def render_scene():
 for whocares in range(len(backgrounds)):
  backgrounds[0].render()
  break
 for i in range(len(sprites)):
  sprites[i-1].render()

def destroy():
 pixels.clear()

def wait(time, function):
 global list
 list1.append(time)
 list2.append(function)
 list3.append(framec)
 

def frame_count():
 global framec
 framec+=1
 for i in range(len(list1)):
  if framec==list3[i-1]+list1[i-1]:
   list2[i-1]()
 

#sprite.render()
#sprite.unrender()
#background.render()
#pixel.render()
  
#ok done
import random

window=tk.Tk()
window.title('Ai birb')
window.configure(bg='#FFFFFF')
window.geometry("768x720+0+0")

is_dead=0

class AI():
 def __init__(self):
  self.points=0
  self.dead=False
 
  self.birbvy=0
  self.birby=60
  
  self.vara=random.randint(0,120)
  self.varb=random.randint(-50,50)
  
  self.varx=random.randint(0,120)
  self.vary=random.randint(-50,50)
  
  self.varw=random.randint(0,120)
  self.varv=random.randint(-50,50)
  
  self.varp=random.randint(0,120)
  self.varq=random.randint(-50,50)

  self.weight_list=[]

 def jump(self):
  self.birbvy=3.5

 def gameloop(self): 
  if self.dead==False:
   self.random_number=random.randint(0,60)
 
   self.weight_list.clear()
   self.weight_list.append(self.varb-(abs(self.birby-self.vara))+self.vary-(abs(self.random_number-self.varx)))
   self.weight_list.append(self.varv-(abs(self.birby-self.varw))+self.varq-(abs(self.random_number-self.varp)))
   self.weight_list.sort()
   if self.weight_list[-1]==self.varb-(abs(self.birby-self.vara))+self.vary-(abs(self.random_number-self.varx)):
    self.jump()
  
   self.points+=1
   self.birbvy-=0.2
   self.birby+=self.birbvy
   
   birb.unrender()
   birb.y=self.birby
   birb.render()
   
   
   if self.birby<24 or self.birby>95:
    self.birbvy=0
    self.birby=60
    self.points-=10
    self.dead=True
    global is_dead
    is_dead+=1
    print(is_dead)

bot_amount=100
bots=[]
for i in range(bot_amount):
 bot=AI()
 bots.append(bot)


true_bot=AI()
true_bot.vara=15
true_bot.varb=12
true_bot.varx=84
true_bot.vary=-32
true_bot.varw=116
true_bot.varv=-26
true_bot.varp=29
true_bot.varq=19


def sortFunc(e):
 return e.points

frames=0

qdee(window, 768, 720, 128, 120)
birb=Sprite(58, 60, 1, (0, 0, 0, 'yellow', 'yellow', 'yellow', 'n', 0, 0, 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'n', 0, 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'orange', 'orange', 'n', 'yellow', 'yellow', 'yellow', 'yellow', 'black', 'black', 'yellow', 'orange', 'n', 0, 0, 'yellow', 'yellow', 'white', 'black', 'yellow', 'n', 0, 0, 0, 'yellow', 'yellow', 'yellow'))
pipe=Sprite(55, 0, 1, (0, -4, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 'light green', 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 'green', 'green', 'black', 'black', 'black', 0, 0, 0, 0, 0, 0, 'black', 'black', 'white', 'green', 'green', 'n', 'green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'white', 'light green', 'green', 'n', 'green', 'light green', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'light green', 'green', 'n', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'n', 'green', 'light green', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'light green', 'green', 'n', 'green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'light green', 'white', 'light green', 'green', 'n', 'green', 'green', 'black', 'black', 'black', 0, 0, 0, 0, 0, 0, 'black', 'black', 'white', 'green', 'green', 'n', 0, 0, 'green', 'light green', 'light green', 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green', 'n', 0, 0, 'green', 'light green', 0, 0, 0, 0, 0, 0, 'light green', 'white', 'light green', 'green'))
render_scene()

while True:
 true_bot.gameloop()
 """
 frames+=1
 for i in range(bot_amount):
  bots[i].gameloop()
 if is_dead==bot_amount:
  bots.sort(key=sortFunc)
  frames=0
  print(bots[-1].points)
  print(bots[-1].vara)
  print(bots[-1].varb)
  print(bots[-1].varx)
  print(bots[-1].vary)
  print(bots[-1].varw)
  print(bots[-1].varv)
  print(bots[-1].varp)
  print(bots[-1].varq)
  for i in range(bot_amount-10):
   competitor=random.randint(-10,-1)
   bots[i].vara=bots[competitor].vara+random.randint(-10,10)
   bots[i].varb=bots[competitor].varb+random.randint(-10,10)
   bots[i].varx=bots[competitor].varx+random.randint(-10,10)
   bots[i].vary=bots[competitor].vary+random.randint(-10,10)
   bots[i].varw=bots[competitor].varw+random.randint(-10,10)
   bots[i].varv=bots[competitor].varv+random.randint(-10,10)
   bots[i].varw=bots[competitor].varp+random.randint(-10,10)
   bots[i].varv=bots[competitor].varq+random.randint(-10,10)
  for i in range(bot_amount):
   bots[i].points=0
   bots[i].dead=False
  is_dead=0
 if frames==100000:
  for i in range(bot_amount):
   if bots[i].dead==False:
    print("It's getting fucking long")
    print(bots[i].points)
    print(bots[i].vara)
    print(bots[i].varb)
    print(bots[i].varx)
    print(bots[i].vary)
    print(bots[i].varw)
    print(bots[i].varv)
    print(bots[i].varp)
    print(bots[i].varq)
    frames=0
    break
  """
 window.update()
