// https://codeforces.com/contest/1907/problem/B
#include<bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define nline "\n"
#define ll long long int
#define pb push_back
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	// For getting input from input.txt file
	freopen("Input.txt", "r", stdin);

	// Printing the Output to output.txt file
	freopen("Output.txt", "w", stdout);

#endif
	FAST;
	int t;
	cin >> t;

	while (t--) {
		string s;
		cin >> s;
		stack<int> s1, s2;
		vector<int> a(s.size(), 0);

		for (int j = 0; j < s.size(); ++j) {
			char i = s[j];
			if (i == 'b') {
				if (!s1.empty()) {
					s1.pop();
				}
			} else if (i == 'B') {
				if (!s2.empty()) {
					s2.pop();
				}
			} else if ('a' <= i && i <= 'z') {
				s1.push(j);
			} else {
				s2.push(j);
			}
		}

		while (!s1.empty()) {
			a[s1.top()] = 1;
			s1.pop();
		}

		while (!s2.empty()) {
			a[s2.top()] = 1;
			s2.pop();
		}

		string ans;

		for (int i = 0; i < s.size(); ++i) {
			if (a[i] == 1) {
				ans += s[i];
			}
		}
		cout << ans << nline;
	}

	return 0;
}