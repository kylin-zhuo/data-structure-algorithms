//
//  Graph.cpp
//  Algorithms
//
//  Created by Kylin on 5/27/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <list>
#include <queue>

using namespace std;

#define WHITE 0
#define GREY 1
#define BLACK 2

class Graph {
    
    static const int N = 100;
    static const int infty = (1<<21);
    
    int matrix[N][N];
    vector<int> neighbor[N];
    
    int n;
    
    void inputGraph()
    {
        // n
        // vertex number, degree, v1...vk
        
        cin>>n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = 0;
            }
        }
        
        int nVertex, deg, vi;
        
        for (int i = 0; i < n; i++) {
            cin>>nVertex>>deg;
            nVertex--;
            list<int> vec;
            for (int j = 0; j < deg; j++) {
                cin>>vi;
                vi--;
                matrix[nVertex][vi] = 1;
                //neighbor[nVertex].push_back(vi);
            }
        }
        
        
    }
    
    void printMatrix()
    {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j) {
                    cout<<" ";
                }
                cout<<matrix[i][j];
            }
            cout<<endl;
        }
    }
    
    
    int color[N];
    // d[N]: the time when the vertex is discovered
    // f[N]: the time when the vertex is finalized
    int d[N], f[N];
    int tt;
    
    void dfs_visit(int u)
    {
        color[u] = GREY;
        d[u] = ++tt;
        int v;
        for (v = 0; v < n; v++) {
            if (matrix[u][v] == 0) {
                continue;
            }
            if (color[v] == WHITE) {
                dfs_visit(v);
            }
        }
        color[u] = BLACK;
        f[u] = ++tt;
        
    }
    
    void dfs()
    {
        // color[]: use white, grey and black to indicate the status
        // Stack s: store the visited vertices
        int u;
        for (u = 0; u < n; u++) {
            color[u] = WHITE;
        }
        tt = 0;
        
        for (u = 0; u < n; u++) {
            if (color[u] == WHITE) {
                dfs_visit(u);
            }
        }
        
        for (u = 0; u < n; u++) {
            printf("%d %d %d \n", u+1, d[u], f[u]);
        }
    }
    
    // depth first search implemented via stack
    void dfs2()
    {
        for (int i = 0; i < n; i++) {
            color[i] = WHITE;
            nt[i] = 0;
        }
        
        tt = 0;
        
        for (int u = 0; u < n; u++) {
            if (color[u] == WHITE) {
                dfs_visit2(u);
            }
        }
        
        for (int i = 0; i < n; i++) {
            printf("%d %d %d \n", i+1, d[i], f[i]);
        }
        
    }
    
    int nt[N];
    
    void dfs_visit2(int r)
    {
        for (int i = 0; i < n; i++) {
            nt[i] = 0;
        }
        
        stack<int> s;
        s.push(r);
        
        color[r] = GREY;
        d[r] = ++tt;
        
        while (!s.empty()) {
            int u = s.top();
            int v = next(u);
            if (v != -1) {
                if (color[v] == WHITE) {
                    color[v] = GREY;
                    d[v] = ++tt;
                    s.push(v);
                }
            }
            else {
                s.pop();
                color[u] = BLACK;
                f[u] = ++tt;
            }
        }
        
    }
    
    
    
    // get the node that is next to u
    int next(int u)
    {
        vector<int> vec = neighbor[u];
        if (vec.size() == 0) {
            return -1;
        }
        else {
            int s = (int) vec.size();
            int i = 0;
            while (i < s) {
                if (color[vec[i]] == WHITE) {
                    return vec[i];
                }
            }
        }
        return -1;
    }
    
    
    void bfs(int s)
    {
        queue<int> q;
        q.push(s);
        for (int i = 0; i < n; i++) {
            d[i] = infty;
        }
        d[s] = 0;
        
        int u;
        while (!q.empty()) {
            u = q.front();
            q.pop();
            for (int v = 0; v < n; v++) {
                if (matrix[u][v] == 0) {
                    continue;
                }
                if (d[v] != infty) {
                    continue;
                }
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
        
        for (int i = 0; i < n; i++) {
            cout<<i+1<<" "<<( (d[i] == infty)? (-1):d[i])<<endl;
        }
        
    }

public:
    
    int main()
    {
        inputGraph();
        //printMatrix();
        //dfs();
        bfs(0);
        return 0;
    }
};


#define MAX 100000
#define NIL -1

class ConnectedComponent {
    
    int n;
    vector<int> g[MAX];
    int color[MAX];
    
    void dfs(int r, int c)
    {
        stack<int> s;
        s.push(r);
        
        color[r] = c;
        
        while (!s.empty()) {
            int u = s.top(); s.pop();
            for (int i = 0; i < g[u].size(); i++) {
                int v = g[u][i];
                if (color[v] == NIL) {
                    color[v] = c;
                    s.push(v);
                }
            }
        }
        
    }
    
    void assignColor() {
        int id = 1;
        for (int i = 0; i < n; i++) {
            color[i] = NIL;
        }
        for (int u = 0; u < n; u++) {
            if (color[u] == NIL) {
                dfs(u, id++);
            }
        }
    }
    
public:
    
    int main()
    {
        int s, t, m, q;
        cin>>n>>m;
        
        for (int i = 0; i < m; i++) {
            cin>>s>>t;
            g[s].push_back(t);
            g[t].push_back(s);
        }
        
        assignColor();
        cin>>q;
        
        for (int i = 0; i < q; i++) {
            cin>>s>>t;
            
            if (color[s] == color[t]) {
                cout<<"yes"<<endl;
            }
            else {
                cout<<"no"<<endl;
            }
        }
        
        return 0;
    }
    
};


class MinimumSpanningTree {
    
    int n;
    int matrix[MAX][MAX];
    
    static const int inf = 1<<21;
    
    int prim()
    {
        int d[MAX], p[MAX], color[MAX];
        
        int u, minv;
        
        for (int i = 0; i < n; i++) {
            d[i] = inf;
            p[i] = -1;
            color[i] = WHITE;
        }
        d[0] = 0;
        
        while (1) {
            minv = inf;
            u = -1;
            for (int i = 0; i < n; i++) {
                if (color[i] != BLACK && d[i] < minv) {
                    minv = d[i];
                    u = i;
                }
            }
            
            if (u == -1) {
                break;
            }
            
            color[u] = BLACK;
            
            for (int v = 0; v < n; v++) {
                if (color[v] != BLACK && matrix[u][v] != inf) {
                    if (d[v] > matrix[u][v]) {
                        d[v] = matrix[u][v];
                        p[v] = u;
                        color[v] = GREY;
                    }
                }
            }
        }
        
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (p[i] != -1) {
                sum += matrix[i][p[i]];
            }
        }
        
        return sum;
        
    }
    
};


