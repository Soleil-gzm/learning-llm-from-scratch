
import numpy as np
# 研究向量的形式
print("研究向量的形式:")
asList = [1,2,3]
asArray=np.array([1,2,3])
rowVec = np.array([[1,2,3]])
colVec = np.array([[1],[2],[3]])

print(asList)
print(asArray)
print(rowVec)
print(colVec)

print(f'asList:{np.shape(asList)}')
print(f'asArray:{asArray.shape}')
print(f'rowVec:{rowVec.shape}')
print(f'colVec:{colVec.shape}')


# 向量的加减法
print("\n向量的加减法:")
v=np.array([4,5,6])
w=np.array([10,20,30])
u=np.array([0,3,6,9])
vPlusW=v+w
print(vPlusW)
# uPlusW=u+v


# 向量-标量的乘法
print("\n向量-标量的乘法:")
s=2
a=[3,4,5]
b=np.array(a)
print(a*s)
print(b*s)

# 标量-向量的加法
print("向量-标量的加法:")
x=np.array([3,6])
print("标量-向量的加法:",s+x)

# Python中的向量广播
print("\nPython中的向量广播:")
n=np.array([[1,2,3]]).T
m=np.array([[10,20]])
print(m)
print(n)
print("\n广播加法:\n",m+n)

# 向量的幅度和单位向量
print("\n向量的幅度和单位向量:\n")

