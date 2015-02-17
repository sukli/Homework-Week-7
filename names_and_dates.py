#! /usr/bin/python

import re
import glob

#names and dates will be printed into file named 'output'
output_file = open('output', 'w')
html_files = glob.glob('*.html')
#iterate through each html file
for file_name in html_files:
	f = open(file_name)
	file_text = f.read()
	#first match the large section of text with the dates / names in it
	prelim_match = re.findall("<div class=\"clear-fix right-wide-column\">.*", file_text, re.DOTALL)[0]
	#check if this page is part of the EcoEvoPub series
	ecoevopub = re.findall("EcoEvoPub Series", prelim_match)
	if (len(ecoevopub) > 0):
		#strip out date and name(s) from text
		date_match = re.findall("((January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2} [0-9]{4})", prelim_match)[0][0]
		names = re.findall(">([A-Z]+ [A-Z]+)<br", prelim_match)
		#write date and names to output file
		if len(names) > 0:
			output_file.write(date_match + "\n")
			for name in names:
				output_file.write(name + "\n")
	f.close()
	