#include<iostream>
// press command and hover the mouse over iostream and this header file will open
// there are two types of header files in c++
//1. System header files - these are the header files that comes with the compiler
//2. User defined header files - It is written by the programmer
using namespace std;
int main()
{
    int a,b;
    cout<<"Enter the first value "; 
    // << is an insertion operator used with cout
    cin>>a;
    // >> is an extraction operator used with cin
    cout<<"Enter the second value ";
    cin>>b;
    cout<<"The sum is "<<a+b;
    return 0;
}