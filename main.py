from math import ceil, floor
import os


def get_data_from_file(filename):
    lst = []
    with open(filename, "r") as f:
        lines = int(f.readline())
        lst = [float(f.readline()) for _ in range(lines)]
        lst.sort()
    return lst


def get_valid_files():
    return [x for x in os.listdir() if os.path.isfile(x)]


def print_intervals(start, end, interval, lst):
    start_idx = 0
    while start < end:
        count = 0
        for i in range(start_idx, len(lst)):
            num = lst[i]
            if num <= start:
                count += 1
            else:
                start_idx = i
                break
        print(f"{round(start, 2)}-{round(start+interval, 2)}:\t {count}")
        start += interval


def max_interval_for_bins(max_bins, data, use_int=True):
    spread = max(data) - min(data)
    interval = spread / max_bins
    if not use_int:
        return interval
    return ceil(interval)


if __name__ == "__main__":
    valid_files = get_valid_files()
    print(f"Enter filename containing target data: ({', '.join(valid_files)})")
    choice = input()
    if not choice.endswith(".txt"):
        choice += ".txt"
    if choice.lower() in [x.lower() for x in valid_files]:
        data = get_data_from_file(choice)
        interval = 0
        print("Calculate interval from bins (0) or enter interval: (1)")
        manual = int(input())
        if manual == 1:
            print("Enter interval: ")
            interval = float(input())
        else:
            print("Enter number of bins: ")
            bins = int(input())
            print("Use integer interval: y/n")
            use_int = input() == "y"
            interval = max_interval_for_bins(bins, data, use_int=use_int)
        start = floor(min(data))
        max_val = ceil(max(data))
        end = max_val + (max_val % interval)
        print_intervals(start, end, interval, data)
    else:
        print("File not found")
