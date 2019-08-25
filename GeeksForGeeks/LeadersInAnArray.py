for _ in range(int(input())):
    list_len = int(input())
    list_data = list(map(int, input().strip().split()))
    tmp_list = []
    current_max = -1
    for idx, data in enumerate(list_data):
        if data > current_max:
            while len(tmp_list) != 0 and data > tmp_list[-1]:
                tmp_list.pop()
        current_max = data
        tmp_list.append(data)
    print(*tmp_list)

"""
Usage:
1
6
16 17 4 3 5 2
17 5 2
"""
