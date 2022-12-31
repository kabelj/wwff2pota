#This script will convert a WWFF adif file to a POTA adif file.
#
# It reads in a CSV table off all the WWFF/POTA references, checks if the number
# needs to be changed, then writes the new one. It will strip out the 'ff' in 
# the WWFF part, e.g. KFF-4480 (Angeles NF) will become K-4453.
# The table is from https://countyhunter.com/Toplist/KFF-County.htm  Thanks to 
# those hams for putting in the work compiling it.
#

import csv
import os
from pathlib import Path

#get WWFF adif file
#wwffFlnm = input('Enter WWFF adif log to convert: ')
#wwffFile = Path(wwffFlnm)

#read csv file
refFile = open('/home/jeff/Documents/radio/wwff-pota_ref.csv', 'r')
LongList = csv.reader(refFile)

#get directory
path = input('Enter full directory path: ')
for root,directories,file in os.walk(path):
    for file in file:
        if(file.endswith('.adi')):
            wwffFlnm = os.path.join(root,file)
            #print(wwffFlnm)
            wwffFile = Path(wwffFlnm)

            #create new file for POTA
            potaFlnm = wwffFlnm[0:-4]+'_POTA.adi'
            potaFile = Path(potaFlnm)

            #Find the wwff ref
            idx = wwffFlnm.find('@')
            wwffRef = wwffFlnm[idx+1:idx+9].upper()
            #print(wwffRef)

            #get corresponding pota ref
            for row in LongList:
                if row[0] == wwffRef:
                    potaRef = row[1]
                    #print(row)

            adif = wwffFile.read_text()
            adif = adif.replace('<my_sig_info:8>'+wwffRef,\
                '<my_sig_info:6>'+potaRef)
            potaFile.write_text(adif)

            #reset csv reader
            refFile.seek(0) 

# Close everything
refFile.close()

print('Conversion Done')
