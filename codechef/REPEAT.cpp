#include <iostream>
using namespace std;

int main() {
	// your code goes here
  int n;
  cin>>n;

  while(n--){
    int a,b,c;
    cin>>a>>b>>c;

    c=c-(a*a);
    cout <<c / (b-1) << endl;
  }
	return 0;
}
