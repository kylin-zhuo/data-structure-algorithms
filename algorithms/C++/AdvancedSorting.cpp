//
//  AdvancedSorting.cpp
//  Algorithms
//
//  Created by Kylin on 5/23/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>

using namespace std;

class MergeSort
{
    static const int MAX = 500000;
    static const int SENTINEL = 2000000000;
    
    
public:
    
    int l[MAX/2+2];
    int r[MAX/2+2];
    
    int cnt;
    
    MergeSort()
    {
        
    }
    
    void merge(int A[], int n, int left, int mid, int right)
    {
        int n1 = mid - left;
        int n2 = right - mid;
        
        for (int i = 0; i < n1; i++) {
            l[i] = A[left + i];
        }
        for (int i = 0; i < n2; i++) {
            r[i] = A[mid + i];
        }
        
        l[n1] = r[n2] = SENTINEL;
        
        int i = 0, j = 0;
        
        for (int k = left; k < right; k++) {
            cnt ++;
            if (l[i] <= r[j]) {
                A[k] = l[i];
                i++;
            } else {
                A[k] = r[j];
                j++;
            }
        }
    }
    
    void mergeSort(int A[], int n, int left, int right)
    {
        if (left < right - 1) {
            int mid = (left + right) / 2;
            mergeSort(A, n, left, mid);
            mergeSort(A, n, mid, right);
            merge(A, n, left, mid, right);
        }
    }
    
    void print(int A[], int n)
    {
        for (int i = 0; i < n; i++) {
            cout<<A[i]<<" ";
        }
        cout<<endl;
    }
    
    int main()
    {
        int A[MAX], n, i;
        cnt = 0;
        
        cin>>n;
        for (i = 0; i < n; i++) {
            cin>>A[i];
        }
        mergeSort(A, n, 0, n);
        
        print(A, n);
        cout<<cnt<<endl;
        
        return 0;
    }
};


class Partition
{
    int A[1000];
    int n;
    
    void swap(int &a, int &b)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }
    
    
    // print the array according to the specific format [target]
    void print(int A[], int n, int pos)
    {
        for (int i = 0; i < n; i++) {
            if(i == pos)
                cout<<"["<<A[i]<<"] ";
            else
                cout<<A[i]<<" ";
        }
        cout<<endl;
    }
    
    int partition(int A[], int p, int r)
    {
        int x = A[r];
        int i = p - 1;
        
        for (int j = p; j < r; j++) {
            if (A[j] <= x) {
                i = i + 1;
                swap(A[i], A[j]);
            }
        }
        swap(A[i+1], A[r]);
        
        return i+1;
    }
    
    
public:
    
    int main()
    {
        cin>>n;
        
        for (int i = 0; i < n; i++) {
            cin>>A[i];
        }
        
        int pos = partition(A, 0, n-1);
        
        print(A, n, pos);
        
        return 0;
    }
    
    
    
};




class QuickSort
{
    
    static const int MAX = 10000;
    static const int SENTINAL = 200000000;
    
    struct Card{
        char suit;
        int value;
    };
    
    struct Card l[MAX/2 + 2], r[MAX/2 + 2];
    
    void merge(struct Card A[], int n, int left, int mid, int right)
    {
        int i, j, k;
        int n1 = mid - left;
        int n2 = right - mid;
        
        for (i = 0; i < n1; i++) { l[i] = A[left + i]; }
        for (i = 0; i < n2; i++) { r[i] = A[mid + i]; }
        
        l[n1].value = r[n2].value = SENTINAL;
        i = j = 0;
        
        for (k = left; k < right; k++) {
            if (l[i].value <= r[j].value) {
                A[k] = l[i++];
            }
            else {
                A[k] = r[j++];
            }
        }
    }
    
