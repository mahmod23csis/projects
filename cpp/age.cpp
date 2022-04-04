#include <iostream>

using namespace std;

int main()
{
    int age;

    cout << "Enter your age: ";
    cin >> age;
    cout << endl;

    switch (age >= 18)
    {
    case true:
        cout << "You are eligible to be drafted." << endl;
        cout << "You are eligible to vote." << endl;

    switch (age >= 21)
    {
    case true:
        cout << "You are eligible to drink." << endl;
        break;
    case false:
        cout << "You are not eligible to drink." << endl;
    }
    break;

    case false:
        cout << "You are not eligible to be drafted." << endl;
        cout << "You are not eligible to vote." << endl;
        cout << "You are not eligible to drink." << endl;
    }
    return 0;

}
