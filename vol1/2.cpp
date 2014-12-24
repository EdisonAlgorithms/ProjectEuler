#include <iostream>

using namespace std;

int main() {
	int a = 1, b = 1, ret = 0;
	while(a < 4000000) {
		int c = a + b;
		if(c % 2 == 0)
			ret += c;
		a = b;
		b = c;
	}
	cout << ret << endl;
	return 0;
}