# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:10:24 2018

@author: Ammar
"""

import csv

import matplotlib.pyplot
import pylab
import numpy as np
import copy


with open('ex1data2.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)

Features=[]

n=len(data[0])-1

#as many features as n-1
for i in range(0,n):
    Features.append([])


#populate the list using data
for i in range(0,len(data)):
    for j in range (0,n):
        Features[j].append(float(data[i][j]))


#copying the lists before normalizing
Features2 = copy.copy(Features)


#normalizing the features
for i in range(0,n):
    mean=np.mean(Features[i])
    std=np.std(Features[i])
    for j in range(len(Features[i])):
        Features[i][j]=(Features[i][j]-mean)/std
        
        
#Making and initialzing Theetas
Theetas=[]
for i in range (0,n+1):
    Theetas.append(float(0.5))



 

    
def find_h_of_x(Theetas=[],Features=[]):
   
    cost=Theetas[0]
    for i in range(0,len(Features)):
        cost=cost+(Features[i]*Theetas[i+1])
        
    return cost    
  
#Cost Function
def costFunction(Theetas=[],Features=[],data=[]):
    
    sum=0
    
    for j in range(0,len(Features[0])):
        myFeatures=[]
        for i in range(0,len(Features)):
            myFeatures.append(Features[i][j])
        hOfx=find_h_of_x(Theetas,myFeatures)
        term1=hOfx-float(data[j][len(data[0])-1])
        term1=term1*term1
        sum=sum+term1
        
    return (sum/len(data))



  
#function to update theetas
def updateTheeta(k,Theetas=[],Features=[],data=[]):
    sum=0
    alpha=0.09
    for j in range(0,len(Features[0])):
        myFeatures=[]
        for i in range(0,len(Features)):
            myFeatures.append(Features[i][j])
        hOfx=find_h_of_x(Theetas,myFeatures)
        term1=hOfx-float(data[j][len(data[0])-1])
        if k>0:
            term1=term1*myFeatures[k-1]
            
        sum=sum+term1
        
    return ((sum*alpha)/len(data))


tempTheetas=copy.copy(Theetas)

costList=[]

#running 50 iterations to find best value of alpha
for i in range(0,50):
    costList.append(costFunction(Theetas,Features,data))
    for j in range(0,len(tempTheetas)):
        tempTheetas[j]=tempTheetas[j]-updateTheeta(j,Theetas,Features,data)
        
    Theetas=copy.copy(tempTheetas)
    tempTheetas=copy.copy(Theetas)


xList=[]
for i in range(0,50):
    xList.append(float(i+1))
    
    
matplotlib.pyplot.plot(xList,costList,"r-")
matplotlib.pyplot.xlabel("Number of Iterations")
matplotlib.pyplot.ylabel("Cost")


#Running the chosen alpha value to find the final theeta values            
            
for i in range(0,1500):
    for j in range(0,len(tempTheetas)):
        tempTheetas[j]=tempTheetas[j]-updateTheeta(j,Theetas,Features,data)
        
    Theetas=copy.copy(tempTheetas)
    tempTheetas=copy.copy(Theetas)
    
    
#Checking the theeta values against the test example given in the question
Area=1650
Bedrooms=3
normalizedArea=(Area-np.mean(Features[0]))/np.std(Features[0])
normalizedBedrooms=(Bedrooms-np.mean(Features[1]))/np.std(Features[1])

predictedPrice=Theetas[0]+(Theetas[1]*normalizedArea)+(Theetas[2]*normalizedBedrooms)


#print(Theetas)

#Printing Predicted Price

print("Predicted Price for test example:")
print(predictedPrice)




    


        
          
        
        
      
