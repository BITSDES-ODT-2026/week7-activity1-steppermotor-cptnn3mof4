from machine import Pin
import time

ln1 = Pin(14, Pin.OUT)
ln2 = Pin(4, Pin.OUT)
ln3 = Pin(18, Pin.OUT)
ln4 = Pin(19, Pin.OUT)

while True:
   ln1.value(1)
   ln2.value(1)
   ln3.value(0)
   ln4.value(0)
   time.sleep_ms(50)
   
   ln1.value(0)
   ln2.value(1)
   ln3.value(1)
   ln4.value(0)
   time.sleep_ms(50)
   
   ln1.value(0)
   ln2.value(0)
   ln3.value(1)
   ln4.value(1)
   time.sleep_ms(50)
   
   ln1.value(1)
   ln2.value(0)
   ln3.value(0)
   ln4.value(1)
   time.sleep_ms(50)

