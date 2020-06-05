# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:38:25 2020

@author: Milan Vishnoi
"""
from random import randint

def printnumpad(lst):
  print(" {} | {} | {}".format(lst[0],lst[1],lst[2]))
  print("------------")
  print(" {} | {} | {}".format(lst[3],lst[4],lst[5]))
  print("------------")
  print(" {} | {} | {}".format(lst[6],lst[7],lst[8]))
def displaypos():
  printnumpad([1,2,3,4,5,6,7,8,9])
def initialize(lst):
  lst=[" "]*9 
  return lst
def assignmarker():
  dit={}
  name1=input("Enter Player1 name : ")
  symbol1=input("Enter {}'s symbol : ".format(name1)).upper()
  while(symbol1!="X" and symbol1!='O'):
    print("You have entered wrong symbol, please only from X and O !!")
    symbol1=input("Enter {}'s symbol : ".format(name1)).upper()
  dit[symbol1]=name1
  name2=input("Enter Player2 name : ")
  symbol2=input("Enter {}'s symbol : ".format(name2)).upper()
  while((symbol2!="X" and symbol2!='O') or symbol2==symbol1):
    if(symbol2==symbol1):
      print("Already taken !!")
    else:
      print("You have entered wrong symbol, please only from X and O !!")
    symbol2=input("Enter {}'s symbol : ".format(name2)).upper()
  dit[symbol2]=name2
  return dit    
def check(lst):
  #positions at which we need to check for winning
  hor1=list({lst[0],lst[1],lst[2]})  
  hor2=list({lst[3],lst[4],lst[5]})
  hor3=list({lst[6],lst[7],lst[8]})
  ver1=list({lst[0],lst[3],lst[6]})
  ver2=list({lst[1],lst[4],lst[7]})
  ver3=list({lst[2],lst[5],lst[8]})
  dia1=list({lst[0],lst[4],lst[8]})
  dia2=list({lst[2],lst[4],lst[6]})
  winpos=[hor1,hor2,hor3,ver1,ver2,ver3,dia1,dia2]
  for item in winpos:
    if len(item)==1:
      if item[0]=="X" or item[0]=="O":
        return item[0]
  return False       
def validmove(lst,pos):
  if pos>8:
    print("Invalid position !!")
    return False
  elif lst[pos]==" ":
    return True
  else :
    print("This position is already taken !!")
    return False  
def play(lst,dit,s1,s2):
  while(True):
    pos1=int(input("{} enter the position : ".format(dit[s1])))
    pos1=pos1-1
    while(not(validmove(lst,pos1))):
      pos1=int(input("{} enter the right position : ".format(dit[s1])))
    lst[pos1]=s1
    printnumpad(lst)
    if check(lst):
      print("--Congratulations {} !! You won!!--".format(dit[s1]))
      break
    if lst.count(" ")==0:
      print("Game drawn !!")
      break  
    pos2=int(input("{} enter the position : ".format(dit[s2])))
    pos2=pos2-1
    while(not(validmove(lst,pos2))):
      pos2=int(input("{} enter the right position : ".format(dit[s2])))
    lst[pos2]=s2
    printnumpad(lst)
    if check(lst):
      print("--Congratulations {} !! You won!!--".format(dit[s2]))
      break
    if lst.count(" ")==0:
      print("Game drawn !!")
      break  
def start():
  lst=[]
  lst=initialize(lst)
  dit=assignmarker()
  s1=list(dit.keys())[0]
  s2=list(dit.keys())[1]
  print("{}'s symbol is {} and {}'s symbol is {}".format(dit[s1],s1,dit[s2],s2))
  print("The positions are as follows : ")
  displaypos()
  print("You have to enter the position number to play !!")
  chance=randint(1,2)
  if chance==1:
    print("--{} will play first move--".format(dit[s1]))
    play(lst,dit,s1,s2)
  else:
    print("--{} will play first move--".format(dit[s2]))
    play(lst,dit,s2,s1)
def tictactoe():
  choice="yes"
  while(choice!="no"):
    start()
    print("Want to play again(Yes/No) ??")
    choice=input().lower()

tictactoe()
print("\nThank you so much for playing!!\nSee you again :)")