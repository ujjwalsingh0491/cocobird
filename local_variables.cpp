#include<iostream>
using namespace std;
int glo =9;
int glo_l=4;
int sum()
{
    cout<<glo<<endl;
    return 0;
}
int main()
{   
    int a=4,b=5;
    float pi = 3.142;
    char c = 'a';
    bool is_true = true;
    // global and local variable can have same name however local variable will have more precedence
    int glo_l=6;
    cout<<"This is program for variables"<<endl;
    cout<<"Value of a is "<<a<<"\n"<<" and value of b is "<<b;
    cout<<"\n Value of pi is "<<pi<<endl;
    cout<<"\n Value character c is "<<c<<endl;
    cout<<"The value of global variable is "<<glo<<endl;
    cout<<"The value when both global & local variable have same name  "<<glo_l<<endl;
    sum();
    cout<<is_true;
    return 0;
}