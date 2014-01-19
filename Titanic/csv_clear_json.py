# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:41:10 2013

@author: olgis
1. import data from csv file:
    - all text is STR
    - all numbers are INT
2. change:
     - Verify age
         -- if Mrs older then 14
    - Change colomn NAME:
        -- ['Surname,', 'Title', 'Name1', 'Name2', ]
    - Add colomn Nickname (priviousle name included in braces) after Name
Export in to 
    - file_name_clean.csv
    - file_name_clean.json
"""
import csv
import json
import string as st
import sys
#import getopt

def proc_file(file_name):
    csv_input_file = file_name

    file_name = str(csv_input_file[:csv_input_file.index(".")])
    csv_output_file = file_name + "_clean" + ".csv"
    json_output_file = file_name + "_clean" + ".json"
    
    print "Open CSV file %s" %csv_input_file 
    with open(csv_input_file, mode="rb") as in_csv:
        dialect = csv.Sniffer().sniff(in_csv.read(1024)) #detect dialect
        csv_has_header = csv.Sniffer().has_header(in_csv.read(1024)) #detect has/hasn't header
        in_csv.seek(0)  #to restart reading from file normaly after dialect & header
    
        data = csv.reader(in_csv, dialect)
        
        new_data = []
        found_header = False
        

        for row in data:
            print "Processing row %s" %row[0]
            new_row = row[:]
            new_row.insert(4, None) #add colomn NICKNAME
            
            if csv_has_header and not found_header:
                new_row[4] = "Nickname"            
                found_header = True            
            else:
    
                for num in xrange(len(new_row)):
                    item = new_row[num]
#    #changing empty string, converting numbers into int() or float()
                    if item is not None:
                        if len(item) == 0:
                            new_row[num] = None #set empty str to NULL
    #modifying name col                    
                    if num == 3:
                        person = item
    
                        if person.find("(") != -1:
                            a = person.index("(") #allocating ( 
                            new_row[4] = person[a:].translate(st.maketrans("", "", ), '"()').split(" ") 
                            person = person[:a] #updating person
    
                        new_row[3] = person.strip().translate(st.maketrans("", "", ), '",').split(" ")
                        
            new_data.append(new_row)
            
    
                            
    print "Saving data into %s" %csv_output_file                      
    with open(csv_output_file, mode="w") as out_csv:
        write = csv.writer(out_csv)         
        write.writerows(new_data)
            
    print "Saving data into %s" %json_output_file
    with open(json_output_file, mode="w") as out_json:
        print new_data[0]
        for x in new_data[1:]:
            my_dict = dict(zip(new_data[0], x))
            json.dump(my_dict, out_json, ensure_ascii=False)
            out_json.write('\n')

        
####### TO DO: Not working

#def main(argv):
#   inputfile = argv[0]
#   try:
#      opts, args = getopt.getopt(argv,"ifile=")
#   except getopt.GetoptError:
#      print 'test.py  <inputfile.csv>'
#      sys.exit(2)
#   for opt, arg in opts:
#      if opt in ("__ifile"):
#          inputfile = arg 
#          print 'Input file is', inputfile
#          proc_file(sys.argv[1])
#      else:
#         print 'test.py <inputfile.csv>'
#         sys.exit()

if __name__ == "__main__":
    proc_file(sys.argv[1])
   