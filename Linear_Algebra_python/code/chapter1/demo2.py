# 向量的加减法
import numpy as np

v=np.array([4,5,6])
w=np.array([10,20,30])
u=np.array([0,3,6,9])
vPlusW=v+w
print(vPlusW)
# uPlusW=u+v


# 向量-标量的乘法
s=2
a=[3,4,5]
b=np.array(a)
print(a*s)
print(b*s)

# 标量-向量的加法

x=np.array([3,6])
print("标量-向量的加法:",s+x)