# -*- encoding: utf-8 -*-
__author__ = 'wdwind'

import numpy
import Pycluster
import collections
from operator import itemgetter
import time
from scipy.spatial.distance import cityblock

# Preserve top K results
K = 102


def cluster_rank_rank(data_file, cluster_file, index_file, output_path):
    """
    Do the "double rank" after the clustering.
    The first rank is to rank the clusters - big clusters go up, small clusters go down.
    The second rank is to rank the points in one cluster, the points close to the center go up,
    otherwise go down.

    @param data_file: CSV data file.
    @param cluster_file: Cluster id file.
    @param index_file: Index file. (This file map the binary code to the Map-Reduce output data item).
    @param output_path: Output path.
    """

    data = numpy.genfromtxt(data_file, delimiter=',')
    if len(data.shape) == 1:
        return

    cluster_id = numpy.genfromtxt(cluster_file, delimiter=',')

    with open(index_file) as f:
        # raw Map-Reduce output data
        raw_data = f.readlines()

    centroids, _ = Pycluster.clustercentroids(data, clusterid=cluster_id)

    # Sort clusters by the number of points in this cluster
    counter = collections.Counter(cluster_id)
    sorted_counter = sorted(counter.items(), key=itemgetter(1), reverse=True)

    used_clusters = [numpy.asscalar(numpy.int16(i[0])) for i in sorted_counter]
    #freq = [numpy.asscalar(numpy.int16(i[1])) for i in sorted_counter]
    #print used_clusters

    # ranked_clusters_2 structure:
    # cluster 1 -> points indices
    # cluster 2 -> points indices
    # ...
    ranked_clusters_2 = [[] for i in used_clusters]

    t2 = time.time()
    for ind, val in enumerate(cluster_id):
        ranked_clusters_2[int(val)].append(ind)
    ranked_clusters_2 = sorted(ranked_clusters_2, key=len, reverse=True)
    t3 = time.time()

    print (t3 - t2)

    del cluster_id

    # ranked_clusters_3 is basic the same as the ranked_clusters_2,
    # just the points in one cluster is sorted by their distances to the center
    ranked_clusters_3 = []

    for ind, cluster in enumerate(ranked_clusters_2):
        dist = [cityblock(data[i], centroids[ind]) for i in cluster]
        sorted_indices = [i[0] for i in sorted(enumerate(dist), key=lambda x: x[1])]
        ranked_clusters_3.append([cluster[i] for i in sorted_indices])

    del data
    del centroids

    # With a format same with Java version output file such as 198401.out
    output_result = [[str(len(i))] for i in ranked_clusters_3]

    for ind, cluster in enumerate(ranked_clusters_3):
        raw_data_in_cluster = [raw_data[i].split("\t")[1].strip() for i in cluster]
        output_result[ind].extend(raw_data_in_cluster[0:K])
        if ind > K:
            break

    # Write to output file
    f = open(output_path, 'w')
    for cluster in output_result:
        f.write("\t".join(cluster))
        f.write("\n")

    f.close()

    # Another choice, very slow
    #
    # rankedClusters = []
    #
    # t0 = TIME.time()
    # for k in used_clusters:
    #     rankedClusters.append([i for i, j in zip(count(), cluster_id) if j == k])
    # t1 = TIME.time()
    #
    # print rankedClusters
    #
    # print (t1-t0)


if __name__ == '__main__':
    cluster_rank_rank(r"D:\198401.csv",
                       r"D:\198401.clusters",
                       r"D:\198401.index",
                       r"test")