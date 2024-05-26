#Lab 12 Train AND Gate using Hebbian Learning
import numpy as np
b=0
alpha=1

def hebb_train(x,y,w):
  for i in range(0,len(x)):
    global b
    dw=alpha*x[i]*y[i]
    db=alpha*y[i]
    w=np.add(w,dw)
    b=b+db
  return w

def hebb_predict(x,w):
  z=x*w
  tx=sum(z)
  y=f(tx)
  return y

def f(x):
  if(x>b):
    return 1
  else:
    return 0

trainx=np.array([[1,1],[1,0],[0,1],[0,0]])
trainy=np.array([1,0,0,0])
wt=np.array([0,0])
print("+++++++++")
for i in range(1,5):
  print("Epoch#",i)
  wt=hebb_train(trainx,trainy,wt)
  print("Weights:")
  print(wt)
testx=np.array([[1,1],[1,0],[0,1],[0,0]])
for x in testx:
  out=hebb_predict(x,wt)
  print("Input:",x)
  print("Output:",out)
