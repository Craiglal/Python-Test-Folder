//Дана послідовність з n цілих чисел. Знайти кількість непарних елементів цієї послідовності.

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
	int N, amount = 0, elem;

	do {
		cout << "Enter N: ";
		cin >> N;
		if (N < 0 || N > 100)
			cout << "Wrong N!" << endl;
	} while (N < 0 || N > 100);

	for (int i = 0; i < N; i++) {
		cout << "Enter element " << i + 1 << " : ";
		cin >> elem;
		if (elem % 2 != 0)
			amount++;
	}

	cout << "The amount of needed elements = " << amount << endl;

	system("pause");
	return 0;
}