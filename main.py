# Notes:
# - Use TopLevel() to make new window (4 preferences)

# To Do:
# - add preferences
# - font size
# - fonts

import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog, messagebox
import settings

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.boldVar = tk.IntVar()
        self.italicVar= tk.IntVar()
        self.underlineVar = tk.IntVar()

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = tk.Menu(menu)
        fileMenu.add_command(label="Open", command=self.openFile)
        fileMenu.add_command(label="Save", command=self.saveAs)
        fileMenu.add_command(label="Find")
        fileMenu.add_command(label="Preferences", command=self.openSettings)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = tk.Menu(menu)
        editMenu.add_command(label="Bold", command=self.makeBold)
        editMenu.add_command(label="Italic", command=self.makeItalic)
        editMenu.add_command(label="Underline", command=self.makeUnderline)
        editMenu.add_command(label="Font Size ↑")
        editMenu.add_command(label="Font Size ↓")
        menu.add_cascade(label="Edit", menu=editMenu)

        viewMenu = tk.Menu(menu)
        viewMenu.add_command(label="Dark Mode", command=self.darkMode)
        menu.add_cascade(label="View", menu=viewMenu)

        self.toolbar = tk.Frame(root, bg="#eee")
        self.toolbar.pack(side="top", fill="x")

        self.boldBtn = tk.Checkbutton(self.toolbar, text="Bold", command=self.makeBold, variable=self.boldVar)
        self.boldBtn.pack(side="left")

        self.italicBtn = tk.Checkbutton(self.toolbar, text="Italic", command=self.makeItalic, variable=self.italicVar)        
        self.italicBtn.pack(side="left")

        self.underlineBtn = tk.Checkbutton(self.toolbar, text="Underline", command=self.makeUnderline, variable=self.underlineVar)
        self.underlineBtn.pack(side="left")

        self.fontIncreaseBtn = tk.Button(self.toolbar, text="Font Size ↑")
        self.fontIncreaseBtn.pack(side="left")

        self.fontDecreaseBtn = tk.Button(self.toolbar, text="Font Size ↓")
        self.fontDecreaseBtn.pack(side="left")

        self.boldFont = Font(family="Helvetica", size=9, weight="bold")
        self.italicFont = Font(family="Helvetica", size=9, slant="italic")
        self.underlineFont = Font(family="Helvetica", size=9, underline="yes")

        self.boldItalic = Font(family="Helvetica", size=9, weight="bold", slant="italic")
        self.boldUnderling = Font(family="Helvetica", size=9, weight="bold", underline="yes")
        self.boldItalicUnderline = Font(family="Helvetica", size=9, weight="bold", slant="italic", underline="yes")
        self.ItalicUnderline = Font(family="Helvetica", size=9, slant="italic", underline="yes")

        scrollbar = tk.Scrollbar(root)

        self.text = tk.Text(root, yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.text.yview)
        self.text.pack(fill="both", expand="yes")

        self.text.tag_configure("BOLD", font=self.boldFont)
        self.text.tag_configure("ITALIC", font=self.italicFont)
        self.text.tag_configure("UNDERLINE", font=self.underlineFont)

    def makeBold(self):
        try:
            self.text.tag_add("BOLD", "sel.first", "sel.last")
        except:
            pass

    def makeItalic(self):
        try:
            self.text.tag_add("ITALIC", "sel.first", "sel.last")
        except:
            pass

    def makeUnderline(self):
        try:
            self.text.tag_add("UNDERLINE", "sel.first", "sel.last")
        except:
            pass

    def openFile(self):
        dialog = filedialog.askopenfilename(title="Open File", filetypes=(("text files","*.txt"),("all files","*.*")))
        chosenFile = open(dialog, "r")

        self.text.insert("1.0", chosenFile.read())

        chosenFile.close()

    def saveAs(self):
        self.newFile = filedialog.asksaveasfilename(initialdir="/Desktop", title="Save File", filetypes=(("text files","*.txt"),("all files","*.*")))

        savedFile = open(self.newFile + '.txt', 'x')
        savedFile.write(self.text.get('1.0', 'end'))
        savedFile.close()
        tk.messagebox.showinfo('', 'File Saved Successfully')

    def onExit(self):
        self.quit()

    def darkMode(self):
        self.text.configure(background="#292929", foreground="#eee", insertbackground="#eee")
        self.toolbar.configure(background="#3d3d3d")
        self.boldBtn.configure(background="#4a4a4a", foreground="#fff")
        self.italicBtn.configure(background="#4a4a4a", foreground="#fff")
        self.underlineBtn.configure(background="#4a4a4a", foreground="#fff")
        self.fontIncreaseBtn.configure(background="#4a4a4a", foreground="#fff")
        self.fontDecreaseBtn.configure(background="#4a4a4a", foreground="#fff")

    def openSettings(self):
        settingsWindow = tk.Toplevel()
        settingsWindow.geometry("400x500")
        settingsWindow.title("WIP Preferences")

        self.themeButton = tk.Checkbutton(settingsWindow, text="Dark Mode")
        self.themeButton.pack(padx=0, pady=50)


root = tk.Tk()
root.geometry('700x500')
root.title('WIP Notes')
app = App(root)
root.mainloop()