#include <iostream>
#include <vector>

using namespace std;

int main() {
    const int L = 10000000;
    vector<int> counter(L + 1);
    for (int i = 2; i < L / 2; ++i)
        for (int j = i * 2; j < L; j += i)
            counter[j] += 1;
    int ans = 0;
    for (int i = 2; i < L - 1; ++i)
        if (counter[i] == counter[i + 1])
            ans += 1;
    cout << ans << endl;
}
