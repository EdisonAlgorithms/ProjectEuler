#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int sum = 0;
	for (int i = 1; ; ++ i) {
		sum += i;
		int ret = 0;
		for (int j = 1; j <= sqrt(sum); ++ j)
			if (sum % j == 0) {
				++ ret;
				if (j * j != sum)
					++ ret;
			}
		if(ret > 500) {
			cout << sum << endl;
			return 0;
		}
	}
}