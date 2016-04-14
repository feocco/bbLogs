from jinja2 import Environment, FileSystemLoader
from fileFactory import *
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def createTemplates(directory=os.getcwd()):
	# Create bbLog objects
	files = fileFactory(directory)
	bbFiles = files.createInstances()

	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

	# Set template we will use
	template = env.get_template('newTemplate.html')
	templates = []

	for bbLog in bbFiles:
		templateVars = bbLog.dict
		name = bbLog.fileName.split('\\')[1]
		templates.append((bbLog.fileName, template.render(fileName=name, templateVars=templateVars)))

	return templates

def print_html_docs(templates, inDir=True):
	for temp in templates:
		if inDir:
			fileName = temp[0].split('\\')[- 1][:-4] + '.html'
		else:
			fileName = temp[0][:-4] + '.html'
		with open(fileName, "w") as fh:
			fh.write(temp[1])	

if __name__ == '__main__':
	directory = input("Input directory of log files or press [ENTER] for current directory:\n")
	if len(directory) == 0:
		print_html_docs(createTemplates())
	else:
		print_html_docs(createTemplates(directory), False)