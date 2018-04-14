//
//  Tree.cpp
//  Algorithms
//
//  Created by Kylin on 5/24/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>

using namespace std;

#define MAX 200000
#define NIL -1

class Tree{
    
public:
    
    struct Node
    {
        int parent, left, right;
    };
    
    Node node[MAX];
    
    // n: the number of Nodes in the tree
    int n, depth[MAX];
    
    int root = 0;
    
    void inputBinaryTree()
    {
        
        int i, v, l ,r;
        
        cin>>n;
        for (i = 0; i < n; i++) {
            node[i].parent = NIL;
        }
        
        for (i = 0; i < n; i++) {
            cin>>v>>l>>r;
            node[v].left = l;
            node[v].right = r;
            if (l != NIL) {
                node[l].parent = v;
            }
            if (r != NIL) {
                node[r].parent = v;
            }
        }
    }
    
    void inputNormalTree()
    {
        int i, j;
        
        // id: the number of a node
        // k: the degree of a node
        // ci: the child node
        // l: the temporary left node
        int id, k, ci, l = 0;
        
        cin>>n;
        for (i = 0; i < n; i++) {
            node[i].parent = node[i].left = node[i].right = NIL;
            
        }
        
        for (i = 0; i < n; i ++) {
            cin>>id>>k;
            for (j = 0; j < k; j++) {
                cin>>ci;
                if(j == 0) node[id].left = ci;
                else node[l].right = ci;
                
                l = ci;
                node[ci].parent = id;
            }
        }
    }
};


class RootedTree : Tree
{
    

    // recursively computes the depth
    // u: the node
    // p: the depth to set to the node
    void rec(int u, int p)
    {
        depth[u] = p;
        if (node[u].right != NIL) {
            rec(node[u].right, p);
        }
        if (node[u].left != NIL) {
            rec(node[u].left, p+1);
        }
    }
    
    
    void print(int u)
    {
        int i, c;
        
        cout<<"node "<<u<<": ";
        cout<<"parent = "<<node[u].parent<<", ";
        cout<<"depth = "<<depth[u]<<", ";
        
        if (node[u].parent == NIL) {
            cout<<"root, ";
        } else if (node[u].left == NIL){
            cout<<"leaf, ";
        } else
            cout<<"internal node, ";

        cout<<"[";
        
        for (i = 0, c = node[u].left; c != NIL; i++, c = node[c].right) {
            if (i) {
                cout<<", ";
            }
            cout<<c;
        }
        
        cout<<"]"<<endl;
        
    }
    
public:
    
    int main()
    {
        
        int i;
        
        inputNormalTree();
        
        for (i = 0; i < n; i++) {
            if(node[i].parent == NIL) root = i;
        }
        
        rec(root, 0);
        for (i = 0; i < n; i++) {
            print(i);
        }
        
        return 0;
    }
    
};



class BinaryTree : Tree
{
    int height[MAX];
    
    
    // set the depths from Node u on
    void setDepth(int u, int d)
    {
        if (u == NIL) {
            return;
        }
        depth[u] = d;
        setDepth(node[u].left, d + 1);
        setDepth(node[u].right, d + 1);
    }
    
    // set the height of a certain node and return this height
    int setHeight(int u)
    {
        int hLeft = 0, hRight = 0;
        if (node[u].left != NIL) {
            hLeft = setHeight(node[u].left) + 1;
        }
        if (node[u].right != NIL) {
            hRight = setHeight(node[u].right) + 1;
        }
        
        height[u] = (hLeft > hRight ? hLeft : hRight);
        return height[u];
    }
    
    // returns the sibling of a certain node
    int getSibling(int u)
    {
        int t;
        
        if (node[u].parent == NIL) {
            return NIL;
        }
        
        t = node[node[u].parent].left;
        if ( t != u && t != NIL) {
            return t;
        }
        
        t = node[node[u].parent].right;
        if (t != u && t != NIL) {
            return t;
        }
        
        return NIL;
    }
    
    int getDegree(int u)
    {
        int deg = 0;
        if (node[u].left != NIL) {
            deg++;
        }
        if (node[u].right != NIL) {
            deg++;
        }
        return deg;
    }
    
    
    // display the node
    void print(int u)
    {
        cout<<"node "<<u<<": ";
        cout<<"parent = "<<node[u].parent<<", ";
        cout<<"sibling = "<<getSibling(u)<<", ";
        cout<<"degree = "<<getDegree(u)<<", ";
        cout<<"depth = "<<depth[u]<<", ";
        cout<<"height = "<<height[u]<<", ";
        
        if (node[u].parent == NIL) {
            cout<<"root";
        }
        else if (node[u].left == NIL && node[u].right == NIL) {
            cout<<"leaf";
        }
        else {
            cout<<"internal node";
        }
        
        cout<<endl;
        
    }
    
public:
    
    int main()
    {
        inputBinaryTree();
    
        for (int i = 0; i < n; i++) {
            if (node[i].parent == NIL) {
                root = i;
            }
        }
        
        setDepth(root, 0);
        setHeight(root);
        
        for (int i = 0; i < n; i++) {
            print(i);
        }
        
        return 0;
    }
};


class TreeWalk : Tree
{
protected:
    void preParse(int u)
    {
        if (u == NIL) {
            return;
        }
        cout<<u<<" ";
        preParse(node[u].left);
        preParse(node[u].right);
    }
    
    void inParse(int u)
    {
        if (u == NIL) {
            return;
        }
        inParse(node[u].left);
        cout<<u<<" ";
        inParse(node[u].right);
    }
    
    void postParse(int u)
    {
        
        if (u == NIL) {
            return;
        }
        postParse(node[u].left);
        postParse(node[u].right);
        cout<<u<<" ";
        
    }
    
public:
    
    int main()
    {
        
        inputBinaryTree();
    
        for (int i = 0; i < n; i++) {
            if (node[i].parent == NIL) {
                root = i;
            }
        }
        
        cout<<"Preorder"<<endl;
        preParse(root);
        cout<<endl;
        cout<<"Inorder"<<endl;
        inParse(root);
        cout<<endl;
        cout<<"Postorder"<<endl;
        postParse(root);
        cout<<endl;
        
        return 0;
    }
};


#include <vector>
#include <algorithm>

class ReconstructionTree : Tree {
    
    // Given pre-order and in-order, reconstruct the tree, output the post-order

protected:
    vector<int> pre, in, post;
    
    int pos = 0;
    
    void reconstruct(int l, int r)
    {
        if(l >= r) return;
        int root = pre[pos];
        pos++;
        int m = (int) distance(in.begin(), find(in.begin(), in.end(), root));
        reconstruct(l, m);
        reconstruct(m + 1, r);
        post.push_back(root);
    }
    
    void solve()
    {
        pos = 0;
        reconstruct(0, (int)pre.size());
        for (int i = 0; i < n; i++) {
            if(i) cout<<" ";
            cout<<post[i];
        }
        cout<<endl;
    }
    
public:

    int main()
    {
        int k;
        cin>>n;
        for (int i = 0; i < n; i++) {
            cin>>k;
            pre.push_back(k);
        }
        for (int i = 0; i < n; i++) {
            cin>>k;
            in.push_back(k);
        }
        
        solve();
        
        return 0;
    }
    
};









