import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  

import numpy as np
rng = np.random.default_rng()
np.set_printoptions(precision=2)

########################################

distributions = [
    ((5,5,5), 2),
    ((15,2,6), 4),
    ((2,8,2), 4),
]
n_points = 90

########################################

dists = []
for parameters in distributions:
    points = rng.normal(parameters[0], parameters[1], [n_points,3])
    dists.append(points)
all_dists = np.concatenate(dists, axis=0)

########################################

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = 'rgbov'
for idx, dist in enumerate(dists):
    ax.scatter(dist[:,0], dist[:,1], dist[:,2], c=colors[idx], marker='o')

plt.savefig("ground_truth.png")

########################################

from sklearn.cluster import KMeans

########################################

kmeans = KMeans(init="k-means++", n_clusters=len(distributions), n_init=4, random_state=0)
kmeans.fit_predict(all_dists)
kmeans.cluster_centers_

########################################

for idx1 in range(len(distributions)):
    best_pick = None
    best_distance = np.inf
    for idx2 in range(len(distributions)):
        predicted = kmeans.cluster_centers_[idx1]
        actual = np.array(distributions[idx2][0])
        distance = np.linalg.norm(predicted-actual)
        if distance < best_distance:
            best_pick = actual
            best_distance = distance
    print("Actual: {:}, Predicted: {:}, Error: {:.2}".format(best_pick, predicted, best_distance))


########################################

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = 'rgbov'
for idx, dist in enumerate(dists):
    ax.scatter(dist[:,0], dist[:,1], dist[:,2], c=colors[idx], marker='o')
ax.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,2], c='black', marker='+', s=105, zorder=200)
plt.savefig("clusters.png")
