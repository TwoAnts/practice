#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def split_sort(arr, start, end):
    j = start
    for i in range(start, end - 1):
        if arr[end - 1] > arr[i]:
            if i != j:
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr[j], arr[end - 1] = arr[end - 1], arr[j]
    #print(start, end, arr)
    return j

def split_recursively(arr, start, end):
    if end - start <= 1:
        return
    split_index = split_sort(arr, start, end)
    split_recursively(arr, start, split_index)
    split_recursively(arr, split_index + 1, end)
    
def quick_sort(arr):
    split_recursively(arr, 0, len(arr))

def test():
    case1 = [1, 4, 2, 5, 8, 2, 9, 0, 3]
    print(case1)
    quick_sort(case1)
    print(case1)

if __name__ == '__main__':
    test()