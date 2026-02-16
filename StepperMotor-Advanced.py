from machine import Pin
import time

ln1 = Pin(14, Pin.OUT)
ln2 = Pin(4, Pin.OUT)
ln3 = Pin(18, Pin.OUT)
ln4 = Pin(19, Pin.OUT)

list = [[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1],[1,0,0,0]]

while True:
    for i in list:
        print(i)
        ln1.value(i[0])
        time.sleep_ms(50)
        ln2.value(i[1])
        time.sleep_ms(50)
        ln3.value(i[2])
        time.sleep_ms(50)
        ln4.value(i[3])
        time.sleep_ms(50)
