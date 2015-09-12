#include <iostream>
#include <cmath>

using namespace std;

#define LOWER 2
#define HIGHER 80
#define EXPECTED 0.5
#define EPSILON 1e-8

int ans = 0;

void search(double cur, int last = 1) {
    if (abs(cur - EXPECTED) < EPSILON) {
        ++ans;
        return;
    }
    double lower = cur + 1.0 / HIGHER;
    if (lower - EXPECTED > EPSILON) {
        return;
    }
    // cout << cur << " " << last << endl;
    double higher = cur + 1.0 / last - 1.0 / HIGHER;
    if (EXPECTED - higher > EPSILON) {
        return;
    }
    for (int i = last + 1; i <= HIGHER; ++i) {
        double new_cur = cur + 1.0 / (i * i);
        if (new_cur > EXPECTED) {
            continue;
        }
        search(new_cur, i);
        if (cur == 0) {
            cout << i << endl;
        }
    }
}

int main() {
   search(0);
   cout << ans << endl;
   return 0;
}
