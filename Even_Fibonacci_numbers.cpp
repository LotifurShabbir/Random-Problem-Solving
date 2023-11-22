// problem link : https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true
#include<bits/stdc++.h>
#define MAX 1000006
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define nline "\n"
#define ll long long int
#define pb push_back
using namespace std;

//function
long long int fibonacci(long long int n) {
    if (n <= 1) {
        return n;
    }

    long long int a = 0, b = 1, sum = 0;
    for (long long int i = 2; i <= n; i++) {
        sum = a + b;
        a = b;
        b = sum;
    }

    return sum;
}

int main() {


    FAST;
    int t;
    cin >> t;
    while (t--) {
        long long int n;
        cin >> n;
        vector<long long int> v;
        for (ll i = 0; ; i++) {
            long long int ans = fibonacci(i);
            if (ans >= n) {
                break;
            }
            v.push_back(ans);
        }
        ll sum = 0;
        for (auto x : v) {
            if (x % 2 == 0) {
                sum += x;
            }
        }
        cout << sum << nline;
    }

    return 0;
}
