import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

#locte every GT in the sequence
#from the GT, try to find the next AG
#the sequence between GT and AG is an intron (including GT and AG)
#the length of the intron is len(AG:)-len(GT:)+1
#find the next GT after the AG
#loop until there is no AG or no GT
#output the largest intron
   

# Find all start positions of 'GT' (splice-donor sites)
GT_sites = [m.start() for m in re.finditer('GT', seq)]   
largest_intron = ''
for i in GT_sites: 
    A =  re.search('AG', seq[i+2:])  # Search for 'AG' after 'GT'; A is the match object 
    if A: # if match, A = ture
        intron = seq [i:A.start()+2+i+2]
        if len(intron) > len(largest_intron):
            largest_intron = intron 
len = len(largest_intron)
print ('the largest intron is: ' + largest_intron)
print ('The length of the largest intron is ' + str(len))
  



