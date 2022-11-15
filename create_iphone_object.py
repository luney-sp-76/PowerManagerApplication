import json
from collections import namedtuple

import api


#  create an iPhone object using namedTuple
def custom_iphone_decoder(aphone):
    return namedtuple('X', aphone.keys())(*aphone.values())


#  get the iphone battery level
def get_iphone_battery_level_response():
    """
    call the method get_state in the api file with the url for iphone battery level from the same file
    :return:
    """
    return api.get_state(api.url_iphone_battery_level).text


#  use the iphone battery level to return the battery percentage
def iphone_battery_level():
    """
     :return a json of the iphone includes state as Charging or Not_Charging, boolean of LOW POWER MODE
    """
    iphone_battery = json.loads(get_iphone_battery_level_response(), object_hook=custom_iphone_decoder)
    status = iphone_battery.state
    return status


#  remove white space in string
def remove(string):
    """
    :param string: to be split with spaces filled with an underscore
    :return: list with no spaces
    """
    new_string = "_".join(string.split(" "))
    return new_string


#  get the iphone charging state
def get_iphone_charge_state_response():
    """
    call the method get_state from the api file with the url for iphone battery state from the same file
    :return: text version of JSON
    """
    return api.get_state(api.url_iphone_battery_state).text


#  use the iphone charging state call to return a state
def iphone_charge_state():
    """
    gets the charge state response and splits it into a list with no spaces then makes an object to be returned
    :return: json object
    """
    aphone_response = get_iphone_charge_state_response()
    anew_response = remove(aphone_response)
    aphone_charge = json.loads(anew_response, object_hook=custom_iphone_decoder)
    return aphone_charge


# print("iPhone Battery charge level is " + iphone_battery_level() + "%")
# print("get_iphone_charge_state_response() returns the json: " + get_iphone_charge_state_response())
# time.sleep(5)
# """
# below is an example or dismantling the tuple into usable info to send to the database
# """
response = iphone_charge_state()


def get_iphone_attributes():
    """
    :return: a list of tuples from the iphone attributes
    """
    return getattr(response, 'attributes')


def get_iphone_id():
    """

    :return: a single String of the iphone id
    """
    context = getattr(response, 'context')
    return context[0]


def get_iphone_entity_id():
    return response[0]


def get_iphone_state():
    return response[1]


def get_charging_attributes():
    charging_attributes = get_iphone_attributes()
    return charging_attributes


def get_battery_icon():
    battery = get_charging_attributes()
    return battery[1]


def get_iphone_friendly_name():
    iphone_name = get_charging_attributes()
    return iphone_name[2]


def is_low_power():
    is_low = get_charging_attributes()
    return is_low[0]


def iphone_last_changed():
    return response[3]


def iphone_last_updated():
    return response[4]


# iphone_battery_charging_attributes = get_iphone_attributes()
# print("Tuple attribute values: ")
# print(get_iphone_attributes())
# print("Entity id: ")
# entity_id = get_iphone_entity_id()
# print(entity_id + " 􀇺")
#
# print("State: ")
# state = get_iphone_state()
# if state == "Not_Charging":
#     print(state + " 􀡷")
# if state == "Charging":
#     print(state + " 􀡸")
#
# print("Battery Icon: ")
# battery_symbol = get_battery_icon()
# print(battery_symbol + " 􀛨")
#
# print("Friendly Name:  ")
# friendly_name = get_iphone_friendly_name()
# print(friendly_name + " 􀎸")
#
# print("is low power Boolean: ")
# is_low_power = is_low_power()
# print(is_low_power)
# if is_low_power:
#     print("Low Power Mode 􀛪")
# else:
#     print("Not Low on Power 􀢋 ")
#
# print("Last Changed: ")
# last_changed = iphone_last_changed()
# print(last_changed + "  􀐱")
# print("Last Updated: ")
# last_updated = iphone_last_updated()
# print(last_updated + "  􀐱")
# context_id = get_iphone_id()
# print("Context id: ")
# print(context_id + " 􀇺")
