//This wearher like program increases the degrees for every city
//by 1 for every 9 seconds. A dummy API function is created to 
//change the temperature, a map to hold cities and its temperature,
//and a thread to keep refreshing the app.

#include <iostream>
#include <map>
#include <thread>
#include <string>
using namespace std;

//API dummy to increase the temperature by one degrees every 9 sec
void refreshWeather(map<string, int> weatherMap)
{   
    while(true) {
    //iterate through every item of the map by reference
    for(auto& item : weatherMap) {
        item.second++;
        cout << item.first << "  " << item.second << endl;
    }
    //this function should happen every 9 seconds
    this_thread::sleep_for(9000ms);
    }
}

int main()
{
    //create a map with keys(string) and values(integer)
    map<string, int> weatherMap = {
        {"Fargo, ND", 1}, 
        {"Los Angeles, CA", 75}, 
        {"Las Vegas, NV", 78}, 
        {"Denver, CO", 40}, 
        {"Chicago, IL", 32}, 
        {"New York, NY", 40}
    };

    //create a thread and pass API dummy and the map
    thread bgApp(refreshWeather, weatherMap);

    system("pause>nul");
}
