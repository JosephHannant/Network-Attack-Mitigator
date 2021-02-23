# Network-Attack-Mitigator
This is the program for the project I researched and Implemented over my final year in university, it detects the presence of any ARP or DNS attacks occurring on your network after it is run. It has a proposed GUI which was not implemented in the final product due to time constraints as well as a text based UI. This program is optimised for the Linux operating system and is run through the command prompt. The accompanying report for the project which discusses multiple network attacks and how to deal with them as well as an in-depth evaluation of the code is available upon request.

README

Mitigation of Network attacks tool To start the tool navigate to the directory, open the command line and type 'python CommandLineMenu.py'.

Requirements Running a kali linux virtual machine, version: Distributor ID: Kali Description: Kali GNU/Linux Rolling Release: 2019.1 Codename: n/a

Python 2.7

Required modules: Scapy 2.4.0(comes with kali linux) PyQt5

Use: To start this module you navigate to the directory it is downloaded and run 'python CommandLineMenu.py ' in the terminal GUI can be opened and used but is not integrated with the other modules currently.

Functionality: This program is capable of scanning the network for ARP spoofing and DNS spoofing attacks. It uses a command line interface to give the options where either module can be loaded. It is setup in a module style so both the DNS and ARP functions are not dependent on eachother, this will aloow further modules to be implemented in the future.

Author Joseph Hannant 2019-2020
