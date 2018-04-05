//
//  ShellSort.cpp
//  Algorithms
//
//  Created by Kylin on 5/21/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;



class ShellSort{
    
public:
    
    const static int MAX = 100000;
    
    long long cnt;
    int l;
    int A[MAX];
    int n;
    
    vector<int> G;
    
    // The insertion sort with gap g
    void insertionSort(int A[], int n, int g)
    {
        for (int i = g; i < n; i++) {
            int v = A[i];
            int j = i - g;
            while (j >= 0 && A[j] > v) {
                A[j+g] = A[j];
                j = j - g;
                cnt = cnt + 1;
            }
            A[j+g] = v;
        }
    }
    
    void shellSort(int A[], int n)
    {
        // generate the array G = {1, 4, 13, 40, 121, 364, 1093, ...}
        for (int h = 1; ; ) {
            if(h > n) break;
            G.push_back(h);
            h = 3 * h + 1;
        }
        
        int i;
        
        for (i = int(G.size()) - 1; i >= 0; i--) {
            insertionSort(A, n, G[i]);
        }
    }
    
    
    void run()
    {
        cout<<"input N:"<<endl;
        cin>>n;
        
        cout<<"input the numbers:"<<endl;
        for (int i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        cnt = 0;
        
        shellSort(A, n);
        
        for (int i = 0; i < n; i++) {
            cout<<A[i]<<" ";
        }
        cout<<endl;
        
        
    }

};








