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
		ll n;
		cin >> n;

		long long ans = -1;
		for (ll i = 2; i * i <= n; i++) {
			while (n % i == 0) {
				ans = max(ans, i);
				n /= i;
			}
		}
		if (n > 1)
			ans = n;
		cout << ans << nline;
	}

	return 0;
}
// problem link: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true