#include <iostream>

using namespace std;

string getOnes(int x) {
	string ret = "";
	switch (x) {
		case 1 : ret = "one";break;
		case 2 : ret = "two";break;
		case 3 : ret = "three";break;
		case 4 : ret = "four";break;
		case 5 : ret = "five";break;
		case 6 : ret = "six";break;
		case 7 : ret = "seven";break;
		case 8 : ret = "eight";break;
		case 9 : ret = "nine";break;
	}
	return ret;
}

string getTens(int x) {
	string ret = "";
	switch (x) {
		case 10 : ret = "ten";break;
		case 11 : ret = "eleven";break;
		case 12 : ret = "twelve";break;
		case 13 : ret = "thirteen";break;
		case 14 : ret = "fourteen";break;
		case 15 : ret = "fifteen";break;
		case 16 : ret = "sixteen";break;
		case 17 : ret = "seventeen";break;
		case 18 : ret = "eighteen";break;
		case 19 : ret = "nineteen";break;
		case 20 : ret = "twenty";break;
		case 30 : ret = "thirty";break;
		case 40 : ret = "forty";break;
		case 50 : ret = "fifty";break;
		case 60 : ret = "sixty";break;
		case 70 : ret = "seventy";break;
		case 80 : ret = "eighty";break;
		case 90 : ret = "ninety";break;
	}
	return ret;
}

string getWord(int x) {
	string ret = "";
	if (x == 1000) {
		ret = "onethousand";
		return ret;
	}
	int h = x / 100, t = (x % 100) / 10, o = x % 10;
	if (h != 0)
		ret = getOnes(h) + "hundred";
	if (x % 100 == 0)
		return ret;
	if (h != 0)
		ret += "and";
	if (t != 0) {
		if (t == 1) {
			ret += getTens(x % 100);
			return ret;
		}
		else
			ret += getTens(t * 10);
	}
	if (o != 0)
		ret += getOnes(o);
	return ret;
}

int main() {
	int n, ret = 0;
	cin >> n;
	for (int i = 1; i <= n; ++ i) {
		cout << i << " " << getWord(i) << " " << getWord(i).length() << endl;
		ret += getWord(i).length();
	}
	cout << ret << endl;
	return 0;
}