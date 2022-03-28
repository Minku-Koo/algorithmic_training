//T=int(input())

#include <stdio.h>

#include <stdio.h>
int main(){
    int T, d, c;
    scanf("%d", &T);
    for(int i=1; i<T+1; i++){
        scanf("%d", &d);scanf("%d", &c);
        register long long result=1;
        register int num = d/c, rem = d%c, a=0, b=0;
        for(; a < c-rem; a++) result *= num;
        for(; b < rem; b++) result *= num+1;
        printf("#%d %lld\n", i, result);
    }
    return 0;
}
