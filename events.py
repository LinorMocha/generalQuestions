#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxEvents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY duration
#

def maxEvents(arrival, duration):
    # the first event can append
    max_events = 1
    min_current_end = arrival[0] + duration[0]
    for company_index in range(1, len(arrival)):
        current_end = arrival[company_index] + duration[company_index]
        # if two group arrived at the same time
        if arrival[company_index] == arrival[company_index - 1]:
            if current_end < min_current_end:
                min_current_end = current_end
                continue
        # both event can append
        if min_current_end <= arrival[company_index]:
            min_current_end = arrival[company_index] + duration[company_index]
            max_events += 1
    return max_events


if __name__ == '__main__':
    arrival = [1, 1, 1, 1, 4]
    duration = [10, 3, 6, 4, 2]
    print(maxEvents(arrival, duration))
