import os, sys
from bbLog import *
from jinja2 import Environment, FileSystemLoader
from fileFactory import *

# Capture our current directory. Pyinstaller --onefile taken into account.
# First THIS_DIR only works for PyInstaller exe
if 'python.exe' in sys.executable:
	THIS_DIR = os.path.dirname(os.path.abspath(__file__))
else:
	THIS_DIR = os.path.join(os.path.dirname(sys.executable))

def createTemplates(directory=os.getcwd()):
	# Create bbLog objects
	files = fileFactory(directory)
	files = files.createInstances()

	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

	templates = []
	fileList = []

	for log in files:
		fileList.append(log.fileName)

	for bbLogInstance in files:
		# if bbLog class instance
		if isinstance(bbLogInstance, bbLog):
			templateVars = [bbLogInstance.dict, bbLogInstance.exclusionsList]
			template = env.get_template('template.html')
		else:
			templateVars = [bbLogInstance]
			template = env.get_template('templateAccess.html')

		name = bbLogInstance.fileName.split('\\')[-1]
		templates.append((bbLogInstance.fileName, template.render(fileList=fileList, fileName=name, templateVars=templateVars)))

	return templates

def createTemplate(fileName):
	# Create the ninja environment and load files from this directory
	env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
	template = env.get_template('template.html')

	bbLogVar = bbLog(fileName)
	templateVars = [bbLogVar.dict, bbLogVar.exclusionsList]
	name = bbLogVar.fileName.split('\\')[-1]
	
	return [(bbLogVar.fileName, template.render(fileList=[name], fileName=name, templateVars=templateVars))]


def printHtmlDocs(templates, inDir=True):
	for temp in templates:
		if inDir:
			fileName = temp[0].split('\\')[- 1][:-4] + '.html'
		else:
			fileName = temp[0][:-4] + '.html'

		with open(fileName, "w", encoding="utf8") as fh:
			fh.write(temp[1])