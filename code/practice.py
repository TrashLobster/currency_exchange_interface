import tkinter
tk = tkinter

from tkinter import StringVar, Label, Button
from tkinter import font
from tkinter.ttk import Combobox

class Parking_Gui(tk.Frame):

    def __init__(self):
        """Sets up the window and widgets"""
        tk.Frame.__init__(self)

        self.myfont = font.Font(family="Calibri", size=11, weight="normal")

        self.master.geometry("315x125")
        self.master.title("MSU PARKING APP")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = 'NW')

        # Label for the parking lots
        self.LotLabel = tk.Label(self, text = "MSU Parking",  font=self.myfont)
        self.LotLabel.grid(row = 0, column = 0)

        # Combo Box for parking lots
        self._ComboValue = tk.StringVar()
        self._LotCombo = Combobox(self, textvariable=self._ComboValue,
                                  state='readonly', height = '6',
                                  justify = 'center', font=self.myfont)

        # List of parking lots
        self._LotCombo['values']=('ARTX', 'BURG', 'CLAY_HALL', 'GLAB',
                                  'HAMH_HUTC', 'HHPA', 'JVIC', 'LIBR','PLSU',
                                  'POST',  'PROF', 'STEC', 'STRO_NORTH',
                                  'STRO_WEST', 'TROP')
        self._LotCombo.grid(row = 0, column = 1)


        # Button to open parking diagram
        self._button = tk.Button(self, text = "Open", font=self.myfont)
        self._button.bind('<Button-1>', self._runParkingLot)
        self._button.grid(row = 0, column = 2)

        # Press enter to open selected parking diagram
        self._LotCombo.bind("<Return>", self._runParkingLot)

        # Search Combobox with keyboard
        self._LotCombo.bind("<Key>", self.findInBox)

        self._LotCombo.focus()

    def _runParkingLot(self, event):
        """Event handler for the button. Will run the
           functinon associated with selected item"""

        parkingLot = self._LotCombo.get()

        """The 'globals' keyword, will return a dictionary of every function,
           variable, etc. currently defined within the global scope."""
        if parkingLot in globals():
            func = globals()[parkingLot]
            func()

    def findInBox(self, event):
        """findInBox method allows user to search through Combobox values
           by keyboard press"""

        alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z')

        lot = ('ARTX', 'BURG', 'CLAY_HALL', 'GLAB', 'HAMH_HUTC', 'HHPA',
               'JVIC' ,'LIBR', 'PLSU', 'POST', 'PROF', 'STEC',
               'STRO_NORTH', 'STRO_WEST', 'TROP')

        keypress = event.char
        keypress = keypress.upper()

        # If key pressed is a letter in alphabet 
        if keypress in alpha:

             # if user press 'A' on keyboard return first item in list
             if(keypress == lot[0][0]):
                    self._LotCombo.current(0)

             # Searches list for first occurrence of key entered by user 
             else:
                 count = 1
                 while(keypress != lot[count][0] and count < len(lot)-1 ):
                     count +=1

                 self._LotCombo.current(count)
                 count = 1

def main():
    Parking_Gui().mainloop

main()