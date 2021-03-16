#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

int main() {
   int n, k, i;
   FILE* fp = fopen("C:/Python27/randomcount.txt", "r");
   fscanf(fp, "%d %d", &n, &k);
   vector<int> v(n);
   
   for (int i = 0; i < n; i++) {
      fscanf(fp, "%d", &v[i]);
   }
   fclose(fp);

   clock_t start = clock();
   sort(v.begin(),v.end());
   printf("%0.5f\n", (float)(clock() - start) / CLOCKS_PER_SEC);

   int count = 0;
   int min = 0;
   for (i = 0; i < n; i++) {
      if (min != v[i]) {
         min = v[i];
         count = 1;
      }
      else count++;
      if (count >= k) {
         printf("%d\n", v[i]);
         return 0;
      }
   }
   printf("-1\n");
   return 0;
}