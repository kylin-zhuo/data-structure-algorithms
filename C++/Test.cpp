//
//  Test.cpp
//  Algorithms
//
//  Created by Kylin on 5/26/17.
//  Copyright © 2017 linzhuo. All rights reserved.
//

#include <stdio.h>
#include <stack>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

void static test1()
{
    stack<int> S;
    
    S.push(3);
    S.push(4);
    S.push(5);
    
    cout<<S.size();
}

void static test2()
{
    int n;
    vector<int> v;
    
    cin>>n;
    for (int i = 0; i < n; i++) {
        int x;
        cin>>x;
        v.push_back(x);
    }
    
    /* The sort of STL is baded on QuickSort, which is not stable
     * Using stable_sort, which is based on MergeSort can ensure stable sorting.
     * However, MergeSort requires more memory and runs slightly slower.
     */
    stable_sort(v.begin(), v.end());
    //sort(v.begin(), v.end());
    
    
    for (int i = 0; i < n; i++) {
        cout<<v[i]<<" ";
        
    }
    
    cout<<endl;
}


void static printSet(set<int> s)
{
    cout<<s.size()<<":";
    for (set<int>::iterator it = s.begin(); it != s.end(); it++) {
        cout<<" "<<(*it);
    }
    cout<<endl;
}

void static test3()
{
    set<int> s;
    s.insert(8);
    s.insert(1);
    s.insert(7);
    s.insert(4);
    s.insert(8);
    s.insert(4);
    
    printSet(s);
    
    s.erase(7);
    
    printSet(s);

    s.insert(2);
    printSet(s);
}

#include <map>

void static printMap(map<string, int> t)
{
    map<string, int>::iterator it;
    cout<<t.size()<<endl;
    for (it = t.begin(); it != t.end(); it++) {
        pair<string, int> item = *it;
        cout<<item.first<<" -->"<<item.second<<endl;
    }
    
}

void static test4()
{
    map<string, int> t;
    
    t["red"] = 32;
    t["green"] = 233;
    t["yellow"] = 146;
    
    t["blue"] += 111;
    
    printMap(t);
    
    t.insert(make_pair("zebra", 10101));
    t.insert(make_pair("horse", 555));
    
    t.erase("yellow");
    
    printMap(t);
    
}
