import json
from collections import namedtuple

import api


#  create a light object using namedTuple
def custom_plug_decoder(plugdict):
    return namedtuple('x', plugdict.keys())(*plugdict.values())


def get_plug_response():
    return api.get_state(api.url_plug_state).text


def remove(string):
    """
    :param string: to be split with spaces filled with an underscore
    :return: list with no spaces
    """
    new_string = "_".join(string.split(" "))
    return new_string


def get_plug_charge_state():
    result = get_plug_response()
    new_response = remove(result)
    return_response = json.loads(new_response, object_hook=custom_plug_decoder)
    return return_response


response = get_plug_charge_state()


def get_plug_attributes():
    return getattr(response, 'attributes')


def get_plug_id():
    context = getattr(response, 'context')
    return context[0]


def get_entity_id():
    return response[0]


def get_state():
    return response[1]


def get_friendly_name():
    attributes = get_plug_attributes()
    return attributes[0]


def last_changed():
    return response[3]


def last_updated():
    return response[4]


# print("Plug data is " + get_plug_response() + "%")
# time.sleep(5)
# plug_attributes = get_plug_attributes()
# print(get_plug_attributes())
# print("Entity id: ")
# entity_id = get_entity_id()
# print(entity_id + " 􀇺")
# print("State: ")
# state = get_state()
# if state == "off":
#     print(state + " 􀡷")
# if state == "on":
#     print(state + " 􀡸")
# print("Friendly Name")
# friendly_name = get_friendly_name()
# print(friendly_name + " 􀎸")
# print("Last Changed: ")
# last_changed = last_changed()
# print(last_changed + "  􀐱")
# print("Last Updated: ")
# last_updated = last_updated()
# print(last_updated + "  􀐱")
# context_id = get_plug_id()
# print("Context id: ")
# print(context_id + " 􀇺")
