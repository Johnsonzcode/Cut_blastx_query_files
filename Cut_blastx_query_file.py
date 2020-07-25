#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !usr/bin/python3
# Function: cutting the blastx query file into several files


print('Start reads number counting and copy all the reads to list ...')
###################################################################
with open('GHJL01.2.fsa_nt') as f:
    # the number of reads
    n_reads = 0
    # the list of all reads sequence
    all_reads = []
    # the list of the lines of a read
    read = []
    while 1:
        l = f.readline()
        if l == '':
            all_reads.append(read)
            read = []
            n_reads += 1
            break
        elif l.startswith('>') and len(read) != 0:
            all_reads.append(read)
            read = []
            read.append(l)
            n_reads += 1
        else:
            read.append(l)
print('Done!')
print('The number of all reads is ',n_reads)

print('Start cutting list ...')
#########################################
# the number of reads that in one file
n = round(n_reads/10)
# the reads already have been put in file
rn = 0
print('Creat files to contain reads ...')
for x in range(10):
    f = open('GHJL01.2.fsa_nt'+str(x),'w')
    for i in all_reads[x*n:]:
        for y in i:
            f.write(y)
        rn += 1
        if rn == (x+1)*n-1:
            f.close()
            break
else:
    f.close()
    print('Done!')


# In[35]:





# In[ ]:




