__author__ = 'wdwind'

import numpy
from matplotlib import mlab
import Pycluster
from pylab import plot, show, scatter


def set_k(number, k):
    """
    Set k in K-means algorithm.

    @param number: c of data points
    @param k: pre-defined k
    @return: k
    """
    if k == -1:
        k = int(0.5 * number)
    if k > 5000:
        k = 5000
    return k


def method_name(number):
    """
    Set number of iterations.

    @param number: Number of data points.
    @return: Number of iterations.
    """

    if len(number) < 1000:
        ite_num = 10
    else:
        ite_num = 1
    return ite_num


def clustering(file_path, k, dist_measure, PLOT):
    """
    Do the K-means clustering for input data.

    @param file_path: Input data file.
    @param k: Number of centers in K-means algorithm.
    @param dist_measure: Distance measure (in this case, we use Manhattan distance).
    @param PLOT: Bool variable, check if plot the result (set it as True only in testing).
    @return: Clusters id for all data points in the input data file.
    """

    data = numpy.genfromtxt(file_path, delimiter=',')

    if len(data.shape) == 1:
        return [-1]

    print "-- Processing file: " + file_path + "  -- Data points: " + str(len(data))
    print "-- Start clustering"

    k = set_k(len(data), k)
    ite_num = method_name(len(data))

    # Do the K-means clustering
    cluster_id, _, _ = Pycluster.kcluster(data, nclusters=k, mask=None, weight=None, transpose=0, npass=ite_num,
                                          method='a', dist=dist_measure, initialid=None)

    if PLOT is False:
        return cluster_id

    # Draw the clustering result plot.
    centroids, _ = Pycluster.clustercentroids(data, clusterid=cluster_id)

    if PLOT:
        data_pca = mlab.PCA(data)
        cutoff = data_pca.fracs[1]
        data_2d = data_pca.project(data, minfrac=cutoff)
        centroids_2d = data_pca.project(centroids, minfrac=cutoff)
    else:
        data_2d = data
        centroids_2d = centroids

    color = ['#2200CC', '#D9007E', '#FF6600', '#FFCC00', '#ACE600', '#0099CC',
             '#8900CC', '#FF0000', '#FF9900', '#FFFF00', '#00CC01', '#0055CC']

    for i in range(k):
        scatter(data_2d[cluster_id == i, 0], data_2d[cluster_id == i, 1], color=color[i % 12])

    plot(centroids_2d[:, 0], centroids_2d[:, 1], 'sg', markersize=8)
    show()

    return cluster_id