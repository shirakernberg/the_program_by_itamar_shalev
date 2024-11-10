#include<iostream>
#include "Graph.h"
using namespace std;
int main()
{
	Graph<int> g;
	cout << "Adding 1,2,3 vertices\n";
	g.addV(1);
	g.addV(2);
	g.addV(3);
	cout << "Adding edge between 1,2,3 vertices\n";
	g.addE(1, 2);
	g.addE(2, 3);
	cout << "Printing graph\n";
	g.print();
	cout << "Removing 3\n";
	g.removeV(3);
	g.print();
	return 0;
}