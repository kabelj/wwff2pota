# wwff2pota
Convert WWFF adif file to POTA adif file

This assumes the WWFF adif file has a name of the form `'call@park-ref_date.adi'`,
for example `'aa6xa@kff-0021_20221224.adi'`
It pulls the WWFF ref from the file name, looks up the corresponding POTA ref,
then writes it to a new adif file.

To use: Run the python script. It will prompt for a directory. Enter the full
path, e.g. /home/username/Documents/WWFFlogs/
The script will convert all the adif files it finds to POTA, and append \_POTA 
to the new filename.

The table used for conversion is from 
https://countyhunter.com/Toplist/KFF-County.htm
Thanks to the hams for creating it!
