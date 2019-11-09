//
//  Recurrence.cpp
//  Algorithms
//
//  Created by Kylin on 5/23/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <iostream>

class ExhaustiveSearch
{
    int n, A[50];
    
public:
    
    int solve(int i, int m)
    {
        if( m == 0) return 1;
        if( i >= n) return 0;
        int res = solve(i + 1, m) || solve(i + 1, m - A[i]);
        
        return res;
    }
    
    int main()
    {
        int q;
        int m;
        int i;
        
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &A[i]);
        }
        
        scanf("%d", &q);
        for (i = 0; i < q; i++) {
            scanf("%d", &m);
            if (solve(0, m)) {
                printf("yes\n");
            }
            else
            {
                printf("no\n");
            }
        }
        
        return 0;
    }
};


class KochCurve
{
    
};













