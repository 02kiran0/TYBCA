import matplotlib.pyplot as mtp
import pandas as pd
dataset=pd.read_csv('C:/Users/admin/Desktop/TYBCA R Prog 6426/Kiran Mundhe/mall.csv')
x=dataset.iloc[:, [3,4]].values
import scipy.cluster.hierarchy as shc
dendro=shc.dendrogram(shc.linkage(x,method="ward"))
mtp.title("dendogram plot")
mtp.ylabel("Euclidean Distances")
mtp.xlabel("customers")
mtp.show()
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidesn',linkage='ward')
y_pred=hc.fit_predict(x)
mtp.scatter(x[y_pred ==0,0],x[y_pred==0,1],s=100,c='blue',label='cluster 1')
mtp.scatter(x[y_pred==1,0],x[y_pred==1,1],s=100,c='green',label='cluster 2')
mtp.scatter(x[y_pred==2,0],x[y_pred==2,1],s=100,c='red',label='cluster 3')
mtp.scatter(x[y_pred==2,0],x[y_pred==2,1],s=100,c='cyan',label='cluster 4')
mtp.scatter(x[y_pred==2,0],x[y_pred==2,1],s=100,c='magenta',label='cluster 5')
mtp.title('Cluster of customer')
mtp.xlabel('Annual Income(k$)')
mtp.ylabel('Spending score(1-100)')
mtp.legend()
mtp.show()
