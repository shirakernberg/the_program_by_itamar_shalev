#pragma once
using namespace std;
#include<list>


template<class T>
class Vertex
{
public:
	T value;
	Vertex<T>* edge;
	list <Vertex<T>*>  edges;
	Vertex(T val) : value(val) , edge(nullptr) {};
};