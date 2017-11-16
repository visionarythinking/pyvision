# baeume.py
# Wald mit Bäumen
from turtle import *
from random import random
 
def baum(a):
   for i in range(1,3):
       color("brown")
       begin_fill()
       forward(a); left(90)
       forward(2*a); left(90)
       end_fill()
   up(); left(90); forward(2*a); left(90); forward(a); left(180); down()
   color("darkgreen")
   begin_fill()
   forward(3*a); left(110)
   forward(4.39*a); left(140); forward(4.39*a); left(110)
   end_fill()
   up(); forward(a); right(90); forward(2*a); left(90); down()
 
speed(0)      # max. Zeichengeschwindigkeit
up(); backward(220); left(90); forward(220); right(90); down()
# Turtle im Windwows-Fenster nach links oben setzen
a=8 # Breite Baumstamm
anzahl_x = 12  # Anzahl der Bäume in x-Richtung
anzahl_y = 8   # Anzahl der Baumreihen in y-Richtung
for j in range(1,anzahl_y+1):
  for i in range(1,anzahl_x+1):
    baum(a); up(); forward((0.5+random())*5*a); down()
  up(); backward(anzahl_x*5*a); right(90); forward(8*a); left(90); down()
