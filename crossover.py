#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
gen1 = input("Enter 1st genes: ")#1100110110110011
gen2 = input("Enter 2nd genes: ")#1000110011011111
n = int(input("How many break points : ")) #less then length of gen1 #3 or 2 or 1
points = random.sample(range(1, len(gen1)-1), n)
points.append(len(gen1))
points.insert(0, 0)
points.sort()
print("\nFollowing are the offsprings: ")
for j in range(2):
    final = []
    for i in range(n+1):
        if i%2==0:
            final.append(gen1[points[i]:points[i+1]])
        else:
            final.append(gen2[points[i]:points[i+1]])
    print("".join(final))


# In[ ]:




