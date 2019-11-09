//
//  BST.cpp
//  Algorithms
//
//  Created by Kylin on 5/26/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>

using namespace std;

class BinarySearchTree {

protected:
    
    struct Node{
        int key;
        Node *parent, *left, *right;
    };
    
    Node* root;
    
    void insert(int k)
    {
        Node *x = root;
        Node *y = NULL;
        Node *z;
        
        z = (Node*) malloc(sizeof(Node));
        
        z->key = k;
        z->left = NULL;
        z->right = NULL;
        
        while (x != NULL) {
            y = x;
            if (z->key < x->key) {
                x = x->left;
            }
            else {
                x = x->right;
            }
        }
        
        z->parent = y;
        if (y == NULL) {
            root = z;
        }
        else {
            if (z->key < y->key) {
                y->left = z;
            }
            else {
                y->right = z;
            }
        }
    }
    
    void inorder(Node *u)
    {
        if (u == NULL) {
            return;
        }
        inorder(u->left);
        printf("%d ", u->key);
        inorder(u->right);
    }
    
    void preorder(Node *u)
    {
        if (u == NULL) {
            return;
        }
        printf("%d ", u->key);
        preorder(u->left);
        preorder(u->right);
    }
    
    Node *find(Node *u, int k)
    {
        while (u != NULL && u->key != k) {
            if (k < u->key) {
                u = u->left;
            }
            else {
                u = u->right;
            }
        }
        
        return u;
    }
    

    Node *getMinimum(Node *u)
    {
        while (u->left != NULL) {
            u = u->left;
        }
        return u;
    }
    
    Node *getSuccessor(Node *u)
    {
        if (u->right != NULL) {
            return getMinimum(u->right);
        }
        
        Node *y = u->parent;
        while (y != NULL && u == y->right) {
            u = y;
            y = y->parent;
        }
        
        return y;
    }
    
    void deleteNode(Node *u)
    {
        Node *y;
        Node *x;
        
        // decide which node to delete -> y
        if (u->left == NULL || u->right == NULL) {
            y = u;
        } else {
            y = getSuccessor(u);
        }
        
        // get the child of y
        if (y->left != NULL) {
            x = y->left;
        } else {
            x = y->right;
        }
        
        if (x != NULL) {
            x->parent = y->parent;
        }
        
        if (y->parent == NULL) {
            root = x;
        }
        else {
            if (y == y->parent->left) {
                y->parent->left = x;
            }
            else {
                y->parent->right = x;
            }
        }
        
        if (y != u) {
            u->key = y->key;
        }
        
        free(y);
        
    }
    

public:
    
    int main()
    {
        int n, i, x;
        string op;
        
        scanf("%d", &n);
        
        for (i = 0; i < n; i++) {
            cin>>op;
            if (op == "insert") {
                scanf("%d", &x);
                insert(x);
            }
            else if (op == "print") {
                inorder(root);
                printf("\n");
                preorder(root);
                printf("\n");
            }
            else if (op == "find") {
                scanf("%d", &x);
                Node *t = find(root, x);
                if (t == NULL) {
                    printf("no\n");
                } else {
                    printf("yes\n");
                }
            }
            else if (op == "delete") {
                scanf("%d", &x);
                deleteNode(find(root, x));
            }
        }
        
        return 0;
    }
    
    
};
