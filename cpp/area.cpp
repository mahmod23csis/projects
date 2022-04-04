#include <iostream>

using namespace std;

int main()
{
    double length, width, area, perimeter;

    cout << "Program to compute and output the perimeter and "
        <<  "area of a rectangle." << endl;

    cout << "Please enter length of rectangle: " << endl;
    cin >> length;
    cout << "Please enter the width of rectangle: " << endl;
    cin >> width;

    perimeter = 2 * (length + width);
    area = length * width;

    cout << "Length = " << length << endl;
    cout << "Width = " << width << endl;
    cout << "Perimeter = " << perimeter << endl;
    cout << "Area = " << area << endl;

    return 0;

}
