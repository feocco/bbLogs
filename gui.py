from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from htmlFactory import *

def getDir():
	directory = askdirectory()

	if len(directory) == 0:
		printHtmlDocs(createTemplates())
	else:
		printHtmlDocs(createTemplates(directory), False)

	root.destroy()

def getFile():
	fileName = askopenfilename()

	printHtmlDocs(createTemplate(fileName), False)

	root.destroy()

root = Tk()
root.title("Bb Log Parser")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)

ttk.Label(mainframe, text="Select Log Files to Parse").grid(column=1, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Select Directory", command=getDir).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Select File", command=getFile).grid(column=1, row=3, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()