from ev3dev.ev3 import *
from time import sleep

light_left = ColorSensor('in2')
light_right = ColorSensor('in1')
touch_sensor = TouchSensor('in4')
lcd = Screen()

right_engine = LargeMotor('outB')
left_engine = LargeMotor('outA')

white_left = 0
white_right = 0
black_left = 0
black_right = 0


lcd.clear()


while not touch_sensor.is_pressed:
    black_left = light_left.reflected_light_intensity
    black_right = light_right.reflected_light_intensity
print("black left:"+str(black_left)+"\n"+"black right:"+str(black_right))
lcd.draw.text((48,13),"black left:"+str(black_left)+"\n"+"black right:"+str(black_right))
lcd.update()
while touch_sensor.is_pressed:
    continue
lcd.clear()
while not touch_sensor.is_pressed:
    white_left = light_left.reflected_light_intensity
    white_right = light_right.reflected_light_intensity
print("white left:"+str(white_left)+"\nwhite right:"+str(white_right))
lcd.draw.text((48,13),"white left:"+str(white_left)+"\nwhite right:"+str(white_right))
lcd.update()
while touch_sensor.is_pressed:
    continue
lcd.clear()
lcd.draw.text((48,13),"wcisnij przycisk aby wystartowac")
lcd.update()
while not touch_sensor.is_pressed:
    continue
while touch_sensor.is_pressed:
    continue
lcd.clear()
lcd.draw.text((48,13),"wcisnij przycisk aby zakonczyc dzialanie programu")
lcd.update()

Kp = 4.0
Kd = 1.0
predkosc_bazowa = 150.0
srodek_l = (white_left + black_right) // 2
srodek_r = (white_right + black_right) // 2
blad = 0
poprzedni_blad = 0
blad_l = 0
blad_r = 0
blad_prop = 0.0
blad_deri = 0.0

while not touch_senor.is_pressed:
    blad_l = light_left.reflected_light_intensity - srodek_l
    blad_r = light_right.reflected_light_intensity - srodek_r
    blad = blad_l - blad_r
    blad_prop = Kp * float(blad)
    blad_deri = Kd * (blad - poprzedni_blad)
    left_engine.run_timed(time_sp = 100, speed_sp = -predkosc_bazowa - blad_prop + blad_deri, stop_action = "coast")
    right_engine.run_timed(time_sp = 100, speed_sp = -predkosc_bazowa + blad_prop - blad_deri, stop_action = "coast")
    poprzedni_blad = blad
    sleep(0.1)

lcd.clear()
print("to jest juz koniec")
lcd.draw.text((48,13),"koniec dzialania programu")
lcd.update()
