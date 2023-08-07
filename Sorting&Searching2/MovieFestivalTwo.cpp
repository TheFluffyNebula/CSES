#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    multiset<int> friends;
    for(int i = 0; i < k; ++i) friends.insert(0);

    vector<pair<int, int>> times(n);
    for(auto &time : times) cin >> time.first >> time.second;

    sort(times.begin(), times.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;
    });

    int ans = 0;
    for(auto time : times) {
        auto friendIt = friends.upper_bound(time.first);
        if(friendIt != friends.begin()) {
            friends.erase(--friendIt);
            friends.insert(time.second);
            ++ans;
        }
    }

    cout << ans << "\n";

    return 0;
}
