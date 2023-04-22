"""Program for profiling stddev.py"""

#!/usr/bin/env python3
import cProfile
import pstats
import stddev

if __name__ == "__main__":
    with cProfile.Profile() as profile:
        stddev.convert_string()
        stddev.arithmetic_mean()
        stddev.variance()
        stddev.standard_deviation()
    
    results = pstats.Stats(profile)
    results.strip_dirs().sort_stats(pstats.SortKey.TIME)
    results.print_stats("ivsmath.py")