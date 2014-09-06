# -*- encoding: utf-8 -*-
__author__ = 'wdwind'

from os import walk
from SingleFile.ClusterCenter import cluster_rank_rank


def wrapper(data_path, cluster_path, index_path, output_path):
    """
    A wrapper for the ClusterCenter.cluster_rank_rank.
    Clustering results post processing.
    Do double rank
        - rank by the number of points in the clusters
        - rank by the distances between every point in a cluster and the cluster center

    @param data_path:
    @param cluster_path:
    @param index_path:
    @param output_path:
    """

    files = []

    for (dir_path, dir_names, file_names) in walk(data_path):
        files.extend(file_names)
        break

    for filename in files:
        data_file = data_path + "\\" + filename
        cluster_file = cluster_path + "\\" + filename[:len(filename) - 4] + ".clusters"
        index_file = index_path + "\\" + filename[:len(filename) - 4] + ".index"
        output_file = output_path + "\\" + filename[:len(filename) - 4] + ".out"
        print data_path + "\\" + filename
        print cluster_path + "\\" + filename[:len(filename) - 4] + ".clusters"
        print index_path + "\\" + filename[:len(filename) - 4] + ".index"
        print output_path + "\\" + filename[:len(filename) - 4] + ".out"

        cluster_rank_rank(data_file, cluster_file, index_file, output_file)


if __name__ == '__main__':
    wrapper(u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\CSV",
            u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\results_C_clustering",
            u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\index",
            u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\Ranked_Clusters_Cut")

