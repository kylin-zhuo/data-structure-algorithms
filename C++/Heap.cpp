//
//  Heap.cpp
//  Algorithms
//
//  Created by Kylin on 5/26/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

#define MAX 200000
#define INFTY (1<<30)

class Heap
{
    
protected:
    
    // the array starts at index 1
    int n, heap[MAX + 1];
    
    void swap(int &a, int &b)
    {
        int temp = a;
        a = b;
        b = temp;
    }
    
    // starts from i-th element of the array and heapify downwards
    void maxHeapify(int i)
    {
        int l = 2 * i;
        int r = 2 * i + 1;
        
        int largest;
        
        // selects the max from {left, right, self}
        if (heap[l] > heap[i] && l <= n) {
            largest = l;
        } else {
            largest = i;
        }
        
        if (heap[r] > heap[largest] && r <= n) {
            largest = r;
        }
        
        if (largest != i) {
            swap(heap[i], heap[largest]);
            maxHeapify(largest);
        }
    }
    
    void inputHeap()
    {
        int i;
        cin>>n;
        
        for (i = 1; i <= n; i++) {
            cin>>heap[i];
        }
        
    }
    
public:
    
    int main()
    {
        
        // don't add the parameter n here! it is not this.n
        // int n;
        
        int i;
        inputHeap();
        
        for (i = n/2; i > 0; i--) {
            maxHeapify(i);
        }
        
        for (i = 1; i <= n; i++) {
            cout<<heap[i]<<" ";
        }
        
        cout<<endl;
        return 0;
    }
};


class PriorityQueue : Heap
{
    
protected:
    
    int extract()
    {
        if (n < 1) {
            return -INFTY;
        }
        int maxv;
        maxv = heap[1];
        heap[1] = heap[n];
        n = n - 1;
        
        maxHeapify(1);
        return maxv;
    }
    
    void insert(int key)
    {
        n++;
        heap[n] = -INFTY;
        heapIncreaseKey(n, key);
        
    }
    
    void heapIncreaseKey(int i, int key)
    {
        if (key < heap[i]) {
            printf("error. the key is less than -inf");
            return;
        }
        
        heap[i] = key;
        while (i > 1 && heap[parent(i)] < heap[i]) {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
    
    int parent(int i)
    {
        return i / 2;
    }
    
public:
    
    int main()
    {
        int key;
        char op[20];
        
        while (1) {
            scanf("%s", op);
            if (op[0] == 'e' && op[1] == 'n') {
                break;
            }
            
            if (op[0] == 'i') {
                scanf("%d", &key);
                insert(key);
            }
            else {
                printf("%d \n", extract());
            }
        }
        
        return 0;
    }
    
    
};




