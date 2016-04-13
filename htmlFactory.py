from jinja2 import Environment, FileSystemLoader
from fileFactory import *
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def print_html_doc():
	# Create bbLog objects
	files = fileFactory()
	bbFiles = files.createInstances()

	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

	# Set template we will use
	template = env.get_template('newTemplate.html')

	for bbLog in bbFiles:
		templateVars = bbLog.dict
		return template.render(filename=bbLog.fileName, templateVars=templateVars)


if __name__ == '__main__':
	with open("renderedTemplate.html", "w") as fh:
		fh.write(print_html_doc())