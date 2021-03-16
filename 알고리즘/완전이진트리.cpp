#include <iostream>
using namespace std;

class node { // Ʈ�� ���
friend class tree;
private:
	int data;
	int num;
	node* left;
	node* right;
	node* par;
	node() {
		data = NULL;
		num = NULL;
		left = NULL;
		right = NULL;
		par = NULL;
	}
	~node() {
		data = NULL;
		num = NULL;
		left = NULL;
		right = NULL;
		par = NULL;
	}
};

class snode { // ���� ���
	friend class stack;
private:
	int data;
	snode* prev;
	snode* next;
	snode() {
		data = NULL;
		next = NULL;
		prev = NULL;
	}
	~snode() {
		data = NULL;
		next = NULL;
		prev = NULL;
	}
};

class stack { // ����
private:
	snode* first;
	snode* top;
public:
	stack() {
		first = NULL;
		top = NULL;
	}
	void push(int data) {
		if (!first) {
			top = new snode;
			top->data = data;
			first = top;
		}
		else {
			snode* newnode = new snode;
			newnode->data = data;
			top->next = newnode;
			newnode->prev = top;
			top = newnode;
		}
	}
	int pop() {
		if (!first) return -1;
		else {
			int result = top->data;
			if (first == top) {
				delete top;
				first = NULL;
				top = NULL;
			}
			else {
				top = top->prev;
				delete top->next;
			}
			return result;
		}
	}
};

class tree {
private:
	node* anc;
	int count;
public:
	tree() {
		anc = NULL;
		count = NULL;
	}
	void push(int data) { // ����
		count++;
		if (!anc) { // ù ���
			anc = new node;
			anc->data = data;
			anc->num = count;
		}
		else {
			node* newnode = new node;
			newnode->num = count;
			newnode->data = data;

			node* pos = anc;
			pos = pushsearch(pos); // push�� ��� Ž��
			if (!pos->left) pos->left = newnode;
			else if (!pos->right) pos->right = newnode;
			newnode->par = pos;
		}
	}
	node* pushsearch(node* pos) { // push�� ��� Ž��
		if (pos->left && pos->right) { // left�� right�� ���� ���� ���
			node* left = pushsearch(pos->left); // left�� ���� ����Լ�
			node* right = pushsearch(pos->right); // right�� ���� ����Լ�
			// ����Լ��� ���� �� �� ��ȯ
			if (left->num > right->num) return right;
			else return left;
		}
		else return pos; // NULL�� ���� �ִٸ� return
	}
	node* search(int num) { // num��° ��� Ž��
		node* pos = anc;
		int find = num;
		stack dir;
		while (find != 1) { // ������ �̿��� �̵����� ����
			// ������ => ������ ��θ� ���ÿ� ����
			int next = find / 2;
			dir.push(find - next * 2);
			find = next;
		}
		while (true) { // ���� ������� �̵�
			int pop = dir.pop();
			if (pop == 1) pos = pos->right;
			else if(pop == 0) pos = pos->left;
			else return pos;
		}
	}
	void pop() {
		if (!anc) cout << "Empty" << endl;
		else {
			node* pos = search(count); // num��° ��� Ž��
			node* par = pos->par;
			if (par->left == pos) par->left = NULL;
			else if (par->right == pos) par->right = NULL;
			delete pos;
		}
		count--;
	}
	void print() {
		if (!anc) cout << "Empty" << endl;
		else {
			int l = 1;
			for (int num = 1; num <= count; num++) {
				if (l == num) {
					cout << endl;
					l = l * 2;
				}
				cout << search(num)->num << " "; // num��° ��� Ž��
			}
		}
	}
};


void main() {
	tree a;
	char in = ' ';
	int data = 0;

	while (in != '0') {
		cout << "\n\n\n1.push\n2.pop\n3.print\n0.exit\nInput:";
		cin >> in;
		system("cls");
		if (in == '1') {
			cout << "data:";
			cin >> data;
			a.push(data);
		}
		else if (in == '2') {
			a.pop();
		}
		else if (in == '3') {
			a.print();
		}
	}
}