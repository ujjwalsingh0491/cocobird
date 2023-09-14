#include<iostream>
using namespace std;
int main()
{
    int a,b;
    cout<<"Following are the arithmentic operators in C++"<<endl;
    // Arithmetic operators
    
    cout<<"The first number is ";
    cin>>a;
    cout<<"The second number is ";
    cin>>b;
    cout<<"The result of a+b is: "<<a+b<<endl;
    cout<<"The result of a-b is: "<<a-b<<endl;
    cout<<"The result of a*b is: "<<a*b<<endl;
    cout<<"The result of a/b is: "<<a/b<<endl;
    // above line will return the quotient
    cout<<"The result of a%b is: "<<a%b<<endl;
    // above line will return the remainder
    cout<<"The output of ++a is: "<<++a<<endl;
    cout<<"The output of ++b is: "<<++b<<endl;
    cout<<"The output of a++ is: "<<a++<<endl;
    cout<<"The output of b++ is: "<<b++<<endl;
    cout<<"The output of a-- is: "<<a--<<endl;
    cout<<"The output of --a is: "<<--a<<endl;

    //Comparison operators
    cout<<"The value of a==b: "<<(a==b)<<endl;
    cout<<"The value of a>=b: "<<(a>=b)<<endl;
    cout<<"The value of a<=b: "<<(a<=b)<<endl;
    cout<<"The value of a!=b: "<<(a!=b)<<endl;
    cout<<"The value of a>b: "<<(a>b)<<endl;
    cout<<"The value of a<b: "<<(a<b)<<endl;

    //Logical Operators
    cout<<"The value of a<=b with logical && operator: "<<((a<b) && (a==b))<<endl;
    cout<<"The value of a>=b logical && operator : "<<((a>b) && (a==b))<<endl;
    cout<<"The value of !(a==b): "<<!(a==b)<<endl;
    cout<<"The value of a<=b logical || operator : "<<((a<b) || (a==b))<<endl;
    cout<<"The value of a>=b logical || operator : "<<((a>b) || (a==b))<<endl;
    //cout<<"The value of !(a==b): "<<!(a==b);


    return 0;
}