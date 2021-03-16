#include "PolyHead.h"

int main(){
	Polynomial a;
	Polynomial b("3 + 3x + 2x^2");
	a.set();

	cout << a;
	cout << b;
	
	cout << a + b;
	cout << a * b;
	
	cout << b.Eval(3) << endl;

	Polynomial c;
	c = a;
	if (c == a){
		cout << "Same" << endl;
		return 0;
	}
	else{
		cout << "not Same" << endl;
		return 1;
	}

	_CrtDumpMemoryLeaks();
}