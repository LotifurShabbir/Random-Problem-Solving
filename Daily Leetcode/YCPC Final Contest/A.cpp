#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        string N;
        cin >> N;

        int sum_of_digits = 0;
        for (char digit : N) {
            sum_of_digits += digit - '0';
        }

        if (sum_of_digits % 3 == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}


// if the integer size is too big then store it as a string and then do your operation.



