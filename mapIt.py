#! python3
# mapIt.py - launches a map in the browswer using an address from
# command line or clipboard

import webbrowser, sys
import pyperclip


if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
print ('yo')

print (sys.argv)
print (address)