    void mergeSort(struct Card A[], int n, int left, int right)
    {
        int mid;
        
        if(left + 1 < right)
        {
            mid = (left + right) / 2;
            mergeSort(A, n, left, mid);
            mergeSort(A, n, mid, right);
            merge(A, n, left, mid, right);
        }
    }
    
    
    int partition(struct Card A[], int n, int p, int r)
    {
        int i, j;
        struct Card t, x;
        
        x = A[r];
        
        i = p - 1;
        
        for (j = p; j < r; j++) {
            if (A[j].value <= x.value) {
                i++;
                t = A[i];
                A[i] = A[j];
                A[j] = t;
            }
        }
        t = A[i+1];
        A[i+1] = A[r];
        A[r] = t;
        
        return i + 1;
    }
    
    void quickSort(struct Card A[], int n, int p, int r)
    {
        int q;
        if (p < r) {
            q = partition(A, n, p, r);
            quickSort(A, n, p, q - 1);
            quickSort(A, n, q + 1, r);
        }
    }
    
public:
    
    int main()
    {
        int n, i, v;
        struct Card a[MAX], b[MAX];
        char s[10];
        int stable = 1;
        
        scanf("%d", &n);
        
        for (i = 0; i < n; i++) {
            scanf("%s %d", s, &v);
            a[i].suit = b[i].suit = s[0];
            a[i].value = b[i].value = v;
        
        }
        
        mergeSort(a, n, 0, n);
        quickSort(b, n, 0, n - 1);
        
        for (i = 0; i < n; i++) {
            if (a[i].suit != b[i].suit) {
                stable = 0;
            }
        }
        
        if (stable == 1) {
            printf("Stable\n");
        }
        
        else
        {
            printf("Not stable\n");
        }
        
        for (i = 0; i < n; i++) {
            printf("%c %d\n", b[i].suit, b[i].value);
        }
        return 0;
    }
};


class CountingSort
{
    static const int MAX = 200000;
    static const int VMAX = 10000;
    
public:
    
    int main()
    {
        unsigned short *a, *b;
        
        int c[VMAX + 1];
        int n, i, j;
        
        scanf("%d", &n);
        
        a = (unsigned short *) malloc(sizeof(unsigned short) * n + 1);
        b = (unsigned short *) malloc(sizeof(unsigned short) * n + 1);
        
        for (i = 0; i <= VMAX; i++) {
            c[i] = 0;
        }
        
        for (i = 0; i < n; i++) {
            scanf("%hu", &a[i+1]);
            c[a[i+1]]++;
        }
        
        for(i = 1; i < VMAX; i++)
            c[i] = c[i] + c[i-1];
        
        for (j = 1; j <= n; j++) {
            b[c[a[j]]] = a[j];
            c[a[j]]--;
        }
        
        for (i = 1; i <= n; i++) {
            if (i > 1) {
                printf(" ");
            }
            printf("%d", b[i]);
        }
        
        printf("\n");
        
        return 0;
    }
    
};



class InverseNumber
{
    
    static const int MAX = 500000;
    static const int SENTINEL = 2000000000;
    
    
    int l[MAX/2+2];
    int r[MAX/2+2];
    
    int nInversion;
    

    
    void merge(int A[], int n, int left, int mid, int right)
    {
        int n1 = mid - left;
        int n2 = right - mid;
        
        for (int i = 0; i < n1; i++) {
            l[i] = A[left + i];
        }
        for (int i = 0; i < n2; i++) {
            r[i] = A[mid + i];
        }
        
        l[n1] = r[n2] = SENTINEL;
        
        int i = 0, j = 0;
        
        for (int k = left; k < right; k++) {
            
            if (l[i] <= r[j]) {
                A[k] = l[i];
                i++;
            } else {
                nInversion += n1 - i;
                A[k] = r[j];
                j++;
            }
        }
    }
    
    void mergeSort(int A[], int n, int left, int right)
    {
        if (left < right - 1) {
            int mid = (left + right) / 2;
            mergeSort(A, n, left, mid);
            mergeSort(A, n, mid, right);
            merge(A, n, left, mid, right);
        }
        
        //return nInversion;
    }
    
public:
    
    InverseNumber()
    {
        nInversion = 0;
        
    }
    
    void main()
    {
        int a[MAX], n, i;
        
        cin>>n;
        for (i = 0; i < n; i++) {
            cin>>a[i];
        }
        
        mergeSort(a, n, 0, n);
        
        cout<<nInversion<<endl;
    }
    
    
};


