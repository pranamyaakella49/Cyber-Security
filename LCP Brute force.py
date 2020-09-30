# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:36:02 2019

@author: pranamyaakella
"""

##LCP brute force Function

def LCP_bruteForce(list_of_strings):
    
    total_strings = len(list_of_strings)
    
    list_of_strings.sort(reverse=False)
    str1= list_of_strings[0]
    str2= list_of_strings[total_strings-1]
    
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
    print("Longest Common Prefix is:", output)
    

list_of_strings = list(map(str, input("Enter multiple strings:").split())) 
print("Entered list of strings: ", list_of_strings) 
LCP_bruteForce (list_of_strings)


