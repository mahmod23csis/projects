#include <iostream>
#include <string>
using namespace std;

class Printer {
    string _name;
    int _availablePaper;

public:
    Printer(string name, int paper) {   //constructor
        _name = name;
        _availablePaper = paper;
    }

    void print(string txtDoc) {
        int requiredPaper = txtDoc.length() / 10; // 40 chars / 10 = 4 required sheets to print the document 

        if(requiredPaper > _availablePaper)
            //throw "No Paper";     //string throw, string or default catch will occur
            throw 101;  //integer throw, integer or default catch will occur

        cout << "Printing..." << txtDoc << endl;
        _availablePaper -= requiredPaper;
    }

};

int main()
{

    Printer myPrinter("HP DeskJet 2020", 10);
    try {
    myPrinter.print("Hello, my name is Mahmod. I am a Computer Science student");
    myPrinter.print("Hello, my name is Mahmod. I love watching TV shows");
    myPrinter.print("Hello, my name is Mahmod. I code for fun");
    }
    catch (const char * txtException) { //handles string type exceptions
        cout << "Exception: " << txtException << endl;
    }
    catch (int exCode) {    //handles integer type exceptions
        cout << "Exception: " << exCode << endl;
    }
    catch (...) {       //handles any type of exceptions
        cout << "Exception occured"
    }
    return 0;
}
