from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
from pmk import PMK
import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

hardware = Hardware()
pmk = PMK(hardware)
keys = pmk.keys
pmk.rotate(180)
cc = ConsumerControl(usb_hid.devices)

muted = False
prev_pressed = False  # Track previous state of key 4

while True:
    pmk.update()

    # LED status updates
    keys[4].set_led(250, 0, 0) if muted else keys[4].set_led(0, 0, 250)

    # Detect key 4 press (mute toggle)
    if keys[4].pressed and not prev_pressed:
        muted = not muted
        cc.send(ConsumerControlCode.MUTE)

    prev_pressed = keys[4].pressed

    # Fix key 0 press detection alonf with 1 and 5
    if keys[0].pressed:
        keys[0].set_led(250, 0, 0)
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    else:
        keys[0].set_led(224, 192, 121)
    
    
    if keys[1].pressed:
        keys[1].set_led(250, 0, 0)
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    else:
        keys[1].set_led(224, 192, 121)
        
        
    if keys[5].pressed:
        keys[5].set_led(250, 0, 0)
        cc.send(ConsumerControlCode.PLAY_PAUSE)
    else:
        keys[5].set_led(224, 192, 121)
    


    time.sleep(0.05)

