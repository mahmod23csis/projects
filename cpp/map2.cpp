//This program creates a map called zodiacSigns with a string as its keys
//and list of strings as its values. To print keys and values associated with
//we use a nested for loop first to print the keys then the values.

#include <iostream>
#include <map>
#include <string>
#include <list>
using namespace std;

int main()
{
    //create a new map called zodiacSigns that has keys(string) and values(list of strings)
    map<string, list<string>> zodiacSigns;

    list<string> aries{"Mar 21 - Apr 20", "Adventurous", "Selfish"};
    list<string> cancer{"Jun 22 - Jul 22", "Emotional", "Moody"};
    list<string> libra{"Sep 24 - Oct 23", "Idealistic", "Gullible"};
    list<string> leo{"Jul 23 - Aug 21", "Generous", "Bossy"};
    list<string> capricorn{"Dec 23 - Jan 20", "Ambitious", "Pessimistic"};
    list<string> aquarius{"Jan 21 - Feb 19", "Inventive", "Unpredictible"};
    list<string> taurus{"Apr 21 - May 21", "Patient", "Jealous"};
    list<string> gemini{"May 22 - Jun 21", "Adaptible", "Cunning"};
    list<string> scorpio{"Oct 24 - Nov 22", "Determined", "Secretive"};
    list<string> virgo{"Aug 22 - Sep 23", "Modest", "Fussy"};
    list<string> sagittarius{"Nov 23 - Dec 22", "Optimistic", "Blindly Optimistic"};
    list<string> pisces{"Feb 20 - Mar 20", "Imaginative", "Escapist"};

    //assigning a string key to a list of string
    zodiacSigns.insert(pair<string, list<string>>("Aries", aries));
    zodiacSigns.insert(pair<string, list<string>>("Cancer", cancer));
    zodiacSigns.insert(pair<string, list<string>>("Libra", libra));
    zodiacSigns.insert(pair<string, list<string>>("Leo", leo));
    zodiacSigns.insert(pair<string, list<string>>("Capricorn", capricorn));
    zodiacSigns.insert(pair<string, list<string>>("Aquarius", aquarius));
    zodiacSigns.insert(pair<string, list<string>>("Taurus", taurus));
    zodiacSigns.insert(pair<string, list<string>>("Gemini", gemini));
    zodiacSigns.insert(pair<string, list<string>>("Scorpio", scorpio));
    zodiacSigns.insert(pair<string, list<string>>("Virgo", virgo));
    zodiacSigns.insert(pair<string, list<string>>("Sagittarius", sagittarius));
    zodiacSigns.insert(pair<string, list<string>>("Pisces", pisces));

    //iterate through keys of zodiacSign
    for (auto pair : zodiacSigns) {
        cout << pair.first << " - ";

        //iterate through each values of each key in zodiacSigns
        for (auto personality : pair.second)
            cout << personality << ", ";
        cout << endl;
    }

    return 0;
}
