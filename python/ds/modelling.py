# -*- coding: utf-8 -*-
"""Modelling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15XhLYrirhvSdGsza8vsWTpBpY6gHEElg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

"""# **Oxygen Frame**

### Initial Oxygen Distribution
"""

c = np.random.rand(100,100)*100
plt.matshow(c)

"""### Microvessles """

from numpy.random import default_rng

rng = default_rng()

xv = rng.choice(100, size=10, replace=False)
yv = rng.choice(100, size=10, replace=False)

plt.matshow(c)
plt.scatter(xv,yv,color='w')
plt.show()

"""# **Cells**"""

from numpy.random import default_rng

rng = default_rng()
cel =[]

xc = rng.choice(100, size=1, replace=False)
yc = rng.choice(100, size=1, replace=False)
rc = ['b']
cel.append(cel(50,50,0,'b',1))
plt.figure(figsize=(5,5))
plt.matshow(c, fignum=1)
plt.scatter(xv,yv,color='w')
plt.scatter(cel[0].x,cel[0].y,color=cel[0].color,s=15)
plt.show()

print(cel)

"""# **Oxygen Dynamic**

c(t+1,j) = (1-d)*c(t,j) + (1/8 * sumk(d * c(t,k)) - ra * 1 + ri * delta(t,j)
"""

d = 0.6 #Oxygen Diffusion Coefficient
mu_r = 0.216
sd_r = 0.072
ri = 18
def r(pheno):
  if pheno=='n':
    return(np.random.normal(mu_r,sd_r))
  elif pheno=='c':
    mu_c = np.random.uniform(0.216,0.432)
    return(np.random.normal(mu_c,mu_c/3))
  else:
    return(0)
def nj(i,j):
  return(int(i in xc and (yc[np.where(xc==i)]==j).any()))
def delta(i,j):
  return(int(i in xv and (yv[np.where(xv==i)]==j).any()))

def recti(x):
  if x<0:
    return(0)
  else:
    return(x)

"""**define cell objects**"""

class cell:
  def __init__(self, x, y, age, color, typ , mig = 0 , death = 0 , quis = 0 , radio = 0):
    self.x = x
    self.y = y
    self.age = age
    self.color = color
    self.typ = typ
    self.death = death
    self.mig = mig
    self.quis = quis
    self.radio = radio

"""**constants**"""

a00=0.10
a01=0.45
a02=0.3
a11=0.04
a22=0.5
a1=0.34
a10 = 0.05
a0=0.13
a2=0.23
a12=0.14
a21=0.39
a20 = 0.25
cel[0].age = 0

"""**function**"""

def posi(obj):
  templi = []
  for i in obj:
    templi.append((i.x,i.y))
  return templi
def get_mig(obj):
  templi = []
  for i in obj:
    templi.append(i.mig)
  return templi
def get_death(obj):
  templi = []
  for i in obj:
    templi.append(i.death)
  return templi
def get_age(obj):
  templi = []
  for i in obj:
    templi.append(i.age)
  return templi

