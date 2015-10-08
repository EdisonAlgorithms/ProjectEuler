#include <iostream>

using namespace std;

int main() {
	string s;
	cin >> s;
	cout << s << endl;
	int ret = (s[0] - '0') * (s[1] - '0') * (s[2] - '0') * (s[3] - '0') * (s[4] - '0');
	for (int i = 5; i < s.length(); ++ i) {
		int temp = s[i] - '0';
		for(int j = i - 4; j < i; ++ j)
			temp *= s[j] - '0';
		if(ret < temp)
			ret = temp;
	}
	cout << ret << endl;
	return 0;

}