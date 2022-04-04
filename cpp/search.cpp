#include <iostream>

using namespace std;

const int array_size = 4;

struct listType
{
    int listElem[array_size];
    int listLength;
};

int seqSearch(const listType list[], int searchItem);

int main()
{
    listType intList[array_size];
    int key;

    cout << "Enter 4 numbers >> ";
    for (int i = 0; i < array_size; i++)
        cin >> intList[].listElem;

    cout << "Enter a number to search for >> ";
    cin >> key;

    seqSearch(intList, key);
    return 0;
}

int seqSearch(const listType list[], int searchItem)
{
    int loc;

    bool found = false;

    for (loc = 0; loc < list.listLength; loc++)
        if (list.listElem[loc] == searchItem)
    {
        found = true;
        break;
    }
    if (found)
        return loc;
    else
        return -1;
}
