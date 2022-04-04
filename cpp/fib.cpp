#include <iostream>
using namespace std;

int main()
{
    int f0 = 0, f1 = 1, f2, fn;

    cout << "Enter how many fibonacci numbers to display: ";
    cin >> fn;

    cout << f0 << " " << f1 << " ";

    for(int i = 2; i <= fn; i++)
    {
        f2 = f1 + f0;
        cout << f2 << " ";
        f0 = f1;
        f1 = f2;
    }
}
