import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('headbrain.csv')
print(data.shape)
data.head()
X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values
meanx=np.mean(X)
meany=np.mean(Y)
n = len(X)
numer=0
denom=0
for i in range(n):
  numer+=(X[i]-meanx)*(Y[i]-meany)
  denom+=(X[i]-meanx)**2
slope=numer/denom
c=meany-(slope*meanx)
print(slope,c)
maxx=np.max(X)+100
minx=np.min(X)-100
x=np.linspace(minx,maxx,1000)
y=c+slope*x
plt.plot(x,y,color='#58b970',label='Regression line')
plt.scatter(X,Y,c='#ef5423', label='scatter plot')
plt.xlabel('head Size')
plt.ylabel('Brain weight')
plt.legend()
plt.show()
y_pred=c+(slope*X)
sst=0
ssr=0
for i in range(n):
  sst+=(y_pred[i]-meany)**2
  ssr+=(Y[i]-meany)**2
r2=sst/ssr
print(r2)