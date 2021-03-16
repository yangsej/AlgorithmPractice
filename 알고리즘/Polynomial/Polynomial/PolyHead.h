#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
#include <crtdbg.h>

typedef struct polyin{
	float coef; //계수
	int exp; //지수
}polyin;

class Polynomial{
private:
	int terms; //항의 개수
	polyin *init;
	Polynomial(int t, polyin *in); //복제 생성자
public:
	Polynomial(); //초기화 생성자
	Polynomial(char poly[]); //입력 생성자
	~Polynomial(); //소멸자
	void set(); //키보드 입력
	void set(char poly[]); //문자열->지수&계수 변환
	friend ostream& operator<<(ostream &os, const Polynomial &poly); //cout
	Polynomial operator+(const Polynomial &poly); //+연산
	Polynomial operator*(const Polynomial &poly); //*연산
	void operator=(const Polynomial &poly); //=연산
	bool operator==(const Polynomial &poly); //==연산
	float Eval(float f); //값 대입
	void sort(); //정렬
};
