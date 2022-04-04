#include <iostream>

using namespace std;

int main(){

    double sales[10];
    int index;
    double largestSale; sum; average;

    for (index; index < 10; index++){
        sales[index] = 0.0;
    }
    for (index; index < 10; index++){
        cin >> sales[index];
}
    for (index; index < 10; index++){
    cout << sales[index] << " ";
    }
    sum = 0;
    for (index; index < 10; index++){
        sum = sum + sales[index];
    average = sum / 10;
    }
    cout << "The total sale is: " << sum << endl;
    cout << "The average sale is: " << average << endl;

    return 0;


}
