from machine import Pin, PWM, ADC
from time import sleep

throttleKnob = ADC(Pin(26))
steeringKnob = ADC(Pin(27))
throttleOut = PWM(Pin(0))
steeringOut = PWM(Pin(4))

throttleOut.freq(50)
steeringOut.freq(300)

in_min = 200
in_max = 65350
throttleOut_min = 1000000
throttleOut_max = 2000000
steeringOut_min = 500000
steeringOut_max = 2500000

def rangeMap(x, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

while True:
    throttleVal = throttleKnob.read_u16()
    steeringVal = steeringKnob.read_u16()

    throttle = rangeMap(throttleVal, throttleOut_min, throttleOut_max)
    steering = rangeMap(steeringVal, steeringOut_min, steeringOut_max)

    if 1470000 < int(throttle) < 1530000:
        throttle = 1500000

    if 1470000 < int(steering) < 1530000:
        steering = 1500000

    throttleOut.duty_ns(int(throttle))
    steeringOut.duty_ns(int(steering))

    #print('Throttle: ', str(int(throttleOut.duty_ns()/1000)), ' Steering: ', str(int(steeringOut.duty_ns()/1000)))

    sleep(0.02)

 

    
