import sys
from ARPDetection import *
from DNSDetection import *
import time
progRunning = True
"""Title for the command line interface"""
print('''


 _   _      _                      _            _   _             _          _      _            _             
| \ | |    | |                    | |          | | | |           | |        | |    | |          | |            
|  \| | ___| |___      _____  _ __| | __   __ _| |_| |_ __ _  ___| | __   __| | ___| |_ ___  ___| |_ ___  _ __ 
| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /  / _` | __| __/ _` |/ __| |/ /  / _` |/ _ \ __/ _ \/ __| __/ _ \| '__|
| |\  |  __/ |_ \ V  V / (_) | |  |   <  | (_| | |_| || (_| | (__|   <  | (_| |  __/ ||  __/ (__| || (_) | |   
\_| \_/\___|\__| \_/\_/ \___/|_|  |_|\_\  \__,_|\__|\__\__,_|\___|_|\_\  \__,_|\___|\__\___|\___|\__\___/|_|   
''')
"""Loop for the command interface"""
while progRunning == True:
    print("Network attack detector")
    print("For ARP detection enter 1")
    print("For DNS detection enter 2")
    print("For Details concerning how the program works enter 3")
    print("To exit enter 4")
    userOption = ""
    """Takes user input"""
    userOption = input()
    """Each option to either start ARP, DNS, the about or to close the program."""
    if userOption == 1:
        print("You have chosen ARP Detection")
        print("To exit the program press ctrl+c")
        time.sleep(2)
        startARP()
    elif userOption == 2:
        print("You have chosen DNS Detection")
        print("To exit the program press ctrl+c")
        time.sleep(2)
        startDNS()
    elif userOption == 3:
        print("Instructions:")
        print("Choose the options in the menu, e.g. 1 for APR detection.")
        print("While one detection is running you can load another file to start another detection.")
        print("If you wish to stop the detection and return to the menu press ctrl+c in the command line to end it")
        print("Author Joseph Hannant, Student ID 17075709.")
        print("2019-2020")
        time.sleep(5)
    elif userOption == 4:
        print("Farewell")
        sys.exit(1)
    else:
        print("Incorrect choice enter a number between 1 and 4")
        time.sleep(1.5)
