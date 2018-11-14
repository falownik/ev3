from ev3dev.ev3 import *
import time

m1 = LargeMotor('outA')
m2 = LargeMotor('outD')
cs1 = ColorSensor('in1')
cs2 = ColorSensor('in2')
ts = TouchSensor()

nastawa = 0

integral = 0

last_error = 0

base_vel = -60

while not ts.is_pressed:

  nastawa = cs1.reflected_light_intensity
  
while True:

    cs1r = cs1.reflected_light_intensity
    
    error = nastawa -  cs1r

    integral =0.5* integral + error

    derivative = error - last_error

    last_error = error

    skret = int(0.8*error  +  18*derivative)
    time.sleep(0.1)


    if ts.is_pressed:

        m1.run_forever(speed_sp =base_vel -  skret)
        m2.run_forever(speed_sp =base_vel +  skret)

        if cs1r < 10:
            m1.run_forever(speed_sp = -200)
            m2.run_forever(speed_sp = 300)
        if cs1r > 100:
            m1.run_forever(speed_sp = 300)
            m2.run_forever(speed_sp = -200)

    elif not ts.is_pressed:
        m1.stop()
        m2.stop()
    print("uch 1: " + str(skret)+ " light reflection: " + str( cs1r) + " " + str(error) + " " + str(integral) + " " + str(derivative) + str(skret))
