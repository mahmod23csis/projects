//Author: Mahmod Ahmad
//File: dequeNode.h
/////////////////////
#ifndef _DEQUENODE_H
#define _DEQUENODE_H
#include "deque.h"
#include <iostream>

template <class T>
struct dequeNode
{
	T data;
	dequeNode *next;
	dequeNode *previous;
	static dequeNode *new_Node(T data)
	{
	    dequeNode * newNode = (dequeNode*)malloc(sizeof(dequeNode));
	    newNode->data = data;
	    newNode->previous = newNode->next = NULL;
	    return newNode;
	} 
};

#endif
