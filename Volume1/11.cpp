#include <iostream>

using namespace std;

int main() {
	int g[20][20];
	for (int i = 0; i < 20; ++ i)
		for (int j = 0; j < 20; ++ j)
			cin >> g[i][j];
	int ret = 0;
	for (int i = 0; i < 20; ++ i)
		for (int j = 0; j < 20; ++ j) {
			if (i > 2) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i - k][j];
				if (ret < temp)
					ret = temp;
			}
			if (i < 17) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i + k][j];
				if (ret < temp)
					ret = temp;
			}
			if (j > 2) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i][j - k];
				if (ret < temp)
					ret = temp;
			}
			if (j < 17) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i][j + k];
				if (ret < temp)
					ret = temp;
			}
			if (i > 2 && j > 2) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i - k][j - k];
				if (ret < temp)
					ret = temp;
			}
			if (i > 2 && j < 17) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i - k][j - k];
				if (ret < temp)
					ret = temp;
			}
			if (i < 17 && j > 2) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i + k][j - k];
				if (ret < temp)
					ret = temp;
			}
			if (i < 17 && j < 17) {
				int temp = g[i][j];
				for (int k = 1; k < 4; ++ k)
					temp *= g[i + k][j + k];
				if (ret < temp)
					ret = temp;
			}
		}
	cout << ret << endl;
	return 0;
}