#include <iostream>

using namespace std;

int main() {
	int v[2000001] = {0};
	long long sum = 0;
	for (int i = 2; i <= 2000000; ++ i)
		if (v[i] == 0) {
			sum += i;
			for(int j = 2; j <= 2000000 / i; ++ j)
				v[i * j] = 1;
		}
	cout << sum << endl;
	return 0;
}