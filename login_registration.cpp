#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void showMenu()
{
    cout << "*******************\n";
    cout << "1. Register\n";
    cout << "2. Login\n";
    cout << "0. Exit\n";
    cout << "*******************\n";
}

int main() 
{

    int option;
    string newUser, newPass, username, password;

    do
    {
        showMenu();
        cout << "Choose an option >> ";
        cin >> option;

        switch (option)
        {
            case 0:
                cout << "Goodbye!";
                break;   
            case 1:
                cout << "Choose a username >> ";
                cin >> newUser;
                cout << "Choose a password >> ";
                cin >> newPass;
                cout << "You are registered!\n";
                break;
            case 2:
                cout << "Enter your username >> ";
                cin >> username;
                cout << "Enter your password >> ";
                cin >> password;
                if(username == newUser && password == newPass)
                {
                    cout << "Successfuly logged in!\n";
                }
                else
                    cout << "Incorrect username & password!\n";
                break;             
        }
    } while (option != 0);

    return 0;
}