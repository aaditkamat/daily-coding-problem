"""
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""

from time import time
from random import randint, choice
from logging import debug


def busiest_period(data_entries):
    curr_people, max_people, start_timestamp, end_timestamp = 0, 0, data_entries[0]["timestamp"], data_entries[-1]["timestamp"]
    for i in range(len(data_entries)):
        curr_entry = data_entries[i]
        if curr_entry["type"] == "entry":
            curr_people += curr_entry["count"]
        else:
            if curr_people > max_people:
                max_people = curr_people
                end_timestamp = curr_entry["timestamp"]
                prev_entry = data_entries[i - 1]
                start_timestamp = prev_entry["timestamp"]
            curr_people -= curr_entry["count"]
    return (start_timestamp, end_timestamp)


if __name__ == '__main__':
    number_of_entries = randint(1, 20)
    start_time = int(time())
    data_entries = [{"timestamp": start_time, "count": randint(1, 20), "type": "entry"}]
    curr_people = data_entries[-1]["count"]
    for i in range(1, number_of_entries - 1):
        start_time += randint(2, 50)
        entry_type = choice(["entry", "exit"])
        if entry_type == "entry":
            data_entries.append({"timestamp": start_time, "count": randint(2, 20), "type": "entry"})
            curr_people += data_entries[-1]["count"]
        else:
            data_entries.append({"timestamp": start_time, "count": randint(1, curr_people) if curr_people > 1 else 1, "type": "exit"})
            curr_people -= data_entries[-1]["count"]
    start_time += randint(2, 50)
    data_entries.append({"timestamp": start_time, "count": sum(map(lambda x: x["count"] if x["type"] == "entry" else -x["count"], data_entries)), "type": "exit"})
    # Uncomment below to check the data entries
    # print(data_entries)
    print(busiest_period(data_entries))
