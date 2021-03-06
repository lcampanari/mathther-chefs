#!/usr/bin/env python
# coding: utf-8

# In[5]:


######################################################################################
#########                                                              ###############
######### Estimation of cooking times for a rectangular slab type meat ###############
#########                                                              ###############
######################################################################################

#### Importing libraries

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


########## 1. Thermal properties for the base case (Lean Beef) at near room termperatures ##############

h=6 # Only reduction(W/mK)
L_i=0.05 #Thickness of the meat cut (m)
L=L_i*0.6 #Thickness after meat shrinkage due to low boiling point at mars (Water boils at 0.7 Celsius at 610 Pa)
A=0.2*0.15 # Surface area(m^2)
V=L*A   #Volume (m^3)

#### 1.1 properties dependent on type of meat

k=0.42 #Thermal conductivity of the beef(W/mK)
rho=1067 # Density of the meat (kg/m^3)
cp=3810 #Specific heat at constant pressure (J/kgK)

#### 1.2 Temperature specification

Ti=-30+273.15 #Initial temperature of the meat
Ta=200+273.15 #Temperature of the oven
Tr=60+273.15 # desired temperature (user input)

########## 2. Derived dimensionless numbers ##########
Bi=h*(L/2)/k #Biot number
alpha=k/(rho*cp) #Thermal diffusivity
tc=((L/2)**2)/alpha #characteristic time
theta_r=(Tr-Ta)/(Ti-Ta)

######### 3. Cooking time calcultion ############

#### 3.1 Finding eigen values ####
### For slab the transcendental equation is given by Bi=lambda*tan(lambda)##

number_of_eigen_values=40

def func_tan(x):
    return x*np.tan(x)-Bi 

guess=np.arange(0.1,10,(10-0.1)/number_of_eigen_values)

res = fsolve(func_tan,guess)
res=np.around(res,6)
eigen_values=np.unique(np.absolute(res))  #eigen values


Fo=np.arange(0,4,0.02)   # Fourier number

x_star=np.arange(0,1,0.01) # dimensionless space grid
T_star=[] #dimensionless temperature
s1=0           
x_center=0 #dimensionless centre
theta=[]

#### 3.2 Theta (dimensionless temp)=A_n*space_func*exp_func

A_n=[2*np.sin(i)/(i+np.sin(i)*np.cos(i)) for i in eigen_values]
space_func=[np.cos(i*x_center) for i in eigen_values]

for k in range(len(Fo)):
    for j in range(len(space_func)):
        s1+=A_n[j]*space_func[j]*np.exp(-(eigen_values[j]**2)*Fo[k])
    theta.append(s1)
    s1=0

Temp=[i*(Ti-Ta)+Ta for i in theta]  #### Temperature profile at the center


for index, val in enumerate(theta):
    if np.absolute(val-theta_r) < 0.01:
        cooking_time=Fo[index]*tc    ###cooking time in seconds
        
cooking_time=np.around(cooking_time/3600,3)
hours=int(cooking_time)
minutes=np.absolute(cooking_time-hours)*60
minutes=np.around(minutes,0)
print("The cooking time on mars is %d hour(s) and %d minutes. " %(hours, minutes))

######### 4. Temperature in space and time #########
theta_eta=np.zeros((len(Fo),len(x_star)))
s2=0
for k in range(len(Fo)):
    for i in range(len(x_star)):
        for j in range(len(eigen_values)):
            s2+=A_n[j]*np.cos(eigen_values[j]*x_star[i])*np.exp(-(eigen_values[j]**2)*Fo[k])
        theta_eta[k,i]=s2
        s2=0    

theta_eta=np.array(theta_eta)

######## Energy calculation ######

E=V*rho*cp*(Tr-Ti) #Total energy consumed
print("Energy in kJ is: ", E/1000)
print("Energy in kWh is: ", E/1000/3600)
# print(np.dot(A_n,space_func))

# print(theta,theta_r)
print(eigen_values,Bi)


# In[233]:





# In[222]:


f=2*np.sin(9.561532)/(9.561532+np.sin(9.561532)*np.cos(9.561532))
g=np.exp(-((0.946972)**2)*1.5)
h=np.cos(3.501085*0.5)
m=2*np.sin(6.483413)/(6.483413+np.sin(6.483413)*np.cos(6.483413))
n=np.exp(-((6.483413)**2)*0.6)
o=np.cos(6.483413*0.5)

print(g)

