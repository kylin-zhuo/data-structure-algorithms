//
//  Solution.cpp
//  Algorithms
//
//  Created by Kylin on 5/21/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>

#include <stack>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

class Solution_Stack
{
    int top, S[1000];
    
public:
    
    void push(int x)
    {
        S[++top] = x;
    }
    
    int pop()
    {
        top --;
        return S[top+1];
    }
    
    void inputHelper(char R[], int &n)
    {
        cout<<"Input the number of chars:"<<endl;
        cin>>n;
        
        cout<<"Input the chars:"<<endl;
        for(int i = 0; i < n; i++) cin>>R[i];
    }
    
    void main()
    {
        int a, b;
        top = 0;
        char s[100];
        int n;
        
        //cout<<"Input the expression:"<<endl;
        
        inputHelper(s, n);
        
        for(int i = 0; i < n; i ++)
        {
            if(s[i] == '+')
            {
                a = pop();
                b = pop();
                push(a + b);
            }
            else if(s[i] == '-')
            {
                b = pop();
                a = pop();
                push(a - b);
            }
            else if(s[i] == '*')
            {
                a = pop();
                b = pop();
                push(a * b);
            }
            else
            {
                push(int(s[i]) - 48);
            }
        }
        
        
        cout<<"The result: "<<pop()<<endl;
        
    }
};


class Solution_Queue
{
    
    const static int MAX = 10000;
    
    typedef struct pp {
        char name[100];
        int t;
    } P;
    
    P Q[MAX];
    int head, tail;
    
    
public:
    
    Solution_Queue()
    {
        
    }
    
    void initialize()
    {
        head = 0;
        tail = 0;
    }
    
    bool isEmpty()
    {
        return head == tail;
    }
    
    bool isFull()
    {
//        return head == (tail + 1) % MAX;
        return head == (tail + 1) % MAX;
    }
    
    void enqueue(P q)
    {
        if(isFull())
            cout<<"Error in enque."<<endl;
        
        Q[tail] = q;
        tail = (tail + 1) % MAX;
        
    }
    
    P dequeue()
    {
        P x = Q[head];
        head = (head + 1) % MAX;
        return x;
    }
    
    // Execute the job scheduling.
    void main()
    {
        
        initialize();
        
        // elaps: the time elapsed
        int elaps = 0;
        
        /*
         * q: the time slice
         * n: the number of jobs
         */
        int i, q, n;
        
        // u: the job that is being processed
        P u;
        
        printf("Input the # of jobs and the time slice: \n");
        scanf("%d %d", &n, &q);
        
        printf("Add the jobs: \n");
        for (i = 1; i <= n; i++) {
            scanf("%s", Q[i].name);
            scanf("%d", &Q[i].t);
        }
        
        head = 1;
        tail = n + 1;
        
        // The simulation
        while(head != tail)
        {
            u = dequeue();
            if(u.t <= q)
            {
                elaps += u.t;
                printf("%s %d\n", u.name, elaps);
            }
            else
            {
                elaps += q;
                u.t = u.t - q;
                enqueue(u);
            }
        }
    }
};



class LinkedList
{
    struct Node{
        int key;
        Node *next, *prev;
    };
    
    // The head node
    Node *nil;
    
    int size;
    int nInsert, nDelete;
    
public:
    
    Node* listSearch(int key)
    {
        Node* current = nil->next;
        while (current != nil && current->key != key) {
            current = current->next;
        }
        return current;
    }
    
    void init()
    {
        nil = (Node *)malloc(sizeof(Node));
        nil->next = nil;
        nil->prev = nil;
        
        size = nInsert = nDelete = 0;
    }
    
    void printList()
    {
        Node* current = nil->next;
        while(current != nil)
        {
            printf("%d", current->key);
            printf(" ");
            current = current->next;
        }
        
        printf("\n");
    }
    
    void insert(int key)
    {
        Node *x = (Node *) malloc(sizeof(Node));
        x->key = key;
        x->next = nil->next;
        nil->next->prev = x;
        nil->next = x;
        x->prev = nil;
    }
    
    void deleteNode(Node *t)
    {
        if(t == nil) return;
        t->prev->next = t->next;
        t->next->prev = t->prev;
        size -= 1;
        nDelete += 1;
        free(t);
        
    }
    
    void deleteKey(int key)
    {
        deleteNode(listSearch(key));
    }
    
    void main()
    {
        
        // two parameters to store the operation and key
        int key;
        char op[20];
        int i, n;
        
        init();
        
        printf("Input n: \n");
        scanf("%d", &n);
        
        printf("Input the operatios: \n");
        for (i = 0; i < n; i++) {
            scanf("%s %d", op, &key);
            if(op[0] == 'i')
            {
                insert(key);
                nInsert += 1;
                size += 1;
            }
            else if(op[0] == 'd')
            {
                deleteKey(key);
                
            }
        }
        
        printList();
    }
};



class AreaOnCross
{
public:
    
    int main()
    {
        stack<int> S1;
        stack<pair<int, int>> S2;
        
        string s;
        
        printf("Input the string: \n");
        scanf("%s", &s);
        
        cout<<s;
        
        return 0;
    }
    
};


class Allocation
{
    int n, k;
    int W[10000];
    
    /*
    int check(int p)
    {
        int count = 0, rest = p, i = 0, nCars = k;
        
        while (nCars > 0 && i < n) {
            if (W[i] < rest) {
                rest = rest - W[i];
                count++;
                i++;
            }
            else
            {
                rest = p;
                nCars = nCars - 1;
            }
        }
        return count;
    }
     */
    
    int check(int p)
    {
        int j = 0;
        for (int i = 0; i < k; i++) {
            int s = 0;
            while (s + W[j] <= p) {
                s += W[j];
                j++;
                if(j == n) return n;
            }
        }
        return j;
    }
    
    int solve()
    {
        int left = 0;
        int right = 10000;
        int mid;
        while (right > left + 1) {
            mid = (left + right) / 2;
            int v = check(mid);
            if (v >= n) {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }
        return right;
    }
    
public:
    int main()
    {
        cin>>n>>k;
        for (int i = 0; i < n; i++) {
            cin>>W[i];
        }
        int ans = solve();
        cout<<ans<<endl;
        
        return 0;
    }
    
};


