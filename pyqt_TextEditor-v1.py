import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from pynotifier import Notification
from os import path as ospath
import tkinter as tk
from easygui import fileopenbox as ezguiFileDialog

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Constant app data;
        allColorsArray = [
            "black", "white", "gray", "silver", "maroon", "red", "purble", "fushsia", 
            "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua"]


        # App state data;
        self.curOpenPath = ""

        # Setting some window properties;
        self.setFixedSize(1500, 800)
        self.setWindowTitle("TextEditor")

        # Some Info Label;
        self.infoLabel = qtw.QLabel("Notepad made my: [bosdos12]  |  ", self)
        self.infoLabel.setFont(qtg.QFont("Arial", 23))
        self.infoLabel.move(10, 10)

        underlineText = qtw.QLabel("________________________________________________________________________________", self)
        underlineText.setFont(qtg.QFont("Arial", 20))
        underlineText.move(0, 32)

        # The path entry;
        self.pathEntry = qtw.QLineEdit(self)
        self.pathEntry.setPlaceholderText("File Path")
        self.pathEntry.setFont(qtg.QFont("Arial", 20))
        self.pathEntry.setFixedSize(380, 40)
        self.pathEntry.move(470, 10)

        # File dialog button;
        fileDialogButton = qtw.QPushButton("📁", self, clicked=self.openFileDialogToSetPATHENTRYText)
        fileDialogButton.setFont(qtg.QFont("Arial", 26))
        fileDialogButton.setFixedSize(35, 35)
        fileDialogButton.move(812, 12)

        # The enter button;
        enterButton = qtw.QPushButton("Open file",self, clicked=lambda:self.loadFileF())
        enterButton.setFont(qtg.QFont("Arial", 20))
        enterButton.setStyleSheet("width: 130; height: 33;")
        enterButton.move(860, 10)

        # The save button;
        saveButton = qtw.QPushButton("Save",self, clicked=lambda:self.saveFileF())
        saveButton.setStyleSheet("width: 130; height: 33;")
        saveButton.setFont(qtg.QFont("Arial", 18))
        saveButton.move(20, 66)

        # The actual notepad/text-location;
        self.TextsLocation = qtw.QTextEdit(self,
            readOnly=True,
            font=qtg.QFont("Arial", 15)
        )
        self.TextsLocation.setFixedSize(1160, 670)
        self.TextsLocation.move(20, 110)

        # Right side info labels;
        #/////////////////////////////////////////////////////////////////////
        editTextColLabel = qtw.QLabel("Edit Text Color", self)             #//
        editTextColLabel.setFont(qtg.QFont("Arial", 20))                   #//
        editTextColLabel.move(1250, 120)                                   #//
        #/////////////////////////////////////////////////////////////////////
        editBackgroundColLabel = qtw.QLabel("Edit Background Color", self) #//
        editBackgroundColLabel.setFont(qtg.QFont("Arial", 20))             #//
        editBackgroundColLabel.move(1200, 210)                             #//
        #/////////////////////////////////////////////////////////////////////
        editTextFontSizeLabel = qtw.QLabel("Edit Text Size", self)         #//
        editTextFontSizeLabel.setFont(qtg.QFont("Arial", 20))              #//
        editTextFontSizeLabel.move(1260, 300)                              #//
        #/////////////////////////////////////////////////////////////////////

        # Edit text color combbox;
        self.editTextColorCombbox = qtw.QComboBox(self)
        self.editTextColorCombbox.setFont(qtg.QFont("Arial", 20))
        self.editTextColorCombbox.setFixedSize(280, 40)
        self.editTextColorCombbox.move(1200, 150)
        # Filling the color combbox;
        for i in range(len(allColorsArray)):self.editTextColorCombbox.addItem(allColorsArray[i])

        # Edit text color combbox;
        self.editBackgroundColorCombbox = qtw.QComboBox(self)
        self.editBackgroundColorCombbox.setFont(qtg.QFont("Arial", 20))
        self.editBackgroundColorCombbox.setFixedSize(280, 40)
        self.editBackgroundColorCombbox.move(1200, 240)
        self.editBackgroundColorCombbox.addItem("white")
        # Filling the color combbox;
        for j in range(len(allColorsArray)): 
            if j != 1:
                self.editBackgroundColorCombbox.addItem(allColorsArray[j]) 
            else: 
                pass
        
        # Edit text font size combbox;
        self.editTextFontSizeSpinBox = qtw.QSpinBox(self,
            value=15, maximum=100, 
            minimum=1, singleStep=1)
        self.editTextFontSizeSpinBox.setFont(qtg.QFont("Arial", 20))
        self.editTextFontSizeSpinBox.setFixedSize(280, 40)
        self.editTextFontSizeSpinBox.move(1200, 330)

        # Save settings changes button;
        saveSettingsChangesButton = qtw.QPushButton("Save Settings", self, clicked=lambda:self.changeSettingsF())
        saveSettingsChangesButton.setFont(qtg.QFont("Arial", 18))
        saveSettingsChangesButton.setFixedSize(180, 40)
        saveSettingsChangesButton.move(1250, 700)

        # The rendering function;
        self.show()
    
    # Loading the file function;
    def loadFileF(self):
        # Checking if the file exists;
        hitPath = self.pathEntry.text()
        self.curOpenPath = hitPath
        if ospath.isfile(hitPath):
            self.TextsLocation.setReadOnly(False)
            self.setWindowTitle(f"Text Editor | {hitPath}")
            with open(hitPath, "r") as openedPath:
                self.TextsLocation.setText(openedPath.read())
        else:
            self.continueOrDont = tk.Tk()
            self.continueOrDont.geometry(f"300x180+{str(int((self.continueOrDont.winfo_screenwidth()/2)-150))}+{str(int((self.continueOrDont.winfo_screenheight()/2)-90))}")
            self.continueOrDont.title("File doesnt exist")
            tk.Label(self.continueOrDont, text="File doesnt exist,\ncreate new file?", font=("Arial", 20)).place(x=40, y=8)

            yesButton = tk.Button(self.continueOrDont, text=" No ", bg="red", fg="white", font=("Arial", 20), width=5, command=lambda: self.continueOrDont.destroy()).place(x=45, y=90)
            noButton = tk.Button(self.continueOrDont, text=" Yes", bg="lime", fg="white", font=("Arial", 20), width=5, command=lambda: self.createNewFileF()).place(x=165, y=90)

            self.continueOrDont.mainloop()
    
    # This function is called once the continueOrDont question gets answered with yes.
    # continueOrDont widget gets destroyed, than the desired file gets created on the desired directory;
    # At the end, the user gets notified about the new file creation;
    def createNewFileF(self):
        self.continueOrDont.destroy()
        with open(self.curOpenPath, "w") as nf:
            nf.write("Write to the new file.")
        Notification("Info", f"New file [{self.curOpenPath}] has been created.").send()
        self.loadFileF()

    def saveFileF(self):
        with open(self.curOpenPath, "w") as sf:
            sf.write(self.TextsLocation.toPlainText())
        # Clearing all the entries;
        self.TextsLocation.setText("")
        self.TextsLocation.setReadOnly(True)
        self.pathEntry.setText("")
    
    # Called from the file-dialog button,
    # Opens a file dialog and sets the entry text to the path,
    # Which then can be accessed by the "Open file" button;
    def openFileDialogToSetPATHENTRYText(self):
        settingPath = ezguiFileDialog()
        if settingPath != None and len(settingPath) > 0:
            self.pathEntry.setText(settingPath)

    
    # Called from the "Save Settings" button,
    # Sets the text-editor settings to those of the chosen settings;
    def changeSettingsF(self):
        self.TextsLocation.setFont(qtg.QFont("Arial", self.editTextFontSizeSpinBox.value()))
        self.TextsLocation.setStyleSheet(f"background-color: {self.editBackgroundColorCombbox.currentText()}; color:{self.editTextColorCombbox.currentText()};")




app = qtw.QApplication([])
mw = MainWindow()
app.exec_()




