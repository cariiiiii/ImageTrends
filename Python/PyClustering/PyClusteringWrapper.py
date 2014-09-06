__author__ = 'Feng Wang'

from os import walk, path
from SingleFile.PyClustering import clustering


def wrapper(input_path, output_path, k, dist):
    """
    A wrapper for PyClustering.clustering.
    Do K-means clustering for all data file in a folder.

    @param input_path: Data folder
    @param k: Number of centers in K-means
    @param dist: Distance measure
    """

    #my_path = r"C:\Users\D062988\Documents\DS\clustering008\CSV"
    files = []
    for (dir_path, dir_names, file_names) in walk(input_path):
        files.extend(file_names)
        break

    for filename in files:
        idx = clustering(input_path + "\\" + filename, k, dist, False)

        print "-- Write to output file"
        out = ','.join([str(i) for i in idx])
        parent = path.dirname(path.abspath(input_path))
        f = open(output_path + "\\" + filename.split(".")[0] + ".clusters", 'w')
        f.write(out)
        f.close()
        print "\n"


if __name__ == '__main__':
    wrapper(r"C:\Users\D062988\Documents\DS\clustering008\CSV", "", -1, 'b')
    ##    from timeit import Timer
    ##    t = Timer("test()", "from __main__ import test")
    ##    print t.timeit(number=1)