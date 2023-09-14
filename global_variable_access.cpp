#include<iostream>
using namespace std;
int c = 20;
int main()
{
    int a,b,c;
    cout<<"Enter the value of a: ";
    cin>>a;
    cout<<endl;
    cout<<"Enter the value of b: ";
    cin>>b;
    cout<<endl;
    c = a+b;
    cout<<"The value of a+b: "<<c<<endl;
    cout<<"The global value of c is: "<<::c<<endl;
    

}