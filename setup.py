#!/usr/bin/python
# -*- coding: utf-8 -*-
#AUTHOR: EITENNE
import os

def main():
	os.system('mkdir /usr/bin/FUZZY')
	os.system('mv FUZZY /usr/bin/FUZZY/')
	file = open("fuzzy","w")
	file.write("#!/bin/bash")
	file.write("#AUTHOR: EITENNE")
	file.write("python FUZZY/FUZZY.py")
	file.close()
	os.system('mv fuzzy /usr/bin/fuzzy')
	os.system('chmod +x /usr/bin/fuzzy')
	print "Done! in terminal anywhere you can run the following command 'fuzzy'"

main()

