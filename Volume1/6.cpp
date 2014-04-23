#include <iostream>

using namespace std;

int main() {
	long long ret = 0, n = 10;
	for(int i = 1; i < n; ++ i)
		for(int j = i + 1; j <= n; ++ j)
			ret += 2 * i * j;
	cout << ret << endl;
	return 0;
}