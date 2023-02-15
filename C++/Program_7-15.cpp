#include <iostream>
#include <iomanip>
#include <ncurses.h>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
using namespace std;

// concatenates a string to itself by number passed into it.
string multiply_string(string string_input, int int_input)
{
    string returned_string = "";
    for (int i = 0; i < int_input; ++i)
    {
        returned_string += string_input;
    }
    return returned_string;
}

// Draws inchworm and takes in distance variable to determine how far the inchworm has traveled.
int worm_state0(int distance)
{
    system("clear");
    cout << multiply_string(" ", distance) << "        \\/\n";
    cout << multiply_string(" ", distance) << "        00\n";
    cout << multiply_string(" ", distance) << "~000000000\n";

    return 0;
}

int worm_state1(int distance)
{
    system("clear");
    cout << multiply_string(" ", distance) << "        \\/\n";
    cout << multiply_string(" ", distance) << "    0   00\n";
    cout << multiply_string(" ", distance) << "~00000000\n";

    return 0;
}

int worm_state2(int distance)
{
    system("clear");
    cout << multiply_string(" ", distance) << "       \\/\n";
    cout << multiply_string(" ", distance) << "    00 00\n";
    cout << multiply_string(" ", distance) << "~00000000\n";

    return 0;
}

int main()
{
    int second, distance;
    second = 500000;
    distance = 0;

    while (true)
    {
        worm_state0(distance);
        usleep(second);
        distance++;

        worm_state1(distance);
        usleep(second);
        distance++;

        worm_state2(distance);
        usleep(second);

        worm_state1(distance);
        usleep(second);

        worm_state0(distance);
        usleep(second);
    }
    return 0;
}
