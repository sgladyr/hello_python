# Author - Serhii Hladyr
import os
import platform
import sys
from traceback import print_exc

# Init Variables
name = input ("Your name: ")
age = input ("Your age: ")
live = input ("Where do you live?: ")
python_1 = (sys.version)
python_2 = (sys.version_info)
python_3 = (platform.python_version_tuple())
python_4 = ".".join(map(str, sys.version_info[:3]))

# Run commands
print ("This is the first Python Program in IT Academy")
print ("Hello,", name)
print ("Your age is", age)
print ("Your live in", live)
print ("1 - Your are using next python version (sys):", python_1)
print ("2 - Your are using next python version (sys info):", python_2)
print ("3 - Your are using next python version (platform):", python_3)
print ("4 - Your are using next python version (join map):", python_4)