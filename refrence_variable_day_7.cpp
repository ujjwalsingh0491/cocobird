#include<iostream>
using namespace std;
int main()
{   
    //float,doubles and long-doubles literals
    //float d = 12.2;   // by default it is double and to make it specifically float we have to add f
    //long double e = 13.3; // by default it is also double and to make it long double we have to add l
    //cout<<"The size of 12.2f is: "<<sizeof(12.2)<<endl;
    //cout<<"The size of 12.2f is: "<<sizeof(12.2f)<<endl;
    //cout<<"The size of 12.2F is: "<<sizeof(12.2F)<<endl;
    //cout<<"The size of 13.2l is: "<<sizeof(13.3l)<<endl;
    //cout<<"The size of 13.3L is: "<<sizeof(12.2L)<<endl;

    //refrence variables
    // when multiple variables are using the same value then they are known as refrence variables
    // when we are using a variable as a refrence to access the value of another variable then it is refrence variable 
    float x =10;
    float &y=x;

    // to make y a refrence variable we use & sign before it, we have still the original variable x
    // we are just multiple versions of it
    cout<<x<<endl<<y<<endl;



    return 0;
}
