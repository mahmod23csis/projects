#include <iostream>
using namespace std;

void showMenu()
{
    cout << "$$$$$$$$$$$$$$$$$$$$$" << endl;
    cout << "1. Check Balace" << endl;
    cout << "2. Deposit" << endl;
    cout << "3. Withdraw" << endl;
    cout << "0. Exit" << endl;
    cout << "$$$$$$$$$$$$$$$$$$$$$" << endl;
}

int main()
{
    int option;
    double balance = 100, deposit, withdraw;

    do
    {
        showMenu();
        cout << "Choose an option >> ";
        cin >> option;

        switch (option)
        {
        case 1:
            cout << "Current balance: " << balance << "$" << endl;
            break;
        case 2:
            cout << "Enter deposit amount: ";
            cin >> deposit;
            balance += deposit;
            cout << "Current balance: " << balance << "$" << endl;
            break;
        case 3:
            cout << "Enter withdraw amount: ";
            cin >> withdraw;
            if (withdraw <= balance) {
                balance -= withdraw;
                cout << "Current balance: " << balance << "$" << endl;
            } else
                cout << "Non-sufficient funds!" << endl;
            break;
        case 0:
            cout << "Thanks for choosing C++ Bank. Goodbye!";
            break;
        default:
            cout << "Incorrect option!" << endl;
            break;
        }
    } while(option != 0);

    return 0;
}