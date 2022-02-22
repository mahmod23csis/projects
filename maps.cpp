#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    //create an ordered map called dict that has string as key and string as value
    map<string, string> dict;
    dict.insert(pair<string, string>("apple", "der Apfel"));
    dict.insert(pair<string, string>("banana", "der Banane"));
    dict.insert(pair<string, string>("orange", "die Orange, die Apfelsine"));
    dict.insert(pair<string, string>("strawberry", "die Erdbeere"));

    //change value of a key in dict
    dict["banana"] = "Der Banane";

    //empty the dict
    //dict.clear();
    
    //iterate through elements of map dict
    for(auto pair : dict)
        cout << pair.first << " - " << pair.second << endl;
    return 0;
}