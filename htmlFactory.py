import os
from jinja2 import Environment, FileSystemLoader
from fileFactory import *
from tkinter import *
from tkinter.filedialog import askdirectory      

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def createTemplates(directory=os.getcwd()):
	# Create bbLog objects
	files = fileFactory(directory)
	bbFiles = files.createInstances()

	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

	# Set template we will use
	template = env.get_template('template.html')
	templates = []
	fileList = []

	for bbLog in bbFiles:
		fileList.append(bbLog.fileName)

	for bbLog in bbFiles:
		templateVars = bbLog.dict
		name = bbLog.fileName.split('\\')[-1]
		templates.append((bbLog.fileName, template.render(fileList=fileList, fileName=name, templateVars=templateVars)))

	return templates

def printHtmlDocs(templates, inDir=True):
	for temp in templates:
		if inDir:
			fileName = temp[0].split('\\')[- 1][:-4] + '.html'
		else:
			fileName = temp[0][:-4] + '.html'
		with open(fileName, "w", encoding="utf8") as fh:
			fh.write(temp[1])	

def callback():
	directory = askdirectory() 
	if len(directory) == 0:
		printHtmlDocs(createTemplates())
	else:
		printHtmlDocs(createTemplates(directory), False)
	root.destroy()

if __name__ == '__main__':
	root = Tk()
	Button(root, text='Select Log Directory', command=callback).pack(fill=X)
	mainloop()