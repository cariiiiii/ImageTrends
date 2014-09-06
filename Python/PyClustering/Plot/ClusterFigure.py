# -*- encoding: utf-8 -*-
__author__ = 'Feng Wang'

import numpy
from matplotlib import mlab
import Pycluster
import pylab
import collections
from operator import itemgetter


def cluster_figure(data_file, cluster_file, output_path):
    """
    Draw the figure of the clusters (top 10 clusters in 2 dimensions).

    @param data_file: Data file in a month (CSV binary file).
    @param cluster_file: Clustering result file.
    @param output_path: Output path to save the figure.
    @return: none
    """

    # The time of the month, for example, 200311
    time = data_file.split("\\")
    time = time[len(time) - 1]
    time = time.split(".")
    time = time[0]

    # Read data.
    data = numpy.genfromtxt(data_file, delimiter=',')
    cluster_id = numpy.genfromtxt(cluster_file, delimiter=',')

    # If the number of data points is 1, return.
    if len(data.shape) == 1:
        return [-1]

    # Sort the cluster by the number of points in this cluster.
    counter = collections.Counter(cluster_id)
    sorted_counter = sorted(counter.items(), key=itemgetter(1), reverse=True)

    # Extract the clusters id and the freq in different lists
    used_clusters = [numpy.asscalar(numpy.int16(i[0])) for i in sorted_counter]
    freq = [numpy.asscalar(numpy.int16(i[1])) for i in sorted_counter]

    # fig1, (the size of clusters)'s distribution
    fig1 = pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
    pylab.xlim(-len(freq) / 50, len(freq) + len(freq) / 50)
    pylab.ylim(0, max(freq) + 1)
    pylab.plot(freq, marker='.', markersize=4)
    pylab.xlabel("Ranked clusters")
    pylab.ylabel("Number of points in the cluster")
    pylab.title("Figure of clusters points distribution in " + time)
    #pylab.show()
    fig1.savefig(output_path + "\\" + time + '_cluster_stat.png', dpi=80)
    pylab.close()

    # k is the top clusters to be showed
    k = 10
    if len(sorted_counter) < k:
        k = len(sorted_counter)

    used_clusters = used_clusters[0:k]

    # Get the centroids for each cluster
    centroids, _ = Pycluster.clustercentroids(data, clusterid=cluster_id)

    # If the number of data is smaller than the dimension of the data point, then return.
    # Because then we need to do the PCA, if the number of data is too small, the PCA will
    # fail.
    if len(data) < len(data[0]):
        print len(data)
        print len(data[0])
        return

    # PCA
    data_pca = mlab.PCA(data)
    cutoff = data_pca.fracs[1]
    data_2d = data_pca.project(data, minfrac=cutoff)
    centroids_2d = data_pca.project(centroids, minfrac=cutoff)

    color = ['#2200CC', '#D9007E', '#660066', '#FFFF00', '#FF6600', '#0099CC',
             '#8900CC', '#140A00', '#6B6B47', '#66FF66', '#FF99CC', '#0055CC']

    # fig2, figure of top k clusters in 2-D
    fig2 = pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
    legend = []
    num = 0
    for i in used_clusters:
        temp = pylab.scatter(data_2d[cluster_id == i, 0], data_2d[cluster_id == i, 1], color=color[num % 12])
        legend.append(temp)
        num += 1

    pylab.plot(centroids_2d[used_clusters, 0], centroids_2d[used_clusters, 1], 'sg', markersize=8)
    pylab.legend(legend, range(1, k + 1))
    pylab.xlabel("Feature 1")
    pylab.ylabel("Feature 2")
    pylab.title("Top " + str(k) + " clusters in " + time)
    #pylab.show()
    fig2.savefig(output_path + "\\" + time + '_cluster_plot.png', dpi=80)
    pylab.close()


if __name__ == '__main__':
    cluster_figure(r"D:\198401.csv",
                   r"D:\198401.clusters",
                   r"")
    ##    from timeit import Timer
    ##    t = Timer("test()", "from __main__ import test")
    ##    print t.timeit(number=1)