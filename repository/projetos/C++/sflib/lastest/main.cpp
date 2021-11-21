#include <iostream>
using namespace std;

#include "display.h"

int main (){
    
    Display dpy(120, 25);

    dpy.linear_draw = true;

    dpy.to_bff("  test\nanooo!!!", 0, ssize("  test\nanooo!!!"));
    dpy.to_bff("  testanuuu!!!");
    dpy.to_bff("  testaniann!!!");

    cout << dpy.mbff;
    


    


    return 0;
}
