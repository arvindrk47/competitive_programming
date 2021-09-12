#include<iostream>
using namespace std;

int main(){
  int n;
  cin>>n;
  while(n--){
    int x,y,z;
    cin>>x>>y>>z;
    if(z < x && z < y){
      cout<<"Alice"<<endl;
      
    }
    else if(y < x && y < z){
      cout << "Bob" <<endl;
    }
    else{
      cout << "Draw" << endl;
    }
  }
}
