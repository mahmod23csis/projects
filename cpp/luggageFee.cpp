#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double bagDimension;
    double bagWeight;
    double addCharges = 0.0;

    cout << fixed << showpoint << setprecision(2);
    cout << "Enter suitcase dimensions (length + width + depth) in inches: ";
    cin >> bagDimension;
    cout << endl;

    cout << "Enter suitcase weight: ";
    cin >> bagWeight;
    cout << endl;

    if (bagDimension > 108 || bagWeight > 50)
        addCharges = 50.0;
    cout << "Additional suitcase charges: $" << addCharges << endl;

    return 0;
}
