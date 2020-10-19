#first of all importing all the

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans

#FUNCTION to read the data from the csv file
def read_data(path):
    file = open(path,"r")
    lines = file.readlines()

    data = []
    clrs = []
    for i in range(1,len(lines)):
        data.append([float(lines[i].split(",")[0]),float(lines[i].split(",")[1])])
        clrs.append(lines[i].split(",")[2].strip())
    file.close()

    return (data,clrs)


#readin values
(X,colors) = read_data("final_points.txt")

X = np.asarray(X)

#finding K means model using max iterations = 300 and K = 5
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)

#taking predictions of cluster number for all points...
pred_y = kmeans.fit_predict(X)


#finding all clusters' centers.
clusters = []

for i in range(5):
    clusters.append((kmeans.cluster_centers_[i, 0].round(2),kmeans.cluster_centers_[i, 1].round(2)))
print("Clusters' centers:",clusters)


#Writing the clusters center location into a file named as "center.txt"
print("Writing clusters to a file....")
file = open("centers.txt","w+")
file.write("X,Y\n")
for i in range(5):
    file.write(str(clusters[i][0])+","+str(clusters[i][1]) +"\n")

file.close()
print("Done..")


print("Writing all classified data into a file....")
#writing all the classified data into "clusterred_data.txt
file = open("clusterred_data.txt","w+")
file.write("X,Y,Color,Cluster No.\n")

for i in range(len(pred_y)):
    file.write(str(X[i][0]) + "," + str(X[i][1])+","+colors[i]+","+str(pred_y[i])+"\n")
file.close()
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()
print("Done...")