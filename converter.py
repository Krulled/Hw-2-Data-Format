import sys
import json
import csv
import os
import xml.etree.cElementTree as ET


read = sys.argv[1:]
print('Argument List:', read)

#open file from the folder


#read second option
if(read[1] == "-c"):
    fileRead = read[0]
    with open(fileRead) as infile, open('outfile.csv','w') as outfile: 
        for line in infile: 
            outfile.write(line.replace('	',','))
    
if(read[1] == "-j"):
    
    with open(read[0], 'r') as igual, open('test.json', 'w') as jout:
        contents = igual.read()
        splitcontent = contents.splitlines()
        for l in splitcontent:
            pipesplit = l.split(" | ")
            print(pipesplit)
            json.dump(pipesplit,jout,indent = 4)
        jout.close()

if(read[1] == "-x"):
    root = ET.Element("root") # set up root
    doc = ET.SubElement(root, "input") # set up input
    fileRead = read[0]
    with open(fileRead) as infile, open('temp.csv','w') as outfile: 
        for line in infile: 
                        outfile.write(line.replace('	',','))
                        
    with open('temp.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|') 
        for row in csv_reader: 
            blanks_removed_row = ' '.join(row).split() 
            input = ET.SubElement(doc, "item")  
            for i, item in enumerate(blanks_removed_row, start=1):
                ET.SubElement(input, "data{0}".format(i)).text = item
    tree = ET.ElementTree(root) 
    tree.write("filename.xml", encoding='utf-8', xml_declaration=True)
    os.remove('temp.csv')
    