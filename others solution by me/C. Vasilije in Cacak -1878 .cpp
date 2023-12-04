#include<iostream>
#define MAX 1000006
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define nline "\n"
#define ll long long int
#define pb push_back
using namespace std;
// !-------functions------!

int main()
{
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
		ll n, k, x;
		cin >> n >> k >> x;
		ll first_sum = (k * (k + 1)) / 2;
		ll last_sum = (n * (n + 1) / 2) - (n - k) * (n - k + 1) / 2;
		if (first_sum <= x && last_sum >= x)
			cout << "YES" << nline;
		else
			cout << "NO" << nline;
	}
	return 0;
}