from ev3dev.ev3 import *
from time import sleep


class Robot:
  light_left = ColorSensor('in2')
  light_right = ColorSensor('in1')
  touch_sensor = TouchSensor('in4')
  lcd = Screen()

  right_engine = LargeMotor('outB')
  left_engine = LargeMotor('outA')
  
  
  
  def follow_the_line():
    Kp = 4.0
    Kd = 1.0
    predkosc_bazowa = 60.0
    srodek_l = (white_left + black_right) // 2
    srodek_r = (white_right + black_right) // 2
    blad = 0
    poprzedni_blad = 0
    blad_l = 0
    blad_r = 0
    blad_prop = 0.0
    blad_deri = 0.0

    while not touch_sensor.is_pressed:
      blad_l = light_left.reflected_light_intensity - srodek_l
      blad_r = light_right.reflected_light_intensity - srodek_r
      blad = blad_l - blad_r
      blad_prop = Kp * float(blad)
      blad_deri = Kd * (blad - poprzedni_blad)
      left_engine.run_timed(time_sp = 100, speed_sp = -predkosc_bazowa - blad_prop + blad_deri, stop_action = "coast")
      right_engine.run_timed(time_sp = 100, speed_sp = -predkosc_bazowa + blad_prop - blad_deri, stop_action = "coast")
      poprzedni_blad = blad
  
