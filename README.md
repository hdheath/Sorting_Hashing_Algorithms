# Sorting & Hashing Algorithm Collection README

## Description 

This repository contains a collection of classic algorithms implemented in Python. These include sorting algorithms like Bubble Sort and Merge Sort, and data structures like a Hash Table with linear and quadratic probing methods, as well as a binary tree with level-order traversal.

## Sorting Algorithms 
1. Bubble Sort: A simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

2. Merge Sort: A divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Data Structures
1. HashTable (Linear Probing): A hash table implementation that uses linear probing to resolve collisions.

2. HashTable (Quadratic Probing): A hash table implementation that uses quadratic probing to resolve collisions, which can help in reducing clustering effects.

3. BinaryTree & Level-Order Traversal: A simple binary tree implementation with the functionality to perform level-order traversal using a queue.

## Usage 
### Sorting Algorithms 
To use the sorting algorithms, import the function and pass a list to it as follows:
```
from sorting import bubbleSort, mergeSort

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(my_list)
print(my_list)  # This will print the sorted list

mergeSort(my_list)
print(my_list)  # This will print the sorted list
```
### HashTable (Linear Probing)
To use the hash table with linear probing:
```
from data_structures import HashTable

hash_table = HashTable()
hash_table.put(1, 'One')
hash_table.put(2, 'Two')
# ... use other methods as needed
```
### HashTable (Quadratic Probing)
Usage is similar to the linear probing hash table, but with the quadratic probing's put method.

### BinaryTree & Level-Order Traversal
To create a binary tree and perform level-order traversal:
```
from data_structures import BinaryTree, levelOrder

root = BinaryTree('Root')
root.insertLeft('Left Child')
root.insertRight('Right Child')

levelOrder(root)  # This will print the nodes in the tree in level order
```
## Requirements 
Python 3.x is required to run these scripts.

## Author 
Harrison Heath 

