#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def heap_down(arr, end, par_k):
    while True:
        l_k = (par_k << 1) + 1
        r_k = (par_k << 1) + 2
        if l_k >= end: 
            break
            
        if r_k >= end:
            if arr[par_k] < arr[l_k]:
                arr[par_k], arr[l_k] = arr[l_k], arr[par_k]
                par_k = l_k
            break
        
        if (arr[par_k] < arr[l_k] 
            and arr[l_k] >= arr[r_k]):
            arr[par_k], arr[l_k] = arr[l_k], arr[par_k]
            par_k = l_k
        elif (arr[par_k] < arr[r_k] 
            and arr[r_k] >= arr[l_k]):
            arr[par_k], arr[r_k] = arr[r_k], arr[par_k]
            par_k = r_k
        else:
            break
        

def heap_up(arr, end):
    k = end - 1
    while k > 0:
        par_k = (k - 1) >> 1
        if arr[par_k] < arr[k]:
            arr[par_k], arr[k] = arr[k], arr[par_k]
        k = par_k
    
def heap_sort(arr):
    for i in range(2, len(arr)+1):
        heap_up(arr, i)
    
    for i in range(len(arr) - 1, 0, -1):
        if arr[0] > arr[i]:
            arr[0], arr[i] = arr[i], arr[0]
        heap_down(arr, i, 0)
        
def heap_sort2(arr):
    for i in range((len(arr)- 2) // 2, -1, -1):
        heap_down(arr, len(arr), i)
    
    for i in range(len(arr) - 1, 0, -1):
        if arr[0] > arr[i]:
            arr[0], arr[i] = arr[i], arr[0]
        heap_down(arr, i, 0)

def test():
    case1 = [1, 4, 2, 5, 8, 2, 9, 0, 3]
    print(case1)
    tmp = []
    tmp[:] = case1[:]
    heap_sort(tmp)
    print(tmp)
    print(case1)
    tmp[:] = case1[:]
    heap_sort2(case1)
    print(case1)

if __name__ == '__main__':
    test()