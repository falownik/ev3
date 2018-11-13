from ev3dev.ev3 import *
import time

m1 = LargeMotor('outA')
m2 = LargeMotor('outD')
cs1 = ColorSensor('in1')
cs2 = ColorSensor('in2')
ts = TouchSensor()

nastawa = 45

integral1 = 0
integral2 = 0

last_error1 = 0
last_error2 = 0

base_vel = -60


while True:

    cs1rli = cs1.reflected_light_intensity
    
    error1 =nastawa -  cs1rli

    integral1 =0.5* integral1 + error1

    derivative1 = error1 - last_error1

    last_error1 = error1

    skret1 = int(0.8*error1  +  18*derivative1)


    if ts.is_pressed:

        m1.run_forever(speed_sp =base_vel -  skret1)
        m2.run_forever(speed_sp =base_vel +  skret1)

        if cs1rli < 10:
            m1.run_forever(speed_sp = -200)
            m2.run_forever(speed_sp = 300)
        if cs1rli > 100:
            m1.run_forever(speed_sp = 300)
            m2.run_forever(speed_sp = -200)

    elif not ts.is_pressed:
        m1.stop()
        m2.stop()
    print("uch 1: " + str(skret1)+ " light reflection: " + str( cs1rli) + " " + str(error1) + " " + str(integral1) + " " + str(derivative1) + str(skret1))
