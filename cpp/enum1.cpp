#include <iostream>

using namespace std;

enum courses {ALGEBRA, BASIC, PYTHON, CPP, PHILOSOPHY, ANALYSIS, CHEMISTRY, HISTORY};

courses readCourses()
{
    courses registered;
    char ch1, ch2;

    cout << "Enter the first two letters of the course: " << endl;
    cin >> ch1 >> ch2;

    switch (ch1)
    {
    case 'a':
        if (ch2 == 'l'){
            registered = ALGEBRA;
            cout << "ALGEBRA registered" << endl;
        }else{
            registered = ANALYSIS;
            cout << "ANALYSIS registered" << endl;}
        break;
    case 'b':
        registered = BASIC;
        cout << "BASIC registered" << endl;
        break;
    case 'c':
        if (ch2 == 'h'){
            registered = CHEMISTRY;
            cout << "CHEMISTRY registered" << endl;
        }else{
            registered = CPP;
            cout << "CPP registered" << endl;}
        break;
    case 'h':
        registered = HISTORY;
        cout << "HISTORY registered" << endl;
        break;
    case 'p':
        if (ch2 == 'y'){
            registered = PYTHON;
            cout << "PYTHON registered" << endl;
        }else{
            registered = PHILOSOPHY;
            cout << "PHILOSOPHY registered" << endl;}
        break;
    default:
        cout << "Invalid input." << endl;
    }
    return registered;
}

int main()
{

    readCourses();
    return 0;
}
