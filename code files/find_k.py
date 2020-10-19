#first of all importing all the libraries needed

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans


#this is a function just to read the data from the CSV file and then return 2 lists i.e. data having points [ [x1,y1],[x2,y2].....]  and clrs having color labels of all
def read_data(path):
    file = open(path,"r")
    lines = file.readlines()
    print("Reading data file....")
    data = []
    clrs = []
    for i in range(1,len(lines)):
        data.append([float(lines[i].split(",")[0]),float(lines[i].split(",")[1])])
        clrs.append(lines[i].split(",")[2].strip())
    file.close()
    print("Reading data file done!")
    return (data,clrs)

#saving data into lists...
(X,colors) = read_data("final_points.txt")

# starting an empty list for saving WCSS of all models.
wcss = []

max_k = 20
print("Finding WCSS for all number of clusters....(It may take upto 30 secs..)")
for i in range(1, max_k):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=100, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
print("Done!...")
plt.plot(range(1, max_k), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