from pickle import TRUE
from ast import Break
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from numpy import random
import math
age = np.zeros((100,100))
c = np.random.rand(100,100)*10
tx = []
ty = []
cs = []
cc = []
are = []
xqui = []
yqui = []
scc = [1]
ncc = [0]
n = [1]
ncc1 = [0]
ncc2 = [0]
quisc = {}
ndc = [0]
for h in range(0,480):
  print(h)
  n.append(len(cel))
  iter = 0
  for j in range(0,100):
    for i in range(0,100):
      c[i,j] = recti((1-d)*c[i,j] + 0.125*d*(c[recti(i-1):recti(i+2),recti(j-1):recti(j+2)].sum()-c[i,j]) - r(pheno='n')*nj(i,j)/3 + d*delta(i,j)/1.5)
  #for i in range(0,len(xc)):
  for i in range(0,len(cel)):
      #if cel[i].age < 24: 
      #cel[i].age = cel[i].age  + 1 
    transit = np.random.normal(2.38,0.79)+2
    #if c[xc[i],yc[i]]>transit and np.random.uniform(0,1)>0.5:
    if c[cel[i].x,cel[i].y]>transit and np.random.uniform(0,1)>0.5:
      temx = cel[i].x + random.randint(-1,2)
      temy = cel[i].y + random.randint(-1,2)
      if (temx,temy) not in posi(cel):


      #xc[i] = xc[i] + np.random.randint(-1,2)
        cel[i].x = temx
        #cel[i].x = cel[i].x + random.randint(-1,2)
      #yc[i] = yc[i] + np.random.randint(-1,2)
        #cel[i].y = cel[i].y + random.randint(-1,2)
        cel[i].y = temy
      #c[xc[i],yc[i]] = c[xc[i],yc[i]]-2.38
        c[cel[i].x,cel[i].y] = c[cel[i].x,cel[i].y]-2.38
        cel[i].mig = cel[i].mig + 1
      #cel[i].x = xc[i]
      #cel[i].y = yc[i]
    #if age[xc[i],yc[i]]==24:
    if cel[i].age == 24 and cel[i].death == 0:
      #if c[xc[i],yc[i]]>1.88:
      if c[cel[i].x,cel[i].y]>1.88:
        for iter in range(0,10):
          #new_x = xc[i] + np.random.randint(-1,2)
          #new_y = yc[i] + np.random.randint(-1,2)
          new_x = cel[i].x + np.random.randint(-1,2)
          new_y = cel[i].y + np.random.randint(-1,2)
  
          #if new_x not in xc and new_y not in yc:
          if (new_x , new_y) not in posi(cel):
            break
          elif (new_x , new_y) in posi(cel):
            cel[i].quis = 1
        xc = np.append(xc,new_x)
        yc = np.append(yc,new_y)
        #if rc[i] == 'b':
        temprand = random.uniform(0,0.5)
        #temprand = 0.05
        if cel[i].color == 'b':
          #if temprand <= a00 and (a00-temprand)<(a01-temprand) and (a00-temprand)<(a02 - temprand):
          if temprand <= a00:
            cel.append(cell(new_x,new_y,0,'b',1))
            #rc.append('r')
            scc.append(scc[-1] + 1)
            #break
            continue
          #elif temprand <= a01 and (a01-temprand)<(a00-temprand) and (a01 - temprand)<(a02 - temprand):
          elif temprand <= a01:
            cel.append(cell(new_x,new_y,0,'r',1))
            #rc.append('b')
            ncc.append(ncc[-1] + 1)
            ncc1.append(ncc1[-1] + 1)
            n.append(n[-1] + 1)
            #break
            continue
          #elif temprand <= a02 and (a02-temprand)<(a00-temprand) and (a02 - temprand)<(a01 - temprand):
          elif temprand <= a02:
            cel.append(cell(new_x,new_y,0,'r',2))
            ncc.append(ncc[-1] + 1)
            ncc2.append(ncc2[-1] + 1)
            n.append(n[-1] + 1)
            #break
            continue
        #elif rc[i] == 'r':
        elif cel[i].color == 'r':
          #rc.append('r')
          #ncc.append(ncc[-1] + 1)
          if cel[i].typ == 1 and temprand <= a11:
            cel.append(cell(new_x,new_y,0,'r',1))
            ncc.append(ncc[-1] + 1)
            ncc1.append(ncc1[-1] + 1)
            n.append(n[-1] + 1)
            #break
            continue
          elif cel[i].typ ==2 and temprand <= a22:
            cel.append(cell(new_x,new_y,0,'r',2))
            ncc.append(ncc[-1] + 1)
            ncc2.append(ncc2[-1] + 1)
            n.append(n[-1] + 1)
            #break
            continue

        #age[xc[-1],yc[-1]]=0
        #age[xc[i],yc[i]]=0
        #if cel[i].age < 24: 
          #cel[i].age = cel[i].age  + 1 
      if c[xc[i],yc[i]]<1.88:
        if cel[i].color == 'b' and random.uniform(0,0.5) <= a0:
          #np.delete(xc,i)
          #np.delete(yc,i)
          #age[xc[i],yc[i]]=0
          #cel.pop(-1)
          cel[i].death = 1
          ndc.append(ndc[-1] + 1)
          n.append(n[-1] - 1)
          scc.append(scc[-1] - 1)
          #break
        elif cel[i].color == 'r' and cel[i].typ ==1 and random.uniform(0,0.5) <= a1:
          #cel.pop(-1)
          cel[i].death = 1
          ncc2.append(ncc2[-1] - 1)
          ncc.append(ncc[-1] - 1)
          ndc.append(ndc[-1] + 1)
          n.append(n[-1] - 1)
          #break
        elif cel[i].color == 'r' and cel[i].typ ==2 and random.uniform(0,0.5) <= a2:
          #cel.pop(-1)
          cel[i].death = 1
          ncc1.append(ncc1[-1] - 1)
          ncc.append(ncc[-1] - 1)
          ndc.append(ndc[-1] + 1)
          n.append(n[-1] - 1)
          #break
    #age[xc[i],yc[i]] = age[xc[i],yc[i]]+1
    if cel[i].age < 24:
      cel[i].age = cel[i].age  + 1 
    #tranformation
    transtemp = random.uniform(0,1)
    if cel[i].color == 'r' and cel[i].typ == 1 and transtemp<=a10:
      cel[i].color == 'b'
    if cel[i].color == 'r' and cel[i].typ == 2 and transtemp<=a20:
      cel[i].color == 'b'
    if cel[i].color == 'r' and cel[i].typ == 1 and transtemp<=a12:
      cel[i].typ == '2'
      ncc2.append(ncc2[-1] + 1)
      ncc1.append(ncc1[-1] - 1)
    if cel[i].color == 'r' and cel[i].typ == 2 and transtemp<=a21:
      cel[i].typ == '1'
      ncc1.append(ncc1[-1] + 1)
      ncc2.append(ncc2[-1] - 1)

    #print(area_np(xc,yc))
    #if iter%(100*100)==0:
    if 1 == 1:
      plt.matshow(c)
      plt.scatter(xv,yv,color='w')
      #for k in range(len(xc)):
      for k in range(len(cel)):
        #plt.scatter(xc[k],yc[k],color=rc[k],s=15)'
        if cel[k].death == 0:
          plt.scatter(cel[k].x,cel[k].y,color=cel[k].color,s=15)
          tx.append(cel[k].x)
          ty.append(cel[k].y)
        elif cel[k].death == 1:
          plt.scatter(cel[k].x,cel[k].y,color = (0.4, 0.1, 0.3, 0.3),s=15)
        #xc.append(cel[k].x)
        #yc.append(cel[k].y)
      try:
        if len(tx) > 2:
          allPoints=np.column_stack((tx,ty))
          hull = ConvexHull(allPoints)
          print('area=' + str(hull.volume))
          print(h)
          are.append(hull.volume)
          for simplex in hull.simplices:
            plt.plot(allPoints[simplex, 0], allPoints[simplex, 1], 'k-')
      except Exception:
        print(h)
      plt.show()
    iter = iter + 1
    cs.append(c[50,50])
    cc.append(c[xc[0],yc[0]])

