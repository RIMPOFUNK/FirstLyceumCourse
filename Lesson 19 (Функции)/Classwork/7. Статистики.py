import statistics as stat


def print_statistics(arr):
    if len(arr) == 0:
        print(0, 0, 0, 0, 0, sep='\n')
    else:
        print(len(arr), sum(arr) / len(arr), 
              min(arr), max(arr), stat.median(arr), sep='\n')
