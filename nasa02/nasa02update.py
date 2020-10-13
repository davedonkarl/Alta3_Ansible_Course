#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=rnaJPpelckDN3rM0139CkMNr3CRgfXuHGH0qumuq' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

"""
CODE CUSTOMIZATION 01 - Make the program accept a start date from a user and (optionally) end parameter.

CODE CUSTOMIZATION 02 - Create a function that expects a parameter of the missdistance in miles and returns the number of 'moon lengths' away that body is. A 'moon length' = 238,900 miles. Use this new function to display this additional data to the user.

CODE CUSTOMIZATION 03 - That's a LOT of data to work with! Make your program do something with it! Here are some ideas (or find your own). Ideally, create function(s) to perform your task(s).

Display to the user how many total NEOs are being tracked.
Display to the user which NEO is closest to earth.
Return any NEOs that are marked "is_potentially_hazardous_asteroid" : True
"""
