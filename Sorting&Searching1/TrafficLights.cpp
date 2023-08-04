cin >> x >> n;
    set<int> s;
    s.insert(0);
    s.insert(x);
    multiset<int> ms;
    ms.insert(x);
    while(n--)
    {
        cin >> a;
        auto it = s.lower_bound(a);
        auto it2 = it;
        --it2;
 		//debug2(*it,*it2)
        ms.erase(ms.find(*it - *it2));
        ms.insert(a - *it2);
        ms.insert(*it - a);
 		//joker(ms)
        //auto last = ms.end()[1];
        cout << *--ms.end() << " ";
        s.insert(a);
    }