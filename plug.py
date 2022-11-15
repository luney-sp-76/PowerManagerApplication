import json
import time
import api
import create_plug_object


#   https://www.zigbee2mqtt.io/devices/SPLZB-134.html

def get_response():
    return api.get_state(api.url_plug_state).text


def print_api_response():
    # create a dict from the response
    api_response = json.loads(get_response())
    # print the response
    print("Rest API Response\n")
    for responding in api_response:
        print(responding, api_response[responding])


#  small script to switch the plug on or off and return a state
api.call_plug(api.url_plug_turn_on)
time.sleep(20)
print(create_plug_object.plug())
time.sleep(10)
api.call_plug(api.url_plug_turn_off)
time.sleep(10)
print(create_plug_object.plug())
api.call_plug(api.url_plug_toggle)
time.sleep(10)
print(create_plug_object.plug())
