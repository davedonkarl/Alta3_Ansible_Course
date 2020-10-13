#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
from pprint import pprint as pp # part of the standard libray

## Define APOD 
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=rnaJPpelckDN3rM0139CkMNr3CRgfXuHGH0qumuq'    ## your key goes in place of DEMO_KEY

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.read() # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8')) # convert JSON
    
    # Show converted json
    print(convertedjson) # show convereted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(convertedjson) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(convertedjson['explanation']) # display the value for the key explanation
    print("Link to the APOD:", convertedjson['hdurl'])
    
    
    input('\nPress ENTER to view this photo of the day') # pause for ENTER
    webbrowser.open(convertedjson['hdurl']) # open in the webbrowser

main()