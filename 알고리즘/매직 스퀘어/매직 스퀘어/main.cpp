#include <iostream>
using namespace std;
#include <crtdbg.h>

void main(){
	int size = 0;
	while (size < 1){
		cout << "매직 스퀘어의 크기: ";
		cin >> size;
	}

	int **square = new int*[size];
	for (int a = 0; a < size; a++){
		square[a] = new int[size];
		for (int b = 0; b < size; b++){
			square[a][b] = 0;
		}
	}

	int i = 0;
	int j = size / 2;
	int num = 1;
	while (num <= size*size){
		square[i][j] = num;
		i = (i + size - 1) % size;
		j = (j + size - 1) % size;
		if (square[i][j] != 0){
			i = (i + size + 2) % size;
			j = (j + size + 1) % size;
		}
		num++;
	}

	for (i = 0; i < size; i++){
		for (j = 0; j < size; j++){
			printf("%3i ",square[i][j]);
		}
		printf("\n");
		delete[] square[i];
	}
	delete[] square;

	_CrtDumpMemoryLeaks();
}