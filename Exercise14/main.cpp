#include <iostream>
#include "BinarySearchTree.h"

using namespace std;

// Assuming your BST functions are implemented in a class called 'BST' with 'Node' struct.

int main() {
    Tree<int>* tree =new Tree<int>();

    // Test 1: Insertion
    cout << "Inserting values: 50, 30, 20, 40, 70, 60, 80" << endl;
    tree->add(tree->root ,50);
    tree->add(tree->root ,30);
    tree->add(tree->root ,20);
    tree->add(tree->root ,40);
    tree->add(tree->root, 70);
    tree->add(tree->root ,60);
    tree->add(tree->root ,80);


    // Test 3: Search
    cout << "Searching for 40: " << ((tree->search(tree->root ,40) != NULL) ? "Found" : "Not Found") << endl;
    cout << "Searching for 90: " << ((tree->search(tree->root ,90) != NULL) ? "Found" : "Not Found") << endl;

    // Test 4: Find Minimum and Maximum
    cout << "Minimum value in the tree: " << tree->findMin(tree->root)->value << endl;
    cout << "Maximum value in the tree: " << tree->findMax(tree->root)->value << endl;

    // Test 5: Deletion
    cout << "Deleting 20 (leaf node), 30 (node with one child), and 50 (node with two children)" << endl;
    tree->remove(tree->root , 20);
    tree->remove(tree->root ,30);
    tree->remove(tree->root ,50);


    return 0;
}
