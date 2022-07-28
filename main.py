from tkinter import *
from tkinter.ttk import *


class Window:
    def __init__(self, parent):  # this creates all necessary widgets and data for runtime
        self.root = parent

        self.money = {
            '100': 100,
            '50': 50,
            '20': 20,
            '10': 10,
            '5': 5,
            '1': 1,
            '0.25': 0.25,
            '0.10': 0.1,
            '0.05': 0.05,
            '0.01': 0.01
        }

        # creates the day cash label and entry widgets
        self.dayCashLbl = Label(self.root, text="Day cash: $")

        self.dayCashTxtVar = StringVar()
        self.dayCashEtry = Entry(self.root, width=6, textvariable=self.dayCashTxtVar)
        self.dayCashTxtVar.trace('w', lambda *args: numFilter(self.dayCashTxtVar, deci=True))

        # creates the target drawer label and entry widgets
        self.targetLbl = Label(self.root, text="Target:      $")

        self.targetStrVar = StringVar()
        self.targetEtry = Entry(self.root, width=6, textvariable=self.targetStrVar)
        self.targetStrVar.trace('w', lambda *args: numFilter(self.targetStrVar, deci=True))

        # this creates the bill amount label and entry widgets
        self.moneyFrame = Frame(self.root)
        self.moneyVars = []
        self.moneyEtries = []
        self.moneyLbls = []
        for bill in self.money:
            self.moneyLbls.append(Label(self.moneyFrame, text=f"${bill}:"))

            self.moneyVars.append(StringVar())
            self.moneyVars[-1].trace('w', lambda *args: numFilter(self.moneyVars[-1]))

            # TODO: fix bug that breaks entry filtering with bill entries
            self.moneyEtries.append(Entry(self.moneyFrame, width=4, textvariable=self.moneyVars[-1]))

    def setUp(self):  # this grids all startup widgets created by init
        self.dayCashLbl.grid(column=0, row=0, sticky='nw')
        self.dayCashEtry.grid(column=1, row=0, sticky='nw')

        self.targetLbl.grid(column=0, row=1, sticky='nw')
        self.targetEtry.grid(column=1, row=1, sticky='nw')

        for x in range(len(self.moneyLbls)):
            self.moneyLbls[x].grid(column=0, row=x, sticky='ne')
            self.moneyEtries[x].grid(column=1, row=x)

        self.moneyFrame.grid(column=1, row=2)


def numFilter(txtVar, deci=False, *args):
    """
    this can be set to a string var to filter out any non number character
    :param txtVar: a tk string var that will be filtered
    :param deci: if a decimal should be allowed
    :param args: throwaway arg for extra arguments
    :return: none
    """
    currVal = splitStr(txtVar.get())

    if len(currVal) == 0:
        return

    elif not valInt(currVal[-1]):
        if currVal[-1] == '.' and deci and countChar(currVal, '.') <= 1:
            print("Decimal Exception Detected")

        else:
            print("Non-Int Detected. Deleting")
            currVal.pop()
            txtVar.set(''.join(currVal))

    else:
        print("Int Detected")


def splitStr(val):
    """
    this func splits a string into a list
    :param val: a string that will be converted into a list
    :return: a list version of val
    """
    return [char for char in val]


def countChar(lis, char):
    """
    this counts how many of a specified char in a string or list
    :param lis: string or list to be tested
    :param char: the character to be counted
    :return: number of characters in given list or string based on given char
    """
    charAmount = 0

    for character in lis:
        if character == char:
            charAmount += 1

    return charAmount


def valInt(instr):
    """
    this verifies that the given data is an integer
    :param instr: given data to be tested
    :return: true if int, false if value error
    """
    try:
        int(instr)
        return True

    except ValueError:
        return False


if __name__ == '__main__':
    root = Tk()

    window = Window(root)
    window.setUp()

    root.mainloop()
