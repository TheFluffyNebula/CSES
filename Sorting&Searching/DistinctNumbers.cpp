//... ok
#include <iostream>
#include <set>

int main() {
    int n, temp;
    std::set<int> numbers;

    std::cin >> n;
    for(int i = 0; i < n; i++) {
        std::cin >> temp;
        numbers.insert(temp);
    }

    std::cout << numbers.size() << std::endl;

    return 0;
}