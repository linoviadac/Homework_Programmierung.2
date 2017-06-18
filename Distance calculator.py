
# Programmierung 2
# Pruefungvorleistung Aufgabe
# Luftlinienberechner
# Chen Yuan MAB14 4060920
# 07.06.2017

#------------------------------------------------------------------------
# Import the modules

import re                                                                  # For the searching funktion
import os
import sys
import logging                                                             # For outputing a log file
from math import cos, sin, asin, sqrt, radians

#------------------------------------------------------------------------
# Using the logging module

logging.basicConfig(level=logging.INFO,                                    # Show all the loggings which have higher level than INFO
                    filename='./log.txt',                                  # The log will be saved in a new txt file called log
                    filemode='w',                                          # File right: write
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#------------------------------------------------------------------------
# Print a cut-off rule

def rule():                                                                 # Make it as a funktion so the lenth of all the
    print("-"*80)                                                           # rules and can be easily changed in the sametime

#-------------------------------------------------------------------------
# Search for the cities
# For both start city and end city
# Input city name return the line of the chosen city in the citylist

def find_city ():
    citylist = []                                                           # The cities you might choose
    citylist_PLZ = []                                                       # The cities which have PLZ that you might choose
    cities = open("DE.tab",encoding="utf-8").readlines()
    logging.info('The positon file has been opened.')                       # Log information
    while len(citylist) == 0 :                                              # Always ask for input if there is no city added to the citylist
        logging.info('There is no city has been added to the citylist yet.')# Log information
        city = input("Please give the name of the city.\n").upper()
        city = city.replace('Ä', 'AE')                                      # Umlauts conversion
        city = city.replace('Ö', 'OE')                                      # Umlauts conversion
        city = city.replace('Ü', 'UE')                                      # Umlauts conversion
        city = city.replace('ß', 'SS')                                      # Umlauts conversion
        print("You mean one of these cities?")
        print("Name                  PLZ")
        for line in cities :
            if re.search(city,line):                                        # Searching the cityname in each line of the cities Daten
                citylist.append(line.split("\t"))                           # Add the line to citylist if there is cityname in the line
    i=0
    for j in range(len(citylist)):
        if len(citylist[j][7]) != 0:                                        # Checking is there PLZ in the line
            print("%i. %s %s"%(i+1,citylist[j][3],citylist[j][7]))          # Print all the cities which has the name and PLZ
            rule()
            citylist_PLZ.append(citylist[j])                                # Add these cities into the citylist with PLZ
            i=i+1
    choice = int(input("Give the number before the city.\n")) - 1           # Asking for the number of the chosen city and give the number to the 'choice'
    city = citylist_PLZ[choice]                                             # Give the line of the chosen city to the 'city'
    print("You have chosen[",city[3],"]\n")                                 # Chosen city varification
    rule()
    print("\n")
    return city                                                             # Return the line of the chosen city

#-------------------------------------------------------------------------
# Calculation of the airline Distance
# Input longitude and latitude of both cities return airline Distance

def calculation(lon1, lat1, lon2, lat2):
    R = 6371                                                                # Average EARTH R in km

    lat1 = radians(float(lat1))                                             # Trasformation of the latitude of the first ciry from degree system to radian system
    lon1 = radians(float(lon1))                                             # Trasformation of the longitude of the first ciry from degree system to radian system
    lat2 = radians(float(lat2))                                             # Trasformation of the latitude of the seconed ciry from degree system to radian system
    lon2 = radians(float(lon2))                                             # Trasformation of the longitude of the seconed ciry from degree system to radian system

    dlon = lon2-lon1                                                        # The calculation
    dlat = lat2-lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2*asin(sqrt(a))
    return c*R                                                              # Return the result of the calculation

#-------------------------------------------------------------------------
# Main programm

def main():
    print("\nStart City:\n")
    city1 = find_city ()                                                    # Give the cityline to city1

    lon1 = city1[5]                                                         # Read the longitude
    lat1 = city1[4]                                                         # Read the latitude

    logging.info('The first city has been choosen.')                        # Log information

    print("End City:\n")
    city2 = find_city ()                                                    # Give the ciryline to city2

    logging.info('The seconed city has been choosen.')                      # Log information

    lon2 = city2[5]                                                         # Read the longitude
    lat2 = city2[4]                                                         # Read the latitude

    L = round(calculation(lon1, lat1, lon2, lat2),2)                        # Rounding off the result and keep 2 number after the radix point
    print("The Distance between [{}] and [{}] is:{}".format(city1[3],city2[3],L)+'km\n\n')
    logging.info('The Distance has been calculated and printed.')           # Log information
    rule()

#------------------------------------------------------------------------
# Asking for runnung the programm again

print("Air Line Distance Calculator \nby Chen Yuan MAB14 4060920 \n\n")
a=1
while a == 1:
    main()
    a= int(input("Do you want to run the programm again?\n1. yes   2.no"))
    if (a == 1):
            logging.info('User has choosed to run the programm again.')     # Log information
print("[Finish!]")
logging.info('User has choosed stop the programm.')                         # Log information

#------------------------------------------------------------------------