class SingleShortestPath {
    
    int n, matrix[MAX][MAX];
    
    static const int inf = 1<<21;
    
    void dijkstra()
    {
        int minv;
        int d[MAX], color[MAX];
        
        for (int i = 0; i < n; i++) {
            d[i] = inf;
            color[i] = WHITE;
        }
        
        d[0] = 0;
        color[0] = GREY;
        
        while (1) {
            minv = inf;
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (minv > d[i] && color[i] != BLACK) {
                    u = i;
                    minv = d[i];
                }
            }
            
            if (u == -1) {
                break;
            }
            
            color[u] = BLACK;
            for (int v = 0; v < n; v++) {
                if (color[v] != BLACK && matrix[u][v] != inf) {
                    if (d[v] > d[u] + matrix[u][v]) {
                        d[v] = d[u] + matrix[u][v];
                        color[v] = GREY;
                    }
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            cout<<i<<" "<<( d[i] == inf ? -1 : d[i])<<endl;
        }
    }
    
    
public:
    
    int main()
    {
        cin>>n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = inf;
            }
        }
        
        int k, c, u, v;
        for (int i = 0; i < n; i++) {
            cin>>u>>k;
            for (int j = 0; j < k; j++) {
                cin>>v>>c;
                matrix[u][v] = c;
            }
        }
        
        dijkstra();
        
        return 0;
    }
};
