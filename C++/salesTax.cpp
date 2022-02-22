#include <iostream>

using namespace std;

int main() {
    stateSalesTax = salePrice * 0.04;
    citySalesTax = salePrice * 0.015;

    //If item is luxury

    if (item = luxuryItem) {
        luxuryTax = salePrice * 0.1;
} else {
        luxuryTax = 0;
}

    salesTax = stateSalesTax + citySalesTax + luxuryTax;

    amountDue = salesPrice + salesTax;


}
