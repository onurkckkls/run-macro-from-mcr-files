# Project Summary
This project is Pythonic solution for to read mcr files and to run some command lines in it. mcr is a file type which is using in macros

I code as many as we need. You don't hesitate to improve this codes if you need more command line which are using in mcr files


## Supporting Command Lines
- `COMMENT`
- `DELAY`
- `Mouse X X Click`
- `TYPE TEXT`
- `Keyboard`
- `LABEL`
- `GOTO`
- `REPEAT`
- `ENDREPEAT`
- `EXIT LOOP`
- `IF PIXEL COLOR EQUALS`
- `ELSE`
- `ENDIF`


# Easy Usage
- Add macro to project folder, or take macro full path name
- Run main.py or exe file with "-m MacroName" or "-m MacroFullPath" if you dont give -m argument it will ask when run.
- If you want to pause and resume, use `CTRL + R`
- The program will stop when macro is finished  


# Use as Module
You can import this code to all program in three line of code 

- `from fromMcr import FromMcr` to import FromMcr class
- `macro = FromMcr(path)` to create object 
- `macro.run()` to run macro 


# Requirement
- Windows envoriment (if you want to use this code in another operating systems you must modify some code.)
- python (lastest version recommended)
- pyautogui (to install `pip install pyautogui`)
- pyperclip (to install `pip install pyperclip`)
- keyboard (to install `pip install keyboard`)


# Test Knowledge
You can run program with your macro to test the program.
