#include <iostream>
using namespace std;
#include <crtdbg.h>

template <class T>
class Queue{
private:
	T *queue;
	int front, rear, capacity;
public:
	Queue(int Capacity = 10){
		capacity = Capacity;
		while (capacity < 1){
			printf("Capacity must be > 0\nRe Input: ");
			cin >> capacity;
		}
		queue = new T[capacity];
		front = rear = 0;
	}
	~Queue(){
		delete[] queue;
	}
	inline bool IsEmpty(){ return front == rear; }
	inline T& Front(){
		if (IsEmpty()) printf("Queue is empty. No front element.\n");
		else return queue[(front + 1) % capacity];
	}
	inline T& Rear(){
		if (IsEmpty()) printf("Queue is empty. No front element.\n");
		else return queue[rear];
	}
	void Push(const T& x){
		if ((rear + 1) % capacity == front){
			T* temp = new T[capacity * 2];

			int start = (front + 1) % capacity;
			int i = 1;
			if (start < 2){
				for (; start < rear + 1; start++){
					temp[i] = queue[start];
					i++;
				}
			}
			else{
				for (; start < capacity; start++){
					temp[i] = queue[start];
					i++;
				}
				for (start = 0; start < rear + 1; start++){
					temp[i] = queue[start];
					i++;
				}
			}
			delete[] queue;
			queue = temp;
			front = 0;
			rear = capacity - 1;
			capacity *= 2;
		}

		rear = (rear + 1) % capacity;
		queue[rear] = x;

	}
	void Pop(){
		if (IsEmpty()) printf("Queue is empty. Cannot delete.\n");
		else{
			front = (front + 1) % capacity;
			queue[front] = queue[front - 1];
		}
	}
	void Print(){
		for (int i = 0; i < capacity; i++){
			cout << queue[i];
			if (i == front) cout << " front";
			if (i == rear) cout << " rear";
			//if (i < rear && i >= front) cout << queue[i] << endl;
			//else printf("'Empty'\n");
			cout << endl;
		}
	}
};

void main(){
	Queue<int> Q;

	while (char in = '0'){
		printf("\n\n\n1. Push\n2. Pop\n3. Print\n4. Exit\nInput: ");
		cin >> in;
		if (in == '1'){
			int x;
			printf("Input to Push: ");
			cin >> x;
			Q.Push(x);
		}
		else if (in == '2'){
			Q.Pop();
		}
		else if (in == '3'){
			Q.Print();
		}
		else if (in == '4'){
			break;
		}
		_CrtDumpMemoryLeaks();
	}
}