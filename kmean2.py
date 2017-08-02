from math import fsum
from math import sqrt
from collections import defaultdict
from functools import partial
from random import sample
from random import seed
from random import randrange

def mean(data):
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)


def dist(p, q, sqrt=sqrt, fsum=fsum, zip=zip):
    'Multi-dimensional euclidean distance'
    return sqrt(fsum((x1 - x2) ** 2.0 for x1, x2 in zip(p, q)))

def assign_data(centroids, data):
    'Assign data the closest centroid'
    d = defaultdict(list)
    for point in data:
        centroid = min(centroids, key=partial(dist, point))
        d[centroid].append(point)
    return dict(d)

def compute_centroids(groups):
    'Compute the centroid of each group'
    return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data, k=2, iterations=10):
    'Return k-centroids for the data'
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids

datapoints = [
    (10,41,23 ),
    (22,30,29 ),
    (11,42,5 ),
    (20,32,4 ),
    (12,40,12 ),
    (21,36,23 )
]
print('datapoint: {}'.format(datapoints))

print('k_means = {}'.format(k_means(datapoints, 2)))
