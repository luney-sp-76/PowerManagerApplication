#  First if the battery is charging and the battery power is over 50% and less than 100% turn off the plug
import json
import re
import time
import api
from create_iphone_object import iphone_battery_level, get_iphone_state
from create_plug_object import get_state, get_friendly_name

print("iPhone Battery charge level is " + iphone_battery_level() + "%")
#  create an iphone and check the iphone charge state (on charge or not on charge)

iphone_charge = iphone_battery_level()
phone_charging_state = get_iphone_state()

iphone_is_charging = api.get_state(api.url_iphone_battery_state)

#  check the iphone battery charge level (this needs mapped from string to integer to allow number value comparisons
iphone_battery_nums = list(map(int, re.findall('\d+', iphone_battery_level())))
iphone_battery_level = iphone_battery_nums[0]

time.sleep(20)

#  if iPhone on charge and the charge level is lower than 100% and higher than 50%
if iphone_battery_level >= 80:
    #  if the plug state is on and the phone is charging
    if get_state() == 'on' and phone_charging_state == "Charging":
        print("Your phone is currently over 60%")
        api.call_plug(api.url_plug_turn_off)
        time.sleep(30)
        print(get_friendly_name() + " is now off 􀡷")
        state = 'off'
        time.sleep(20)
        if state == 'off' and phone_charging_state == "Charging":
            print("Your phone is currently below 60% and is on charge but not on the smart plug")
            time.sleep(20)
            print(get_friendly_name() + " is now off 􀡷")
    else:
        print("Your phone is currently over 60%")
        time.sleep(20)
        print(get_friendly_name() + " is now off 􀡷")
else:
    if get_state() == 'off' and phone_charging_state == "Not_Charging":
        print("Your phone is currently below 60% and is not on charge")
        time.sleep(20)
        api.call_plug(api.url_plug_turn_on)
        print("Switching the plug on...")
        time.sleep(30)
        print(get_friendly_name() + " is now on 􀡸")
        state = 'on'
        time.sleep(20)
        if state == 'on' and phone_charging_state == "Not_Charging":
            print("Your phone is currently below 60% and is not on charge on this plug")
            print("Switching the plug off...")
            time.sleep(20)
            api.call_plug(api.url_plug_turn_off)
            time.sleep(30)
            print(get_friendly_name() + " is now off 􀡷")
    if get_state() == 'on' and phone_charging_state == "Not_Charging":
        print("Your phone is currently below 60% and is not on charge on this plug")
        print("Switching the plug off...")
        time.sleep(20)
        api.call_plug(api.url_plug_turn_off)
        time.sleep(30)
        print(get_friendly_name() + " is now off 􀡷")
    else:
        if get_state() == 'on' and phone_charging_state == "Charging":
            print("Your phone is currently below 60% and may be on charge on this smart plug")
            time.sleep(20)
            print(get_friendly_name() + " is now on 􀡸")
