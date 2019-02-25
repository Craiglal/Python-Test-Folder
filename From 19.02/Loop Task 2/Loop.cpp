#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
	int amount = 0, elem = 1;

	while (elem != 0) {
		cout << "Enter element: ";
		cin >> elem;
		if (elem % 2 == 0)
			amount++;
	}

	cout << "The amount of needed elements = " << amount - 1 << endl;

	system("pause");
	return 0;
}