#!/usr/bin/env /Applications/MAMP/Library/bin/python
import mysql.connector


def connected():
    config = {
        'user': 'poweruser',
        'password': 'A5DVtUB8xE6)@xr',
        'host': 'localhost',
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'database': 'power_manager',
        'raise_on_warnings': True
    }
    connection_x = mysql.connector.connect(**config)
    return connection_x


