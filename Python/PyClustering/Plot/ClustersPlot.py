# -*- encoding: utf-8 -*-
__author__ = 'Feng Wang'

from os import walk
from ClusterFigure import cluster_figure


def wrapper(data_path, cluster_path, output_path):
    """
    A wrapper for the ClusteringPlot.clustering_plot.
    Draw figures for all data file in a folder.

    @param data_path: Input data path.
    @param cluster_path: Corresponding cluster path.
    @param output_path: Output path
    """

    files = []

    # Get all file names
    for (dir_path, dir_names, file_names) in walk(data_path):
        files.extend(file_names)
        break

    # Draw figures for each file
    for filename in files:
        print data_path + "\\" + filename
        cluster_figure(data_path + "\\" + filename,
                        cluster_path + "\\" + filename[:len(filename) - 4] + ".clusters",
                        output_path)

if __name__ == '__main__':
    wrapper(u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\CSV",
            u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\results_C_clustering",
            u"C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\figures")
##    from timeit import Timer
##    t = Timer("test()", "from __main__ import test")
##    print t.timeit(number=1)