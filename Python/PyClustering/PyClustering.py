__author__ = 'Feng Wang'

import numpy
from matplotlib import mlab
import Pycluster
from pylab import plot, show, scatter
from os import walk, path


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


def wrapper(my_path, k, dist):
    """
    A wrapper for clustering.
    Do K-means clustering for all data file in a folder.

    @param my_path: Data folder
    @param k: Number of centers in K-means
    @param dist: Distance measure
    """

    #my_path = r"C:\Users\D062988\Documents\DS\clustering008\CSV"
    files = []
    for (dir_path, dir_names, file_names) in walk(my_path):
        files.extend(file_names)
        break

    for filename in files:
        idx = clustering(my_path + "\\" + filename, k, dist, False)

        print "-- Write to output file"
        out = ','.join([str(i) for i in idx])
        parent = path.dirname(path.abspath(my_path))
        f = open(parent + "\\results_C_clustering\\" + filename.split(".")[0] + ".clusters", 'w')
        f.write(out)
        f.close()
        print "\n"


if __name__ == '__main__':
    wrapper(r"C:\Users\D062988\Documents\DS\clustering008\CSV", -1, 'b')
    ##    from timeit import Timer
    ##    t = Timer("test()", "from __main__ import test")
    ##    print t.timeit(number=1)