#include <iostream>
using namespace std;


//time complexity O(logn)
//space complexxity O(1)
double pow(double x,int n){

    double ans = 1.0;
    long nn = n;
    if(nn<0){
        nn=-1*nn;
    }
    while (nn>0)
    {
        if (nn%2!=0){
            ans=ans * x;
            nn-=1;
        }
        else{
            x=x*x;
            nn/=2;
        }
    }

    return ans;
    
}

int main(){
    double num;
    int power;
    cin>>num;
    cin>>power;
    cout<<pow(num,power);

    return 0;
}