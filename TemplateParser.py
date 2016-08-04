# =============================================================================================
# Script: TemplateParser.py
# Usage: python TemplateParser.py -i <TemplateFileName> -c <ConfigFileName>
# Description: This script takes in a template file which includes parameters enclosed in ${}
#              and replaces them with the values in the config file.
# Notes: The input template filename should have '_template' in the filename. 
# Author: Binal 
# =============================================================================================

# Imports
import ConfigParser
import os,sys, argparse
from string import Template
from subprocess import check_output, STDOUT

def parse_args():
	parser = argparse.ArgumentParser(description='This script replaces the parameters as per a config file')
	parser.add_argument('-i','--input', help='Input Template file name',required=True)
	parser.add_argument('-c','--config',help='Config file name', required=True)
	args = parser.parse_args()
	return args

def replaceTemplate(templateFile, configFile):
	# REad the config file
	config = ConfigParser.ConfigParser()
	config.optionxform = str
	config.read(configFile)
	config_params = {}
	for section in config.sections():
		for key, val in config.items(section):
			config_params[key] = val

	# Read the Template file		
	with open(templateFile, 'r+') as f:
		temp = Template(f.read())
		resultFile = temp.substitute(config_params)
	
	# Write the new replaced file
	outputFileName = templateFile.replace("_template","",1)
	target = open(outputFileName, 'w')
	target.write(resultFile)
	return outputFileName

def main():
    args = parse_args()
    print "Replacing parameters in the Template file.."
    outputFile = replaceTemplate(args.input, args.config)
    print "Parameters replaced !"
    print "============================================"

if __name__ == '__main__':
    main()