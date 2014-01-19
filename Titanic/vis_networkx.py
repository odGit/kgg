# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:21:15 2013

@author: olgis
"""

import networkx as nx
import pygraphviz
import pylab as plt
import csv
import string as st

with open("train.csv", "rb") as infile:
   reader = csv.reader(infile)
   reader.next() # Skip header line.
   my_dict = {}
   for r in reader:
        a = r.pop(3)
        for i in r:
            if len(i) == 0:
                m = r.index(i)
                r[m] = None
        my_dict[a] = r

for item in my_dict:
    a = item.index(",")
    familyname = item[:a] #extracting surname before comma
    my_dict[item].append(familyname)
    
    if item.find("(") != -1:
        b = item.index("(")
        brace_name = item[b:].translate(st.maketrans("", "", ), '"()').rsplit()
        new_item = item[:b]
        my_dict[new_item] = my_dict[item]
        del(my_dict[item])
        my_dict[new_item].append(brace_name) #adding braces name as list
    else:
        my_dict[item].append(None)


name_list = list(my_dict.keys()) #creating a list of the passenger names

who_has_rel = [x for x in my_dict if int(my_dict[x][5]) > 0] #list of all passengers who had relative on a board -> graph edges

relatives = {}
#building a dict of all who had REGISTERED relatives on board
for item in who_has_rel:
    familyname = my_dict[item][-2]
    if familyname in relatives:
        relatives[familyname].append(item)
    else:
        relatives[familyname] = [item]
        
second_relatives = {}
#print relatives

#for n in name_list:
#    if my_dict[n][-1] is not None:
#        for i in my_dict[n][-1]:
#            if i in n and i not in ["Mr.", "Mr", "M", "Miss", "Mrs"] and len(i) >1:
#                print n,i
                

#
#
#g = nx.Graph()
#g.add_nodes_from(name_list)
#
#
#
##plot the graph
#pos = nx.spring_layout(g)
##pos=nx.graphviz_layout(g,prog='dot')
#
#nx.draw(g, pos,node_size=300)
#
##display the graph
#plt.show()