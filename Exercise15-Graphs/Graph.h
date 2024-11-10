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
	void removeV(T val);
	void print();
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
	if (ver != vertices.end())//if the vertex already exist we just add the edge
	{
		(*ver).second->edges.push_back(edge);
	}
	else//else we add the vertex then the edge
	{
		vertices.emplace(val,edge);
		auto ver = vertices.find(vertex);
		(*ver).second->edges.push_back(edge);
	}
}

template<class T>
inline void Graph<T>::addV(T val)//adding the vertex to the vertices map
{
	Vertex<T> * v= new Vertex<T>(val);
	vertices.emplace(val, v);
}

template<class T>
inline void Graph<T>::removeV(T val)
{
	vertices.erase(val);//remove from vertices map
	for(auto vertex : vertices) //remove the edges of the vertex 
	{
		if (vertex.first == val)
		{
			vertex.second->edges.remove(vertex.second);
		}
	}
}

template<class T>
inline void Graph<T>::print()
{
	for (auto vertex : vertices)// print the graph
	{
		cout << vertex.first << ". ";
	}
}
