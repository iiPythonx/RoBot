# Modules
import pygetwindow as gw
from errors import NoRobloxInstance

# Master class
class WindowManager():

    def switchToProgram(self, name = "Roblox"):

        programList = gw.getWindowsWithTitle(name)

        for program in programList:

            if "discord" in program.title.lower():

                programList.remove(program)
                
        try:

            program = programList[0]

            program.maximize()

            program.activate()

        except:

            raise NoRobloxInstance("No ROBLOX instance detected.")

    def focusROBLOX(self):

        self.switchToProgram()

