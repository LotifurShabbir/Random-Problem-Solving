// problem Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
#include <bits/stdc++.h>
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

long long int suming(long long int x, long long int n) {
    n -= 1; // karon below n. tai n er man ek komai dissi
    long long int p = n / x;
    return x * (p * (p + 1)) / 2;
}

int main() {
    FAST;
    int t;
    cin >> t;

    while(t--) {
        long long int n;
        cin >> n;
        long long int three = suming(3, n);
        long long int five = suming(5, n);
        long long int fifteen = suming(15, n);

        long long int result = three + five - fifteen;
        cout << result << endl;
    }

    return 0;
}