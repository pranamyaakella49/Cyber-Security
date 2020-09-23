# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:36:02 2019

@author: pranamyaakella
"""

##findLCP Function

def findLCP(str1, str2):
    output=[]
    i=0
    j=0
    
    while i<= (len(str1)-1) and j <= (len(str2)-1):
        if str1[i]==str2[j]:
            output.append(str1[i])
            i+=1
            j+=1
        else:
            break
    
    output = ''.join(output)
    return output
        
##findPrefix function
def findPrefix(list_of_strings, init, total_strings):
    
    if init == total_strings:
        return list_of_strings[init]
    
    if total_strings > init:
        mid = init + (total_strings - init)//2
        #mid = init + (total_strings - init)//3
        str1= findPrefix(list_of_strings, init, mid)
        str2= findPrefix(list_of_strings, mid+1, total_strings)
        
        return findLCP(str1, str2)
    

##Declaration
init = 0

list_of_strings = list(map(str, input("Enter multiple strings:").split())) 
print("List of strings: ", list_of_strings) 
total_strings = len(list_of_strings)-1
matchedValues = findPrefix (list_of_strings, init, total_strings)
#print("Common prefix size:", len(matchedValues))
print("Longest Common subsequence:", matchedValues)
