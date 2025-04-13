#include <fstream>
#include <iostream>
#include <regex>
using namespace std;

// Different OSs use different CLI commands to run Python
#ifdef _WIN32
// TODO: If your Windows machine runs Python in CLI with "python" instead of "py", update this line.
const string python = "py";
#else
// TODO: If your Mac/Linux machine runs Python in CLI with "python3" instead of "python", update this line.
const string python = "python3";
#endif

/*
 * Prompts the user for a filename.
 * Allows the user to enter nothing to use the default pic (autumn.jpg).
 * If the file has extension jpg, jpeg, jpe, or png
 * and it exists in the project folder, return it.
 * Otherwise, return the default pic filename.
 * Hint: Use ../ before the filename when trying to open it.
 */
string get_filename();

/*
 * Prints the main menu of options:
 * (a) flip, (b) mirror, (c) invert, or (d) exit
 */
void print_menu();

/*
 * Prompts the user for one of the options from the menu.
 * Validates input: makes sure the user enters exactly one character
 * and that it is one of the four valid options.
 * If it isn't valid, keep prompting for input until a valid option
 * is entered.
 */

char get_manip_choice();

int main() {
    cout << "Welcome to the image manipulator!" << endl;
    string filename = get_filename();
    cout << "Using file " << filename << "." << endl;
    print_menu();
    char choice = get_manip_choice();
    cout << "Processing. Go to Python program when it opens. May take a few seconds." << endl;
    string command;
    switch (choice) {
        // Use command-line arguments to pass the filename and manip to the Python file
        case 'a': command = python + " ../render.py " + filename + " flip";
        break;
        case 'b': command = python + " ../render.py " + filename + " mirror";
        break;
        case 'c': command = python + " ../render.py " + filename + " invert";
        break;
    }
    system(command.c_str());
    return 0;
}
// asks for user file name, uses autumn.jpg as default
    string get_filename() {
        const regex pattern("[^\\s]+(.*?)\\.(jpg|jpeg|png|JPG|JPEG|PNG|)$");
        string filename;

        cout << "Enter the file name of the image you want to manipulate: ";
        getline(cin, filename);

        if (filename.empty()) {
            return "autumn.jpg";
        }

        if (regex_match(filename, pattern)){
                return filename;
            }
         else {
            cout << "Invalid image, using default image." << endl;
            return "autumn.jpg";
        }

    }

// show menu
void print_menu() {
    cout << "Option Menu: \n(a) flip\n(b) mirror\n(c) invert\n(d) exit!" << endl;
}

// takes in user choice, validates
char get_manip_choice() {
    string s;
    cout << "Please enter an option (a,b,c, or d): ";
    getline(cin, s);
    while ((s.length() != 1) || (s != "a" && s != "b" && s != "c" && s != "d")){
        cout << "invalid, please enter a single character: ";
        getline(cin,s);
    }
    return s[0];
}
