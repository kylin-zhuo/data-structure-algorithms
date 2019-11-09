//
//  InsertionSort.cpp
//  Algorithms
//
//  Created by Kylin on 5/20/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <limits.h>

using namespace std;

static const int MAX = 200000;

class Sorting{
    
    static int get_max(int a, int b)
    {
        if(a>b) return a;
        else return b;
    }
    
    static int get_min(int a, int b)
    {
        if(a>b) return b;
        else return a;
    }
    
    static void printArray(int R[], int n)
    {
        for(int i = 0; i < n; i++){
            cout<<R[i]<<" ";
        }
        cout<<endl;
    }
    
    static void inputHelper(int R[], int &n)
    {
        cout<<"Input the number of integers:"<<endl;
        cin>>n;
        
        cout<<"Input the numbers"<<endl;
        for(int i = 0; i < n; i++) cin>>R[i];
    }
    
    static void swap(int& a, int& b)
    {
        int temp;
        temp = a;
        a = b;
        b = temp;
    }
    
public:
    
    static void run1()
    {
        int R[MAX], n;

        inputHelper(R, n);
        
        int max_value = INT_MIN;
        int min_value = R[0];
        
        
        for(int i = 0; i < n; i++)
        {
            max_value = get_max(max_value, R[i] - min_value);
            min_value = get_min(min_value, R[i]);
        }
        
        cout<<"The maximal profit: "<<max_value<<endl;
    }

    static void insertionSort()
    {
        int R[MAX], n;
        
        inputHelper(R, n);
        
        int v;
        int j;
        
        for(int i = 1; i < n; i++)
        {
            v = R[i];
            j = i - 1;
            
            while(j >= 0 && R[j] > v)
            {
                R[j+1] = R[j];
                j = j - 1;
            }
            R[j+1] = v;
            
            printArray(R, n);
        }
        
    }
    
    static int bubbleSort()
    {
        
        int R[MAX], n;
        inputHelper(R, n);
        
        int sw = 0;
        
        bool flag = true;
        
        while(flag)
        {
            flag = false;
            for(int j = n-1; j > 0; j--)
            {
                if(R[j] < R[j-1])
                {
                    swap(R[j], R[j-1]);
                    sw = sw + 1;
                    flag = true;
                }
            }
            
            printArray(R, n);
        }
        
        return sw;
    }
    
    static void selectionSort()
    {
        int R[MAX], n;
        inputHelper(R, n);
        
        int minj, i, j;
        
        for(i = 0; i < n; i++)
        {
            minj = i;
            for(j = i; j < n; j++)
            {
                if(R[j] < R[minj]) minj = j;
            }
            
            swap(R[i], R[minj]);
            
            printArray(R, n);
        }
    }
    
    
    
};


