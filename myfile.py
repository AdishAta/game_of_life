from tkinter import * 
from time import sleep 
from random import randint, choice 
import tkinter 
from turtle import heading 
 
 
 
class Space: 
    def __init__(self, c, n, m, width, height, walls=False): 
        self.c = c 
        self.a = [] 
        self.n = n + 2 
        self.m = m + 2 
        self.width = width 
        self.height = height 
        self.count = 0 
        for i in range(self.n): 
            self.a.append([])   
            for j in range(self.m):
                if randint(1,7) == 4:
                    self.a.append(10)
                elif randint(1,3) == 2:
                    self.a.append(1)
                else:
                    self.a.append(0) 
        self.draw() 
 
         
    def step(self): 
        b = [] 
        for i in range(self.n):  
            b.append([]) 
            for j in range(self.m): 
                b[i].append(0) 
                
        for i in range(1, self.n - 1):     #№1 Human VS Alien
            for j in range(1, self.m - 1): 
                neib_sum =  self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                humans = int(str(neib_sum)[1])
                aliens = int(str(neib_sum)[0])
                print(humans, aliens)
                if humans > aliens: #if amount of aliens is bigger
                    if self.a[i][j] == 1:   #if the current cell is human
                        if randint(1,3) == 1:   #33% that he'll stay survive
                            self.b[i][j] == 1
                        elif randint(1,5) == 2:     #20% that he'll become an alien
                            self.b[i][j] == 10
                        else:                       #otherwise he dies
                            self.b[i][j] == 0 
                elif aliens > humans:
                    if self.a[i][j] == 10:                         
                        if randint(1,2) == 1:
                            self.b[i][j] = 0
                        else:
                            self.b[i][j] = 10
                if aliens > 2 and self.a[i][j] == 0:
                    if randint(1,3) == 1:
                        self.b[i][j] == 10
                if humans > 1 and self.a[i][j] == 0:
                    self.b[i][j] = 1
                        
        self.a = b 
                     
    def print_field(self): 
        for i in range(self.n): 
            for j in range(self.m): 
                print(self.a[i][j], end="") 
            print() 
  
    def draw(self): 
        
        sizen = self.width // (self.n - 2) 
        sizem = self.height // (self.m - 2) 
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1): 
                    color = "white"  #People
                elif (self.a[i][j] == 2): 
                    color = "purple" #Aliens
                else: 
                    color = "black" 
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color) 
        self.step() 
        self.c.after(100, self.draw) 
 
         
root = tkinter.Tk() 
 
root.geometry("1600x1600") 
c = Canvas(root, width=1600, height=1600) 
c.pack() 
 
f = Space(c, 40, 40, 1600, 1600) 
f.printSpace() 
 
 
root.mainloop()