#!/usr/bin/env python3
# get the json
"""
wget https://static.alta3.com/files/ciscoAPIC.json -O ciscoAPIC.json
"""

"""parsing json"""
import json

def main():
    with open("ciscoAPIC.json", "r") as jsonfile:
        fog = json.load(jsonfile)
        print("The number of instances: ", len(fog['imdata']))
        for instances in fog['imdata']:
            print("Firmware version running - ", instances.get('firmwareCtrlrRunning')\
              .get('attributes').get('version'))

main()

