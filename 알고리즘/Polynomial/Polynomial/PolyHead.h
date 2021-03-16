#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
#include <crtdbg.h>

typedef struct polyin{
	float coef; //���
	int exp; //����
}polyin;

class Polynomial{
private:
	int terms; //���� ����
	polyin *init;
	Polynomial(int t, polyin *in); //���� ������
public:
	Polynomial(); //�ʱ�ȭ ������
	Polynomial(char poly[]); //�Է� ������
	~Polynomial(); //�Ҹ���
	void set(); //Ű���� �Է�
	void set(char poly[]); //���ڿ�->����&��� ��ȯ
	friend ostream& operator<<(ostream &os, const Polynomial &poly); //cout
	Polynomial operator+(const Polynomial &poly); //+����
	Polynomial operator*(const Polynomial &poly); //*����
	void operator=(const Polynomial &poly); //=����
	bool operator==(const Polynomial &poly); //==����
	float Eval(float f); //�� ����
	void sort(); //����
};
