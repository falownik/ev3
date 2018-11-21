from ev3dev.ev3 import *
from time import sleep


class Robot:
  light_left = ColorSensor('in2')
  light_right = ColorSensor('in1')
  touch_sensor = TouchSensor('in4')
  lcd = Screen()

  right_engine = LargeMotor('outB')
  left_engine = LargeMotor('outA')
  
    #parametry PD
    Kp = 4.0
    Kd = 1.0
    base_speed = 60.0
    mid_l = (white_left + black_right) // 2
    mid_r = (white_right + black_right) // 2
    blad = 0
    last_error = 0
    error_l = 0
    error_r = 0
    error_P = 0.0
    error_D = 0.0
    
    
  def follow_the_line():

    while not touch_sensor.is_pressed:
      error_l = light_left.reflected_light_intensity - mid_l
      error_r = light_right.reflected_light_intensity - mid_r
      error = error_l - error_r
      error_P = Kp * float(error)
      error_D = Kd * (error - last_error)
      left_engine.run_timed(time_sp = 100, speed_sp = -base_speed - error_P + error_D, stop_action = "coast")
      right_engine.run_timed(time_sp = 100, speed_sp = -base_speed + error_P - error_D, stop_action = "coast")
      last_error = error
  
  def turn(direction, degree):
     q = 10 %% time factor
     if direction is 'right':
        dir = 1
     else if direction is 'left':
        dir = -1
     else 
        %% raise exception
        left_engine.run_timed (time_sp = degree*q, speed_sp = -300*dir)
        right_engine.run_timed(time_sp = degree*q, speed_sp = 300*dir)
