#include <iostream>
using namespace std;

template <class T>
class Queue{
private:
	T *queue;
	int front, rear, capacity;
	void expand(){ //배열 2배 확장
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
		//front와 rear의 위치 선정 및 capacity 2배
		front = 0;
		rear = capacity - 1;
		capacity *= 2;
	}
public:
	Queue(int Capacity = 10){ //생성자
		capacity = Capacity;
		while (capacity < 1){
			printf("Capacity must be > 0\nRe Input: ");
			cin >> capacity;
		}
		queue = new T[capacity];
		front = rear = 0;
	}
	~Queue(){ //소멸자
		delete[] queue;
	}
	inline bool IsEmpty(){ return front == rear; } //빈공간 확인
	void RPush(const T& x){ //rear에서 추가
		if ((rear + 1) % capacity == front) expand();
		rear = (rear + 1) % capacity;
		queue[rear] = x;

	}
	void FPush(const T& x){ //front에서 추가
		if ((capacity + front - 1) % capacity == rear) expand();
		queue[front] = x;
		front = (capacity + front - 1) % capacity;
	}
	void FPop(){ //front에서 제거
		if (IsEmpty()) printf("Queue is empty. Cannot delete.\n");
		else{
			front = (front + 1) % capacity;
			queue[front] = queue[front - 1];
		}
	}
	void RPop(){ //rear에서 제거
		if (IsEmpty()) printf("Queue is empty. Cannot delete.\n");
		else{
			queue[rear] = queue[rear + 1];
			rear = (capacity + rear - 1) % capacity;
		}
	}
	void Print(){ //출력
		for (int i = 0; i < capacity; i++){
			if (i == front) printf("F");
			if (i == rear) printf("R");
			if ((rear < front && (i <= rear || i > front)) // 역방향시
				|| (front < i && i <= rear)) // 정방향시
				cout << queue[i];
			else printf("''");
			printf(", ");
		}
	}

};

void main(){
	Queue<int> Q;

	while (char in = '0'){
		printf("\n\n\n1. FPush\n2. FPop\n3. RPush\n4. RPop\n5. Print\n6. Exit\nInput: ");
		cin >> in;
		if (in == '1'){
			int x;
			printf("Input to Push: ");
			cin >> x;
			Q.FPush(x);
		}
		else if (in == '2'){
			Q.FPop();
		}
		else if (in == '3'){
			int x;
			printf("Input to Push: ");
			cin >> x;
			Q.RPush(x);
		}
		else if (in == '4'){
			Q.RPop();
		}
		else if (in == '5'){
			Q.Print();
		}
		else if (in == '6'){
			break;
		}
	}
}