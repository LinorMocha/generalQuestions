#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#
def get_users_under_max_span(users, max_span):
    users_under_max_span = set()
    for user_id in users.keys():
        try:
            user = users[user_id]
            if (int(user["sign-out"]) - int(user["sign-in"])) <= max_span:
                users_under_max_span.add(user_id)
        except KeyError:
            continue
    return users_under_max_span


def processLogs(logs, maxSpan):
    users = {}
    for log in logs:
        (user_id, timestamp, action) = log.split(' ')
        try:
            users[user_id][action] = timestamp
        except KeyError:
            users[user_id] = {action: timestamp}
    return get_users_under_max_span(users, maxSpan)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())
    # logs = ['99 1 sign-in', '100 10 sign-in', '50 20 sign-in', '100 15 sign-out', '50 26 sign-out',
    #         '99 2 sign-out']
    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
