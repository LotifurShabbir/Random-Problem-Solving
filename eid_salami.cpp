#include<bits/stdc++.h>
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

	int arr[] = {1, 1, 1, 2, 1};
	int len = sizeof(arr) / sizeof(arr[0]);
	// cout << len << nline;
	int trigger = 0; int total_sum = 0;

	for (int i = 0; i < len; i++) {
		total_sum += arr[i];
	}
	int pans = 0;

	for (int i = 0; i < len - 1; i++) {
		pans += (arr[i] + arr[i + 1]);
		//cout << pans << nline;
		if ((total_sum - pans) == pans) {
			//cout << "YES" << nline;
			trigger = 1;
			break;
		}
		pans = 0;
	}
	if (trigger == 1) {
		cout << "True" << nline;
	}
	else
		cout << "False" << nline;
	return 0;
}