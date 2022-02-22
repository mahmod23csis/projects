//Author: Mahmod Ahmad
//File: main.cpp
/////////////////////
#include "deque.h"
#include "dequeNode.h"
#include <iostream>
#include <deque>
using namespace std;

int main() {
    Deque<int> dq;
    int num1, num2;
    
    cout << "Insert 3 number at the front:\n";
    for(int i =0; i < 3; i++)
    {
        cin >> num1;
        dq.push_front(num1);
    }

    cout << "Insert 3 number at the back:\n";
    for(int i =0; i < 3; i++)
    {
        cin >> num2;
        dq.push_back(num2);
    }

    cout << "\nShow size of the deque\n"
     << dq.size();
    
    cout << "\nShow front of the deque\n"
     << dq.show_front();

    cout << "\nShow back of the deque\n"
     << dq.show_back();

    cout << "\nPop front of the deque...\n";
    dq.pop_front();

    cout << "\nShow front of the deque\n"
     << dq.show_front();

    cout << "\nPop back of the deque...\n";
    dq.pop_back();

    cout << "\nShow back of the deque\n"
     << dq.show_back();

    cout << "\nShow size of the deque\n"
     << dq.size() << endl;

    Deque<int> dq2 = dq; //testing overloaded assignment operator
    
    cout << "\nTesting copy constructor\n";
    cout <<"\nshow front of deque 2: "
     << dq2.show_front() << endl;
    
    return 0;
}
