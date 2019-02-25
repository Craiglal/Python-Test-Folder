#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool triangle(float a, float b, float c) {
	if (a + b > c && a + c > b && b + c > a) {
		return true;
	}
	else {
		return false;
	}
}

float sq(float a, float b, float c, float p) {
	float s;
	s = sqrt(p * ((p - a) * (p - b) * (p - c)));
	return s;
}

void sides(int x1 ,int x2 ,int x3 ,int y1 ,int y2 ,int y3) {
	float a, b, c, p;
	a = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
	b = sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2));
	c = sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2));
	p = a + b + c;
	if (triangle(a, b, c) == true) {
		cout << "S = " << sq(a, b, c, p) << endl;
	}
	else {
		cout << "Wrong triangle!" << endl;
	}
}

int main(int x1, int x2, int x3, int y1, int y2, int y3) {
	cout << "Enter x1: ";
	cin >> x1;
	cout << "Enter y1: ";
	cin >> y1;
	cout << "Enter x2: ";
	cin >> x2;
	cout << "Enter y2: ";
	cin >> y2;
	cout << "Enter x3: ";
	cin >> x3;
	cout << "Enter y3: ";
	cin >> y3;	
	sides(x1, x2, x3, y1, y2, y3);

	system("pause");
	return 0;
}