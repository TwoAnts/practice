#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def _merge_sort(arr, start, end):
    if end - start == 2:
        if arr[start] > arr[start+1]:
            arr[start], arr[start+1] = arr[start+1], arr[start]
    if end - start > 2:
        mid = (start + end - 1) // 2
        _merge_sort(arr, start, mid)
        _merge_sort(arr, mid, end)
        #print(start, mid, end, arr)
        tmp_arr = []
        i = start
        j = mid
        while i < mid and j < end:
            if arr[i] <= arr[j]:
                tmp_arr.append(arr[i])
                i += 1
            else:
                tmp_arr.append(arr[j])
                j += 1
        
        while i < mid:
            tmp_arr.append(arr[i])
            i += 1
        
        while j < end:
            tmp_arr.append(arr[j])
            j += 1
            
        arr[start:end] = tmp_arr[:]
        #print(start, mid, end, arr)

def merge_sort(arr):
    _merge_sort(arr, 0, len(arr))

def test():
    case1 = [1, 4, 2, 5, 8, 2, 9, 0, 3]
    print(case1)
    merge_sort(case1)
    print(case1)

if __name__ == '__main__':
    test()