#include <cstdio>

int main(){
    int a, b, c, d, e, f, x, y;
    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);

    x = (b*f - c*e)/(b*d - a*e);
    if(a != 0 && b != 0) y = (-a*x+c)/b;
    else if(d != 0 && e != 0) y = (-d*x+f)/e;
    else if(a == 0) y = c/b;
    else if(d == 0) y = f/e;

    printf("%i %i\n", x, y);

    return 0;
}