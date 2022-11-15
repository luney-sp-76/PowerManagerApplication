from jproperties import Properties
from requests import get, post

# home assistant long-lived authorization token
configs = Properties()
with open('api.properties', 'rb') as config_file:
    configs.load(config_file)

items_view = configs.items()
list_keys = []

for item in items_view:
    list_keys.append(item[0])

db_configs_dict = {}

for item in items_view:
    db_configs_dict[item[0]] = item[1].data

# {'DB_HOST': 'localhost', 'DB_SCHEMA': 'Test', 'DB_User': 'root', 'DB_PWD': 'root@neon'}
# ['DB_HOST', 'DB_SCHEMA', 'DB_User', 'DB_PWD']
#  homeassistant url endpoints
url_plug_state = "http://homeassistant.local:8123/api/states/switch.powermanager_kasa"
url_plug_turn_on = "http://homeassistant.local:8123/api/services/switch/turn_on"
url_plug_turn_off = "http://homeassistant.local:8123/api/services/switch/turn_off"
url_plug_toggle = "http://homeassistant.local:8123/api/services/switch/develco/toggle"
url_iphone_battery_state = "http://homeassistant.local:8123/api/states/sensor.iphone_battery_state"
url_iphone_battery_level = "http://homeassistant.local:8123/api/states/sensor.iphone_battery_level"

# bearer = auth.bearer()
bearer = db_configs_dict['bearer']


def call_plug(url):
    mydata = '{"entity_id": "switch.powermanager_kasa"}'

    headers = {
        "Authorization": bearer,
        "content-type": "application/json",
        "payload": mydata,
    }

    response = post(url, headers=headers, data=mydata)
    return response


def get_state(url):
    headers = {
        "Authorization": bearer,
        "content-type": "application/json",
    }
    response = get(url, headers=headers)
    return response
