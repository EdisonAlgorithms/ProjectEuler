#include <iostream>

using namespace std;

int main() {
	for (int i = 1; i <= 333; ++ i)
		for (int j = i; j <= (1000 - i) / 2; ++ j) {
			int k = 1000 - i - j;
			if (i * i + j * j == k * k) {
				cout << i * j * k << endl;
				return 0;
			}
		}
}