# 研究向量的形式
import numpy as np

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