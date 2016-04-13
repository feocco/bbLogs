from jinja2 import Environment, FileSystemLoader
from fileFactory import *
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def createTemplates():
	# Create bbLog objects
	files = fileFactory()
	bbFiles = files.createInstances()

	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

	# Set template we will use
	template = env.get_template('newTemplate.html')
	templates = []

	for bbLog in bbFiles:
		templateVars = bbLog.dict
		name = bbLog.fileName.split('\\')[1]
		templates.append((name, template.render(fileName=name, templateVars=templateVars)))

	return templates

def print_html_docs(templates):
	for temp in templates:
		fileName = temp[0][:-4] + '.html'
		with open(fileName, "w") as fh:
			fh.write(temp[1])	

if __name__ == '__main__':
	print_html_docs(createTemplates())