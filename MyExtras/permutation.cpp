#include <iostream>
#include <vector>
using namespace std;
int main() {
	long long int t;
	cin>>t;
	while(t--) {
		long long int n;
		cin>>n;
		if(n%2==0) {
			for(long long int i=1;i<=n/2;i++) {
				cout<<2*i<<" "<<2*i-1<<" ";
			}
		}
		else {
			long long int i;
			for( i=1;i<=n/2-1;i++) {
				cout<<2*i<<" "<<2*i-1<<" ";
			}	
			cout<<2*i+1<<" "<<2*i<<" "<<2*i-1;
		}
	}
	return 0;
}
