//Author: Mahmod Ahmad
//File: deque.h
/////////////////////
#ifndef _DEQUE_H
#define _DEQUE_H
#include "dequeNode.h"
#include <iostream>
using namespace std;

template <class T>
class Deque
{
	public:
	    Deque()
	    {
		head = rear = NULL;
		int Size = 0;
	    }
	    T show_front();	//function to display front of the deque
	    T show_back();	//function to display back of the deque
	    void push_front(const T& newItem);	//insert an element to front
	    void push_back(const T& newItem);	//insert an element to back
	    void pop_front();	//function to delete front element
	    void pop_back();	//function to delete back element
	    int size();		//function to return size of the deque
	    bool isEmpty();	//function to check if deque is empty
	    Deque(const Deque<T>& other);    //copy constructor
	    ~Deque();	//destructor
	    const Deque<T>& operator=(const Deque<T>&);  //overload assignment operator
	private:
	    dequeNode<T> * head = NULL;	//create a front node of type dequeNode
	    dequeNode<T> * rear = NULL;	//create a back node of type dequeNode
	    int Size = 0;
};

//class memeber implementation functions
template <class T>
bool Deque<T>::isEmpty()
{
    return (head == NULL);
}

template <class T>
void Deque<T>::push_front(const T& newItem)
{
    dequeNode<T> *next;
    dequeNode<T> *previous;
    dequeNode<T> * newNode = dequeNode<T>::new_Node(newItem);
    if (newNode == NULL)
	cout << "Overflow\n";
    else
    {
	if (head == NULL)
	    rear = head = newNode;
	else
	{
	    newNode->next = head;
	    head->previous = newNode;
	    head = newNode;
	}
	Size++;
    }
}

template <class T>
void Deque<T>::push_back(const T& newItem)
{
    dequeNode<T> *next;
    dequeNode<T> *previous;
    dequeNode<T> * newNode = dequeNode<T>::new_Node(newItem);
    if (newNode == NULL)
	cout << "Overflow\n";
    else
    {
	if (rear == NULL)
	    head = rear = newNode;
	else
	{
	    newNode->next = rear;
	    rear->previous = newNode;
	    rear = newNode;
	}
	Size++;
    }
}

template <class T>
void Deque<T>::pop_front()
{
     if (isEmpty())
	 cout << "The deque is already empty!\n";
     else
     {
	 dequeNode<T>* temp = head;
	 head = head->next;
	 
	 if (head == NULL)
	     rear = NULL;
	 else
	     head->previous = NULL;
	 delete temp;
	 
	 Size--;
      }
}

template <class T>
void Deque<T>::pop_back()
{
     if (isEmpty())
	 cout << "The deque is already empty!\n";
     else
     {
	 dequeNode<T>* temp = rear;
	 rear = rear->next;
	 
	 if (rear == NULL)
	     head = NULL;
	 else
	     rear->previous = NULL;
	 delete temp;
	 
	 Size--;
      }
}

template <class T>
T Deque<T>::show_front()
{
     if(isEmpty())
	cout << "The deque is empty!\n";
     return head->data;
}

template <class T>
T Deque<T>::show_back()
{
     if(isEmpty())
	cout << "The deque is empty!\n";
     return rear->data;
}

template <class T>
int Deque<T>::size()
{
    return Size;
}

template <class T>
Deque<T>::Deque(const Deque<T>& other)	//copy constructor
{
    dequeNode<T>* p1; //current
    dequeNode<T>* p2; //next

    if(other.head == 0)
         head = 0;
    else
    {
	 head = new dequeNode<T>;
	 head->previous = other.head->previous;
	 head->data = other.head->data;
	 p1 = head;
	 p2 = other.head->next;
    }
    while(p2)
    {
	 p1->next = new dequeNode<T>;
	 p1 = p1->next;
	 p1->previous = p2->previous;
	 p1->data = p2->data;
	 p2 = p2->next;
    }
    p1->next = 0;
}

template <class T>
Deque<T>::~Deque()	//destructor
{
    cout << "Destructor is called" << endl;
    if(isEmpty())
        cout << "Deque is empty!" << endl;
    else
        delete(head);
        delete(rear);
}

template <class T>
const Deque<T>& Deque<T>::operator=(const Deque<T>& other)  //overload assignment operator
{
    if(this != &other)
        return *this;
    while(!isEmpty())
    {
	remove(1);
    }
    Size = other.Size;

    dequeNode<T>* p1; //current
    dequeNode<T>* p2; //next

    if(other.head == 0)
         head = 0;
    else
    {
	 head = new dequeNode<T>;
	 head->previous = other.head->previous;
	 head->data = other.head->data;
	 p1 = head;
	 p2 = other.head->next;
    }
    while(p2)
    {
	 p1->next = new dequeNode<T>;
	 p1 = p1->next;
	 p1->previous = p2->previous;
	 p1->data = p2->data;
	 p2 = p2->next;
    }
    p1->next = 0;
}

#endif
