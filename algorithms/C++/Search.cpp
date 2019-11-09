//
//  Search.cpp
//  Algorithms
//
//  Created by Kylin on 5/22/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>
using namespace std;

class LinearSearch
{
    // linear search
    int search(int A[], int n, int key)
    {
        int i = 0;
        A[n] = key;
        while (A[i] != key) {
            i++;
        }
        return i != n;
    }
    
public:
    int main()
    {
        int i, n, A[10000+1], q, key, sum = 0;
        
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        scanf("%d", &q);
        for (i = 0; i < q; i++) {
            scanf("%d", &key);
            if (search(A, n, key)) {
                sum++;
            }
        }
        
        printf("%d\n", sum);
        return 0;
    }
    
};


class BinarySearch
{
    int A[100000], n;
    
    int binarySearch(int key)
    {
        int left = 0;
        int right = n;
        
        int mid;
        
        while (left < right) {
            mid = (left + right) / 2;
            if(key == A[mid]) return 1;
            else if(key > A[mid]) left = mid + 1;
            else right = mid;
        }
        
        return 0;
    }
    
public:
    int standardBS()
    {
        int i, q, k, sum = 0;
        scanf("%d", &n);
        
        for (i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        scanf("%d", &q);
        for (i = 0; i < q; i++) {
            scanf("%d", &k);
            if (binarySearch(k)) {
                sum ++;
            }
        }
        
        printf("%d \n", sum);
        
        return 0;
    }
    
    int searchWithSTL()
    {
        int A[10000], n;
        cin>>n;
        
        for (int i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        int q, k, sum = 0;
        cin>>q;
        
        for (int i = 0; i < q; i++) {
            scanf("%d", &k);
            if( *lower_bound(A, A + n, k) == k) sum++;
        }
        
        cout<<sum<<endl;
        
        return 0;
    }
    
    
    
};


#include <string>

class HashSet
{
    
#define M 1046527
#define NIL (-1)
#define L 14
    
    char H[M][L];
    
    // transfer A C G T to integers
    int getChar(char ch)
    {
        switch (ch) {
            case 'A':
                return 1;
            case 'B':
                return 2;
            case 'C':
                return 3;
            case 'D':
                return 4;
            default:
                return 0;
        }
    }
    
    // transfer the string to numeric and generate key
    long long getKey(char str[])
    {
        long long p = 1, i, sum = 0;
        for (i = 0; i < strlen(str); i++) {
            sum += p * getChar(str[i]);
            p = p * 5;
        }
        return sum;
    }
    
    // two hash functions
    int h1(int key) { return key % M; }
    int h2(int key) { return 1 + (key % (M - 1)); }
    
    // insert the string into the table
    int insert(char str[])
    {
        long long key, h, i;
        key = getKey(str);
        for (i = 0; ; i++) {
            h = (h1(key) + i * h2(key)) % M;
            
            // strcmp returns 0 if both strings are equal
            if (strcmp(H[h], str) == 0) {
                return 1;
            }
            else if (strlen(H[h]) == 0)
            {
                strcpy(H[h], str);
                return 0;
            }
        }
        
        return 0;
    }
    
    int find(char str[])
    {
        long long key, i, h;
        key = getKey(str);
        
        for (i = 0; ; i++) {
            h = (h1(key) + i * h2(key)) % M;
            if (strcmp(H[h], str) == 0) {
                return 1;
            }
            else if (strlen(H[h]) == 0) return 0;
        }
        
        return 0;
    }
    
    
public:
    
    int main()
    {
        int i, n;
        char str[L], com[9];
        
        for (i = 0; i < M; i++) {
            H[i][0] = '\0';
        }
        
        printf("input n: \n");
        scanf("%d", &n);
        
        
        printf("input the operations: \n");
        
        for (i = 0; i < n; i++) {
            scanf("%s %s", com, str);
            
            if (com[0] == 'i') {
                insert(str);
            }
            else if (com[0] == 'f')
            {
                if (find(str))
                    printf("yes\n");
                else
                    printf("no\n");
            }
            else
                printf("error");
        }
        
        return 0;
    }
};


#include <iostream>
#include <vector>
using namespace std;

class Iterator
{
    
    void print(vector<int> v)
    {
        vector<int>::iterator it;
        for (it = v.begin(); it != v.end(); it++) {
            cout<< *it;
        }
        cout<<endl;
    }
    
public:
    int main()
    {
        int N = 4;
        vector<int> v;
        
        printf("input the numbers: \n");
        
        for (int i = 0; i < N; i++) {
            int x;
            scanf("%d", &x);
            v.push_back(x);
        }
        
        print(v);
        
        vector<int>::iterator it = v.begin();
        
        *it = 3;
        it ++;
        (*it) ++;
        
        print(v);
        return 0;
    }
    
    
};


