#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
         
         
         
         
n=[]
def turnitaround(x):
    x.reverse()
    
    for i in x:
        i.reverse()
        n.append(i)
      
        

