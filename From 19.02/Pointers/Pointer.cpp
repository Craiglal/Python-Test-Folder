#include <iostream>
#include <string>
using namespace std;

int main() {
	int arr[12], amount = 0;

	for (int i = 0; i < 12; i++) {
		cout << "Enter element " << i + 1 << " : ";
		cin >> arr[i];
		if (arr[i] % 2 == 0)
			amount++;
	}

	cout << "The amount of needed elemens = " << amount << endl;

	system("pause");
	return 0;
}