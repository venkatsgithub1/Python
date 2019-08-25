for _ in range(int(input().strip())):
    list_len = int(input().strip())
    list_data = list(map(int, input().strip().split(" ")))
    times_to_rotate = int(input().strip())
    print(*(list_data[times_to_rotate % list_len:] + list_data[:times_to_rotate % list_len]))
"""
Usage:
1
5
1 2 3 4 5
2
3 4 5 1 2
"""