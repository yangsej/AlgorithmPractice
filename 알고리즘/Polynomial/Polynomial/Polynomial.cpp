#include "PolyHead.h"

Polynomial::Polynomial(){
	//초기화
	this->terms = 0;
	this->init = NULL;
}
Polynomial::Polynomial(char poly[]){
	//입력받은 poly를 분할 함수 set으로 전송
	this->set(poly);
}
Polynomial::Polynomial(int t, polyin *in){
	//입력받은 값들을 복제
	this->terms = t;
	this->init = new polyin[t];
	for (int i = 0; i < t; i++){
		this->init[i] = in[i];
	}
	//임시 저장 메모리 할당 해제
	delete[] in;
	this->sort();//정렬
}
Polynomial::~Polynomial(){
	//소멸자
	delete[] this->init;
}
void Polynomial::set(){
	//키보드 입력 및 값 설정
	char *poly;
	int max = 1024;
	char *temp;
	poly = new char[max];

	cout << "Polynomial Input(only with variable 'x'): ";
	fgets(poly, max-1, stdin);
	//문자열 크기 초과시 확장
	while (strlen(poly) == max - 1){
		temp = new char[max + 1];
		strcpy(temp, poly);
		delete[] poly;
		poly = new char[max * 2];
		strcpy(poly, temp);
		fgets(temp, max, stdin);
		strcat(poly, temp);
		delete[] temp;
		max = max * 2;
	}

	this->set(poly);
	delete[] poly;
}
void Polynomial::set(char poly[]){
	//외부 입력 및 값 설정
	int len = strlen(poly);
	int &terms = this->terms = 1;
	int i;

	//terms 계산
	for (i = 0; i < len; i++){
		if (poly[i] == '+' || poly[i] == '-') terms++;
	}

	this->init = new polyin[terms];
	int pos = 0;

	for (pos = 0; pos < terms; pos++){
		this->init[pos].exp = 0;
		this->init[pos].coef = 1;
	}

	//문자열=>지수,계수 변환
	int pass = 1; //0:pass_space 1:coef 2:pass_x^ 3:exp
	int sign = 1; //+,-
	if (poly[i] == '-') sign = -1;
	pos = 0;
	i = 0;
	while (i < len){
		if (isspace(poly[i])); //공백 문자
		else if (isdigit(poly[i]) && pass == 1){ //계수
			this->init[pos].coef = atof(&poly[i]) * sign;
			pass = 2;
		}
		else if (poly[i] == 'x'){ //x의 존재여부
			this->init[pos].exp = 1;
		}
		else if (poly[i] == '^'){ //지수의 확인
			pass = 3;
		}
		else if (isdigit(poly[i]) && pass == 3){ //지수
			this->init[pos].exp = atoi(&poly[i]);
			pass = 0;
		}
		else if (poly[i] == '+'){ //+부호
			sign = 1;
			pos++;
			pass = 1;
		}
		else if (poly[i] == '-'){ //-부호
			sign = -1;
			pos++;
			pass = 1;
		}
		i++;
	}

	this->sort(); //정렬
}
Polynomial Polynomial::operator+(const Polynomial &poly){
	//+ 연산
	polyin *init = new polyin[this->terms + poly.terms];
	int Pos1 = 0, Pos2 = 0, Pos3 = 0;
	while ((Pos1 < this->terms) && (Pos2 < poly.terms)){
		//지수가 같은 경우
		if (this->init[Pos1].exp == poly.init[Pos2].exp){ 
			float t = this->init[Pos1].coef + poly.init[Pos2].coef;
			if (t){
				init[Pos3].coef = t;
				init[Pos3].exp = this->init[Pos1].exp;
			}
			Pos1++;
			Pos2++;
		}
		//지수가 다른 경우
		else if (this->init[Pos1].exp > poly.init[Pos2].exp){
			init[Pos3].coef = this->init[Pos1].coef;
			init[Pos3].exp = this->init[Pos1].exp;
			Pos1++;
		}
		else{
			init[Pos3].coef = poly.init[Pos2].coef;
			init[Pos3].exp = poly.init[Pos2].exp;
			Pos2++;
		}
		Pos3++;
	}
	//while 탈출 후 나머지 추가
	for (; Pos1 < this->terms; Pos1++){
		init[Pos3].coef = this->init[Pos1].coef;
		init[Pos3].exp = this->init[Pos1].exp;
	}
	for (; Pos2 < poly.terms; Pos2++){
		init[Pos3].coef = poly.init[Pos2].coef;
		init[Pos3].exp = poly.init[Pos2].exp;
	}
	//복제 생성자 호출
	return Polynomial(Pos3,init);
}
Polynomial Polynomial::operator*(const Polynomial &poly){
	//* 연산
	polyin *init = new polyin[this->terms * poly.terms];
	int Pos3 = 0;
	for (int Pos1 = 0; Pos1 < this->terms; Pos1++){
		for (int Pos2 = 0; Pos2 < poly.terms; Pos2++){
			init[Pos3].coef = this->init[Pos1].coef * poly.init[Pos2].coef;
			init[Pos3].exp = this->init[Pos1].exp + poly.init[Pos2].exp;
			Pos3++;
		}
	}
	//복제 생성자 호출
	return Polynomial(Pos3, init);
}
void Polynomial::operator=(const Polynomial &poly){
	//= 연산
	this->terms = poly.terms;
	this->init = new polyin[this->terms];
	for (int i = 0; i < terms; i++){
		this->init[i] = poly.init[i];
	}
}
bool Polynomial::operator==(const Polynomial &poly){
	//== 연산
	if (this->terms == poly.terms){ //terms 비교
		for (int i = 0; i < terms; i++){ //coef와 exp 비교
			if(this->init[i].coef != poly.init[i].coef
				|| this->init[i].exp != poly.init[i].exp)
				return false;
		}
		return true;
	}
	return false;
}
float Polynomial::Eval(float f){
	//값 대입
	float result = 0.0;
	for (int i = 0; i < terms; i++){
		result += this->init[i].coef * pow(f, this->init[i].exp);
	}
	return result;
}
void Polynomial::sort(){
	//exp 기준 정렬(selection sort)
	int index;
	polyin temp;
	for (int i = 0; i < this->terms - 1; i++){
		index = i;
		for (int j = i + 1; j < terms; j++){
			if (this->init[j].exp > this->init[index].exp) index = j;
			//지수가 같은 것들 결합 후 위치 변경
			else if (this->init[j].exp == this->init[index].exp){ 
				this->init[index].coef += this->init[j].coef;
				for (int k = j; k < terms; k++){
					this->init[k] = this->init[k + 1];
				}
				terms--;
			}
		}
		temp = this->init[index];
		this->init[index] = this->init[i];
		this->init[i] = temp;
	}
}
ostream& operator<<(ostream &os, const Polynomial &poly){
	// cout의 Polynomial에 대한 연산자 오버로딩
	for (int i = 0; i < poly.terms; i++){
		if (poly.init[i].coef != 1) os << poly.init[i].coef;
		if (poly.init[i].exp != 0){
			os << "x";
			if (poly.init[i].exp != 1) os << "^" << poly.init[i].exp;
		}
		if (i + 1 != poly.terms && poly.init[i + 1].coef > 0) os << "+";
	}
	os << endl;

	return os;
}