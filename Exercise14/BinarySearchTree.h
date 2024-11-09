#pragma once
template<class T> 
class Node 
{
public:
	Node* left;
	Node* right;
	T value;
	Node(T val) : value(val), left(nullptr), right(nullptr) {}
	Node(T val, Node* l, Node* r)
		: value(val), left(l), right(r) {}
};
template<class T>
class Tree
{
public:
	Node<T>* root;
	void add(Node<T> *current ,T val);
	Node<T>* search(Node<T> *root, T value);
	void remove(Node<T>* current, T val);
	Node<T>* findMin(Node<T>* node);
	Node<T>* findMax(Node<T>* node);

};

template<class T>
inline void Tree<T>::add(Node<T> *current  , T val)
{
	if (root == nullptr)//if tree is empty
	{
		root = new Node<T>(val);
		return;
	}
	else//tree isnt empty
	{
		if (current->right == nullptr && current->value < val)//node has only a left son and the current value is less than val
		{
			current->right = new Node<T>(val);
			return;
		}
		else if (current->left == nullptr && current->value > val)//node has only a rightt son and the current value is greater than val
		{
			current->left = new Node<T>(val);
			return;
		}
		else
		{
			if (current->value < val)
			{
				add(current->right, val);
			}
			else
			{
				add(current->left, val);
			}
		}
	}
}

template<class T>
inline Node<T>* Tree<T>::search(Node<T>* current, T val)
{
	if (root == nullptr || (current->right == nullptr && current->left == nullptr))
	{
		return nullptr;
	}
	if (current->right->value == val || current->left->value == val)//return the parent node
	{
		return current;
	}
	else
	{
		if (current->value < val)
		{
			search(current->right, val);
		}
		else
		{
			search(current->left, val);
		}
	}
}

template<class T>
inline void Tree<T>::remove(Node<T>* current, T val)
{
	//if the node is null, return
	if (current == nullptr) 
	{
		return;
	}

	// Recursively find the node to remove
	if (val < current->value) 
	{
		remove(current->left, val);
	}
	else if (val > current->value) 
	{
		remove(current->right, val);
	}
	else // Node found
	{
		//Node has no children (leaf node)
		if (current->left == nullptr && current->right == nullptr) 
		{
			delete current;
			current = nullptr;
		}
		//has one child
		else if (current->left == nullptr) 
		{
			Node<T>* temp = current;
			current = current->right;
			delete temp;
		}
		else if (current->right == nullptr) 
		{
			Node<T>* temp = current;
			current = current->left;
			delete temp;
		}
		// Node has two children
		else 
		{
			Node<T>* temp = findMin(current->right);
			current->value = temp->value;
			remove(current->right, temp->value);
		}
	}
}

template<class T>
inline Node<T>* Tree<T>::findMin(Node<T>* node)
{
	while (node->left != nullptr) //go left till the most left leaf
	{
		node = node->left;
	}
	return node;
}

template<class T>
inline Node<T>* Tree<T>::findMax(Node<T>* node)
{
	while (node->right != nullptr) //go right till the most right leaf
	{
		node = node->right;
	}
	return node;
}
