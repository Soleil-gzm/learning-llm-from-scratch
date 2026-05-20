
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
print("\n向量的幅度和单位向量:")
v_m=np.array([1,2,3,7,8,9])
v_dim=len(v)  # dimensionality
v_mag=np.linalg.norm(v_m)

print("v_m:",v_m)
print("v_dim:",v_dim)
print("v_mag:",v_mag)

# 向量点积 dot product or inner product
print("\n向量点积:")
v_dot = np.array([1,2,3,4])
w_dot = np.array([5,6,7,8])
product = np.dot(v_dot,w_dot)
print("dot(v_dot,w_dot) =",product)

# 两个向量和的点积分配律：
a_dot = np.array([0,1,2])
b_dot = np.array([3,5,8])
c_dot = np.array([13,21,34])

# 点积满足分配律
print("\n点积满足分配律:")
res1 = np.dot(a_dot,b_dot+c_dot)
res2 = np.dot(a_dot,b_dot)+np.dot(a_dot,c_dot)
print("dot(a_dot,b_dot+c_dot):",res1)
print("dot(a_dot,b_dot)+np.dot(a_dot,c_dot):",res2)