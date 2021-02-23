import sys
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ProjectInterface import *
#from ARPDetection import *
import threading
import subprocess
from subprocess import Popen, PIPE
import thread
import time
"""This is the python file which connects the GUI and the other modules. This doesn't currently connect properly."""

ARPRun = True
DNSRun = True
"""This is used initialise the GUI window."""
class MyUi(QtWidgets.QMainWindow):
    """This is the implementation of the ARP module which would connect a GUI button to the ARPDetection module."""
    def ARPimp(self):
        #ARPRun =True
        #if ARPRun == True:

        self.ui.arpDisplay.append("Now monitoring")
        """time.sleep is used throughtout to give slight delays between interactions."""
        time.sleep(1)
        self.ui.arpDisplay.append("Check the console for ARP detection results")
        """Below is the attempt to run a module in command line through interaction with the button."""
        arpCon = 'python ARPDetection.py'
        #stdout = Popen(arpCon, shell=True, stdout=PIPE).stdout
        #moduleThreader(stdout.read())
        """Below is commented out code which was an attempt to connect another function to the button so I could
        thread the entire ARPimp process"""
        #time.sleep(1)
        #moduleThreader(self.ARPScan())
        #self.ARPScan()


                #arpInfo = self.ARPScan
                #self.ui.arpDisplay.append(arpInfo)
            #except TypeError:
            #    pass
            #arpInput = toS
    def stopARP(self):
        ARPRun = False
            # self.ui.arpDisplay.append("Ending monitoring")

    # arpThread = moduleThreader(ARPimp)

    #def ARPScan(self):
        #scanner("eth0")

    def __init__(self):
        super(MyUi,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.arpDetect.clicked.connect(lambda: self.ARPimp())
        self.ui.arpEnd.clicked.connect(self.stopARP)
        self.ui.arpClear.clicked.connect(self.clearTARP)


        self.show()

    """Clears the textEdit for the ARP tab"""
    def clearTARP(self):
        self.ui.arpDisplay.clear()


"""Threading module that I planned on passing ARP and DNS modules into so that the GUI isn't tied up."""
class moduleThreader(threading.Thread):

    def __init__(self, modFunc):
        threading.Thread.__init__(self)
        self.runnable = modFunc
        self.daemon = True


def runUI():
    app = QtWidgets.QApplication(sys.argv)
    w = MyUi()
    w.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    UIRun = moduleThreader(runUI())
    #thread.start_new_thread(runUI())
    UIRun.daemon = True

    '''app = QtWidgets.QApplication(sys.argv)
    w = MyUi()
    w.show()
    sys.exit(app.exec_())'''