print(len(cel))
g = 0
for i in cel:
  if i.mig >= 1:
    g = g + 1
print(g)
#plt.scatter(cel[2].x , cel[2].y , color = (0, 0, 0.9, 1) , s = 15)
#plt.scatter(cel[2].x , cel[2].y , color = (0.4, 0.1, 0.9, 0.3) , s = 15)

import seaborn as sns
#sns.displot(get_mig(cel), label_x = 'migration frequency' ,binwidth=1, discrete=True)
plt.hist(get_mig(cel) , label = 'Cell Migration Frequency')
plt.legend(loc="upper right")

plt.hist(get_age(cel) , label = 'Cell Age Distribution')
plt.legend(loc="upper right")

#sns.displot(get_death(cel), bins=[0,1],binwidth = 1,  discrete=True)
plt.hist(get_death(cel) , rwidth = 1.5, bins= [0,1,2], label = 'Cell Migration Frequency')
plt.legend(loc="upper right")
#print(get_death(cel))

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"} , figsize=(10,6))

# Make data.
X = np.arange(0, 100, 1)
Y = np.arange(0, 100, 1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, c[X,Y], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('x position')
ax.set_ylabel('y position')
ax.set_zlabel('Oxygen Concentration' )

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"} , figsize=(10,6))
n = 100
a1 = []
b1 = []
c1=[]
a2 = []
b2 = []
c2 =[]
for i in cel:
  if i.color == 'b':
    a1.append(i.x)
    b1.append(i.y)
    c1.append(i.mig)
  if i.color == 'r':
    a2.append(i.x)
    b2.append(i.y)
    c2.append(i.mig)
 
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for m, x ,y , z in [('o',a1,b1,c1 ), ('^',a2,b2,c2)]:
    xs = x
    ys = y
    zs = z
    ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('x position')
ax.set_ylabel('y position')
ax.set_zlabel('Migration frequency' )

plt.show()

plt.plot(scc , label= 'StemCell')
plt.plot(ncc , label= 'non-StemCell')
plt.legend(loc="upper left")

plt.plot(ncc1 , label = 'phenotype 1')
plt.plot(ncc2 , label = 'phenotype 2')
plt.legend(loc="upper left")

plt.plot(n , label = 'total cell')
plt.legend(loc="upper left")

"""# **deep copy of current object list**"""

import copy
new_list1 = copy.deepcopy(cel)

"""# **radiotherapy**"""

import random
import math
#cxc = np.copy(xc)

#cyc = np.copy(yc)
#crc = np.copy(rc)
g2 = 18
g1 = 0
s = 12
m = 22
alpha = 0.2
beta = 0
dose = 3
sfd = math.e**(-(alpha*dose + beta*dose*dose))
sfd = 0.23
print(sfd)
ind = []
t2x = []
t2y = []
for h in range(480):
  #print(h)
  #ind = []
  for j in new_list1:
    receivedradio = 0
    #xr = cxc[j]
    #yr = cyc[j]
    if j.age >= g2 and j.age < m :
      receivedradio = random.random()*1.25
    elif j.age >= g1 and j.age < g2:
      receivedradio = random.random()*0.75
    elif j.age >= s and j.age < g2:
      receivedradio = random.random()
    if receivedradio > sfd:
      #print(receivedradio)
      #for i in range(len(cxc)):
      #if cxc[i] == xr and cyc[i] == yr:
      #ind.append(j)
      j.radio = 1
      print(j.radio)
          #cxc = np.delete(cxc,i)
          #cyc = np.delete(cyc,i)
          #break
  #ind.sort()
  #ind.reverse()
  #for l in ind:
  #  print(l)
  #  cxc = np.delete(cxc,l)
  #  cyc = np.delete(cyc,l)
  #  crc = np.delete(crc,l)
plt.matshow(c)
plt.scatter(xv,yv,color='w')
for k in range(len(cel)):
        #plt.scatter(xc[k],yc[k],color=rc[k],s=15)'
  if new_list1[k].death == 0 and new_list1[k].radio == 0:
    plt.scatter(cel[k].x,cel[k].y,color=cel[k].color,s=15)
    t2x.append(cel[k].x)
    t2y.append(cel[k].y)
try:
  if len(t2x) > 2:
    allPoints=np.column_stack((t2x,t2y))
    hull = ConvexHull(allPoints)
    print('area=' + str(hull.volume))
    for simplex in hull.simplices:
      plt.plot(allPoints[simplex, 0], allPoints[simplex, 1], 'k-')
except Exception:
  print('1')
plt.show()

"""# **without time rario therapy**"""

import random
import math
def rt(dose,obj):

  cxc = np.copy(xc)
  cyc = np.copy(yc)
  crc = np.copy(rc)
  g2 = 18
  g1 = 0
  s = 12
  m = 22
  alpha = 0.2
  beta = 0
  sfd = math.e**(-(alpha*dose + beta*dose*dose))
  #sfd = 0.37
  #ind = []
  t1x = []
  t1y = []
  #for j in range(len(cxc)):
  for i in obj:
    if i.death == 1 and i.radio == 1:
      continue
    receivedradio = 0
    #xr = cxc[j]
    #yr = cyc[j]
    #if age[xr,yr] >= g2 and age[xr,yr] < m :
    if i.age >= g2 and i.age < m :
      receivedradio = random.random()*1.25
    elif i.age >= g1 and i.age < g2:
      receivedradio = random.random()*0.75
    elif i.age >= s and i.age < g2:
      receivedradio = random.random()
    if receivedradio > sfd:
      #for i in range(len(cxc)):
      #if cxc[i] == xr and cyc[i] == yr:
      ind.append(i)
      i.radio = 1
      for d in obj:
        if (i.x,i.y) == (d.x,d.y):
          d.radio = 1
          #cxc = np.delete(cxc,i)
          #cyc = np.delete(cyc,i)
          #break
  #ind.sort()
  #ind.reverse()
  #for l in ind:
  #  cxc = np.delete(cxc,l)
  #  cyc = np.delete(cyc,l)
  #  crc = np.delete(crc,l)
  #plt.matshow(c)
  #plt.scatter(xv,yv,color='w')
  #for k in range(len(cxc)):
        #plt.scatter(cxc[k],cyc[k],color=crc[k],s=10)
  
  for k in range(len(obj)):
        #plt.scatter(xc[k],yc[k],color=rc[k],s=15)'
    if obj[k].death == 0 and obj[k].radio == 0:
      #plt.scatter(obj[k].x,cel[k].y,color=obj[k].color,s=15)
      t1x.append(obj[k].x)
      t1y.append(obj[k].y)
    #elif obj[k].death == 0 and obj[k].radio==1:
      #plt.scatter(obj[k].x,obj[k].y,color = (0.4, 0.1, 0.3, 0.3),s=15)
        #xc.append(cel[k].x)
        #yc.append(cel[k].y)
  try:
    if len(t1x) > 2:
      allPoints=np.column_stack((t1x,t1y))
      hull = ConvexHull(allPoints)
        #print('area=' + str(hull.volume))
      volum = hull.volume
        #for simplex in hull.simplices:
          #plt.plot(allPoints[simplex, 0], allPoints[simplex, 1], 'k-')
  except Exception:
    print(1)
  return(volum)

"""# **q-learning**"""

clist = copy.deepcopy(cel)
qs = [are[-1]]
qa = [1]
a = qa[-1]
s = are[-1]
lr = 0.001

while (True):
  clist = copy.deepcopy(cel)
  reward = are[-1] - rt(qa[-1],clist)
  print(rt(qa[-1],clist))
  qa.append(a + lr*reward)
  if reward>= 50:
    break

h =0
for i in cel:
  if i.radio == 1:
    h = h + 1
print(h)

plt.plot(qa)

plt.plot(cs)
plt.plot(cc)

"""plot area"""

plt.plot(are , label = 'area')
plt.legend(loc="upper left")

plt.plot(age[xc[1],yc[1]])

xc,yc

c[i-1:i+2,j-1:j+2]

import numpy as np

np.log2(120)






