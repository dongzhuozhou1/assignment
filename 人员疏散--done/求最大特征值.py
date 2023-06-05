import numpy as np

#输入矩阵
A = np.array([[1, 1/2, 1/3, 1/4, 1/2, 1/2, 1/3, 1/4],
              [2, 1, 1/2, 1/3, 1/2, 2, 1/2, 1/3],
              [3, 2, 1, 1/2, 1/2, 2, 1/2, 1/3],
              [4, 3, 2, 1, 1/2, 3, 1, 1/2],
              [2, 2, 2, 2, 1, 1, 1/2, 1/3],
              [2, 1, 1/2, 1/3, 1, 1, 1/2, 1/3],
              [3, 2, 2, 2, 2, 2, 1, 1/2],
              [4, 3, 3, 3, 3, 3, 2, 1]])
  
#求解特征值即特征向量
lamda = np.linalg.eig(A)

for i in range(len(lamda[0])):
    print('特征值：{0}\n对应的特征向量：\n{1}\n'.format(lamda[0][i], np.transpose([lamda[1][:,i]])))

index = np.argmax(lamda[0])
lamda_max = np.real(lamda[0][index])
vector = lamda[1][:,index]

vector_final = np.transpose((np.real(vector)))

print('最大特征值为：{0}\n对应的特征向量：\n{1}'.format(lamda_max, vector_final))



      
                




