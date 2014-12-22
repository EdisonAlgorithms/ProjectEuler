#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int n = 15;
	long long a[n][n];
	long long ret = 0;
	for (int i = 0; i < 15; ++ i) {
		for (int j = 0; j <= i; ++ j) {
			cin >> a[i][j];
			if (i > 0) {
				if (j == 0)
					a[i][j] += a[i - 1][j];
				else if (j == i)
					a[i][j] += a[i - 1][j - 1];
				else
					a[i][j] += max(a[i - 1][j], a[i - 1][j - 1]);
			}
			if (i == n - 1)
				ret = max(ret, a[i][j]);
		}
	}
	cout << ret << endl;
	return 0;
}