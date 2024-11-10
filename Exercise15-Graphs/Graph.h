#pragma once
#include "Vertex.h"
#include<map>
using namespace std;
template<class T> 
class Graph
{
public:
	Graph* graph;
	map< T, Vertex<T>*> vertices;
	Graph();
	void addE(T vertex , T val);
	void addV(T val);
};

template<class T>
inline Graph<T>::Graph()
{
	
}

template<class T>
inline void Graph<T>::addE(T vertex, T val)
{
	Vertex<T>* edge = new Vertex<T>(val);
	auto ver = vertices.find(vertex);
	if (ver != vertices.end())
	{
		(*ver).second->edges.push_back(edge);
	}
	else
	{
		vertices.emplace(val,edge);
		auto ver = vertices.find(vertex);
		(*ver).second->edges.push_back(edge);
	}
}

template<class T>
inline void Graph<T>::addV(T val)
{
	Vertex<T> * v= new Vertex<T>(val);
	vertices.emplace(val, v);
}
