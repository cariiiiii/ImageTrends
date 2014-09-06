# -*- encoding: utf-8 -*-
__author__ = 'Feng Wang'

import PyClusteringWrapper
import ClusterPlotWrapper
import ClusterCenterWrapper


def main():
    """
    Main function. Still lots of refactoring can be done. But I don't want to do anymore...

    """

    # CSV_path = u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash_test\\CSV"
    # #CSV_path = CSV_path.decode("GBK")
    # clusters_id_path = u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash_test\\clusters_id"
    # #clusters_id_path = clusters_id_path.decode("GBK")

    PyClusteringWrapper.wrapper(
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\CSV",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\clusters_id",
        -1,
        'b')
    ClusterPlotWrapper.wrapper(
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\CSV",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\clusters_id",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\figures")
    ClusterCenterWrapper.wrapper(
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\CSV",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\clusters_id",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\index",
        u"D:\\F\\课件2\\IN4144 Data Science (2013-2014 Q4)\\project\\DATA\\clustering008\\pHash\\Ranked_Clusters_Cut")


if __name__ == '__main__':
    main()