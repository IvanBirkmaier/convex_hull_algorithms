# coding: utf-8

import cProfile
import pstats
import time


# Performance messurement
def performance_measure(algo):
    # cProfile used to record # of function calls per algo
    profiler = cProfile.Profile()
    profiler.enable()
    start = time.time()
    # beide classen der algorithmen bekommen die performance methode, die nur den
    # algo ausführt ohne weitere extra sachen.
    hull = algo.performance()
    ende = time.time()
    profiler.disable()
    dauer = ende - start
    profiler.dump_stats("stats1")
    stats = pstats.Stats("stats1")
    return stats.total_calls, hull, dauer
