#include <iostream>

using namespace std;

int main() {
	int n, ret = 0;
	cin >> n;
	for(int i = 0; i < n; ++ i) 
		if(i % 3 == 0 || i % 5 == 0)
			ret += i;
	cout << ret << endl;
	return 0;
}