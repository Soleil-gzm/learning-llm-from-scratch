import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-1))
x=np.random.randn(10,2)
print("x=",x)
W1=np.random.randn(2,4)
print("W1=",W1)
b1=np.random.randn(4)
print("b1=",b1)
W2=np.random.randn(4,3)
print("W2=",W2)
b2=np.random.randn(3)
print("b2=",b2)

h=np.dot(x,W1)+b1
print('h=',h)
a=sigmoid(h)
print("a=",a)
s=np.dot(a,W2)+b2
print("s=",s)