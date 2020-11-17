#include <bits/stdc++.h>
using namespace std;

#define MAX 1000

int multiply(int,int[],int);

void fact(int n) {

    int res[MAX];
    int size = 1;
    res[0]=1;

    for(int num=2;num<=n;num++){
        size = multiply(num,res,size);
    }

    for(int i=size-1;i>=0;i--){
        cout<<res[i];
    }
}


int multiply(int n,int res[],int size){
    int carry=0;

    for(int i=0;i<size;i++){
        int val =res[i]*n+carry;

        res[i]=val%10;

        carry = val/10;
        
    }

    while (carry){
        res[size++]=carry%10;
        carry/=10;
     
    }


    return size;
}

int main(){
    int num;
    cin>>num;
    fact(num);


    return 0;

}