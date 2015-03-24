#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n = 50000000;
  vector<int> p(n + 1);
  vector<int> prime;
  for (int i = 2; i < n; ++i)
    if (p[i] == 0) {
      for (int j = 2 * i; j < n; j += i)
        p[j] = 1;
      prime.push_back(i);
    }
  int ans = 0;
  for (int i = 0; i < prime.size(); ++i) {
    if (prime[i] * 4 < n)
      ++ans;
    if (prime[i] * 16 < n)
      ++ans;
    if ((prime[i] - 3) % 4 == 0)
      ++ans;
  }
  cout << ans << endl;
}
