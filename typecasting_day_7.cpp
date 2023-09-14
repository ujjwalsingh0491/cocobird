#include<iostream>
using namespace std;
int main()
{
    int a =45;
    cout<<"The floating value of a is: "<<float(a)<<endl;
    float b=23.29;
    cout<<"The integer value of b is: "<<int(b)<<endl;
    float c = b+float(a);
    
    cout<<"The floating sum of a+b is: "<<c<<endl;
    int d = (int)b+a;
    cout<<"The integer sum of a+b is: "<<d<<endl;

    
    return 0;
}