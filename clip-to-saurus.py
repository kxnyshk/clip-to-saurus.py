# imports
import sys
import json
import clipboard
from time import sleep

# errors
ERR = '\nError!'
ERR_CMD = f'{ERR} Command not found.'
ERR_KEY = f'{ERR} Key not found.'

# defining PATH for clipboard
PATH = "clipboard.json"

# writer
def writer(text):
    for char in text:
        sleep(0.10)
        sys.stdout.write(char)
        sys.stdout.flush()

# methods

def loadData():
    try:
        with open(PATH, 'r') as path:
            return json.load(path)
    except:
        return {}

def saveData():
    key = input('Enter key: ')
    data = loadData()
    data[key] = clipboard.paste()

    with open(PATH, 'w') as path:
        json.dump(data, path)
        print('Data saved successfully!')

def copyData():
    key = input('Enter key: ')
    data = loadData()

    if key in data:
        clipboard.copy(data[key])
        print("Data copied to clipboard!")

    else:
        print(ERR_KEY)

def printData():
    data = loadData()
    print(data)

def help():
    writer('\nHi! This is clip-to-saurus 📎\nI save all your clipboards just with one command!')

    cmd1 = 'Save:\tCopy the text you wanna save. Run the save command.\n\tEnter the key you wanna ref. your data with. Voila! its done.'
    cmd2 = 'Copy:\tRun the copy command. Enter the key you saved your data with.\n\tYour data will be copied to clipboard!'
    cmd3 = 'Print:\tRun the print command. All the saved clips will get displayed to you.'

    print('\nHelp commands: \n')
    print(cmd1)
    print(cmd2)
    print(cmd3)

# main
def main(): 
    # help()

    if len(sys.argv) == 2:
        cmd = sys.argv[1]
        cmd = cmd.lower()

        match cmd:
            case "save": 
                saveData()
            case "copy": 
                copyData()
            case "print":
                printData()
            case _:
                print(ERR_CMD)

    else:
            print(ERR_CMD)

# run
main()

# comments
"""
bootstrap frozen
"""