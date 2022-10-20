from macro import Macro
from random import randrange


class FromMcr(Macro):
    def __init__(self, path):
        super().__init__()
        self.path = path + ".mcr"
        self.lines = self.openFile()
        self.currentLineIndex = -1
        self.allLinesCount = len(self.lines)
        self.tabs = []
        self.line = None

    def openFile(self):
        """Opening mcr file

        Raises:
            FileNotFoundError: If file doesn't exists

        Returns:
            list: list of lines that all lines in one item
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                lines = list(
                    map(
                        lambda x: x.split(":"),
                        file.read().replace(" : ", ":").split("\n"),
                    )
                )
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found!")
        else:
            return lines

    def run(self):
        """To begin stepping in lines
        """
        while self.currentLineIndex < self.allLinesCount - 1:
            self.step()
            # print(self.currentLineIndex, self.lines[self.currentLineIndex])

    def step(self):
        """Step to functions, I don't use match, because befere 3.10 version of Python it doesn't support
        """
        self.currentLineIndex += 1

        self.line = self.lines[self.currentLineIndex]
        if self.line[0] == "COMMENT":
            self.comment()
        elif self.line[0] == "DELAY":
            baseTime = int(self.line[1])
            if len(self.line) > 2 and self.line[2] == "1":
                baseTime += randrange(int(self.line[3]))
            self.delay(baseTime)
        elif self.line[0] == "Mouse":
            if self.line[3] == "Click":
                self.click(int(self.line[1]), int(self.line[2]))
        elif self.line[0] == "TYPE TEXT":
            self.writePaste(self.line[1])
        elif self.line[0] == "Keyboard":
            self.keyboard(self.line[1], self.line[2])
        elif self.line[0] == "LABEL":
            pass
        elif self.line[0] == "GOTO":
            self.goTo()
        elif self.line[0] == "REPEAT":
            self.repeat()
        elif self.line[0] == "ENDREPEAT":
            self.endRepeat()
        elif self.line[0] == "EXIT LOOP":
            self.exitLoop()
        elif self.line[0] == "IF PIXEL COLOR EQUALS":
            self.ifColorFunction()
        elif self.line[0] == "ELSE":
            self.elseFunction()
        elif self.line[0] == "ENDIF":
            self.tabs.pop()
        else:
            pass
        # self.log('step')

    def stepForOnlyTabs(self):
        """To follow we are in which indentation (IF, REPEAT etc.)
        """
        self.currentLineIndex += 1

        self.line = self.lines[self.currentLineIndex]
        if self.line[0] == "REPEAT":
            self.tabs.append(
                {
                    "type": "for",
                    "beginLine": self.currentLineIndex,
                    "remaining": int(self.line[1]),
                }
            )
        elif self.line[0] == "ENDREPEAT":
            self.tabs.pop()
        elif self.line[0] == "IF PIXEL COLOR EQUALS":
            self.tabs.append({"type": "if", "success": False})
        elif self.line[0] == "ELSE":
            self.tabs[-1]["type"] = "else"
        elif self.line[0] == "ENDIF":
            self.tabs.pop()

        # self.log('stepForOnlyTabs')

    def comment(self):
        """Comment step
        """
        print(self.line[1])

    def keyboard(self, which, how):
        """Keyboard step

        Args:
            which (str): key code
            how (string): KeyPress|KeyDown|KeyUp
        """
        if how == "KeyPress":
            self.press(which)
        elif how == "KeyDown":
            self.keyDown(which)
        elif how == "KeyUp":
            self.keyUp(which)
            pass

    def goTo(self):
        """For going to specific line
        """
        label = self.line[1]
        self.tabs = []
        self.currentLineIndex = -1
        while self.currentLineIndex < self.allLinesCount - 1:
            if self.line[0] == "LABEL" and self.line[1] == label:
                break
            else:
                self.stepForOnlyTabs()

    def repeat(self):
        """For add repat indentation
        """
        self.tabs.append(
            {
                "type": "for",
                "beginLine": self.currentLineIndex,
                "remaining": int(self.line[1]),
            }
        )

    def endRepeat(self):
        """For delete repat indentation
        """
        if self.tabs[-1]["remaining"] > 0:
            self.currentLineIndex = self.tabs[-1]["beginLine"]
            self.tabs[-1]["remaining"] -= 1
        else:
            self.tabs.pop()

    def exitLoop(self):
        """For finish loop repeat
        """
        while self.currentLineIndex < self.allLinesCount - 1:
            if self.line[0] == "ENDREPEAT":
                self.stepForOnlyTabs()  # for finish loop repeat
                break
            else:
                self.stepForOnlyTabs()

    def ifColorFunction(self):
        """Color check codes
        """
        self.tabs.append({"type": "if", "success": False})
        currentTabIndex = len(self.tabs) - 1

        color = hex(int(self.line[3])).replace("0x", "", 1)
        if self.ifColor(int(self.line[1]), int(self.line[2]), color):
            self.tabs[currentTabIndex]["success"] == True
        else:
            while self.currentLineIndex < self.allLinesCount - 1:
                if (len(self.tabs) - 1) < currentTabIndex:
                    # self.currentLineIndex -= 1
                    break
                elif self.tabs[currentTabIndex]["type"] == "else":
                    break
                else:
                    self.stepForOnlyTabs()

    def elseFunction(self):
        """For else step
        """
        self.tabs[-1]["type"] = "else"
        currentTabIndex = len(self.tabs) - 1

        if self.tabs[-1]["success"]:
            while self.currentLineIndex < self.allLinesCount - 1:
                if (len(self.tabs) - 1) < currentTabIndex:
                    # When exit from tab block
                    break
                else:
                    self.stepForOnlyTabs()
        else:
            pass

    def log(self, stepFunctionType):
        """For logging for to check code 
        """
        print(
            f"{stepFunctionType} \n \
            path: {self.path} \n \
            lines: {self.line} \n \
            currentLineIndex: {self.currentLineIndex} \n \
            allLinesCount: {self.allLinesCount} \n \
            tabs: {self.tabs} \n\n \
            "
        )
        self.delay(500)
