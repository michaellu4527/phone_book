#
# Python Ver:   3.5.2
#
# Author:       Michael Lu
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 7.

from tkinter import *
import tkinter as tk

# Importing other custom modules
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from.
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define the master frame configuration
        self.master = master    # Self references ParentWindow

        # Cannot change the size of the login screen
        self.master.minsize(500, 300)  # (Height, Width)
        self.master.maxsize(500, 300)

        # This CenterWindow method will center app on the user's screen.
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")     # Title of the application window
        self.master.configure(bg="#F0F0F0")     # Gray color

        # This protocol method is a Tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module
        phonebook_gui.load_gui(self)







        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",
                             command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar,
                        tearoff=0)  # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(
            label="About This Phonebook Demo")  # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu)  # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')


"""

    This indicates to Python that if the program is run, to run the lines of code contained
    within the if statement in order.

"""
if __name__ == "__main__":
    root = tk.Tk()      # Creates a window from Tkinter
    App = ParentWindow(root)    # Instantiates the ParentWindow class as an App object
    root.mainloop()     # Continually loop so the window is always shown until manually closed
