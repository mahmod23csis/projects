#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int num1, num2, result;
    cout << "Enter an enumerator >> ";
    cin >> num1;
    cout << "Enter a denominator >> ";
    cin >> num2;

    try {
        if(num2 == 0)
        {
            throw num2;
        }
        result = num1 / num2;
        cout << num1 << " / " << num2 << " = " << result << endl;
    }
    catch(int exc){
        cout << "Choose a different denominator other than 0" << endl;
    }
    return 0;
}