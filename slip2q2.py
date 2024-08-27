import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
data=make_blobs(n_samples=300,n_features=2,centers=5,cluster_std=1.8,random_state=101)
data[0].shape
data[1]
plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='brg')
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=5)
kmeans.fit(data[0])
kmeans.cluster_centers_
kmeans.labels_f,(ax1,ax2)=plt.subplots(1,2,sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='brg')
ax2.set_title("Orignal")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='brg')
plt.show()
