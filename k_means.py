from math import fsum
from math import sqrt
from collections import defaultdict
from functools import partial
from random import sample
from random import seed
from random import randrange
from pprint import pprint


def mean(data):
    data = list(data)
    return fsum(data) / len(data)

def dist(p, q, fsum=fsum, sqrt=sqrt, zip=zip):
    return sqrt(fsum([(x-y)**2 for x, y in zip(p, q)]))

def assign_data(centroids, data):
    '''groups data points around the centroid'''
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return d

def compute_centroid(groups):
    '''finds centroid of each goup and returns list of centroids'''
    return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data, k=2, iteration=100):
    '''k in the number of abitrary centroids'''
    data = list(data)
    centroids = sample(data, k)
    for i in range(iteration):
        labeled = assign_data(centroids, data)
        centroids = compute_centroid(labeled.values())
    return centroids


if __name__ == "__main__":
    # seed(1234)
    population = [randrange(10,100,1) for i in range(100)]
    #print('population = {}'.format(population))
    datapoints = [tuple(sample(population, 3)) for i in range(10)]
    datapoints = [
        (10,41,23 ),
        (22,30,29 ),
        (11,42,5 ),
        (20,32,4 ),
        (12,40,12 ),
        (21,36,23 )
    ]
    print('datapoint: {}'.format(datapoints))
    centroids = k_means(datapoints, 3)
    print('k_means = {}'.format(centroids))

    # group the datapoints around these centers

    groups = dict(assign_data(centroids, datapoints))

    #print('Groups: {}'.format(groups, width=40))
    # if k is large we end up by  finding all data is it own center, data very different
    # if k is small we end up by  finding all data is very alike
    for k in groups:
        print('{} : {}'.format(k, groups[k]))
