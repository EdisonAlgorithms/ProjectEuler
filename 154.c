#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

#define L 200000
#define P2 199983
#define P3 49987

unsigned long p(unsigned long n, unsigned long d) {
    unsigned long div = d;
    unsigned long ret = 0;
    while (div <= n) {
        ret += n / div;
        div *= d;
    }
    return ret;
}

unsigned long* p_list(unsigned long n, unsigned long d) {
    unsigned long i;
    unsigned long* ret = malloc((n + 1) * sizeof(unsigned long));
    for (i = 0; i <= n; i++)
        ret[i] = p(i, d);
    return ret;
}

int main(int argc, char** argv) {
    unsigned long k1, k2, k3;
    unsigned long long ans = 0;

    unsigned long* p2 = p_list(L, 2);
    unsigned long* p5 = p_list(L, 5);

    for (k1 = 0; k1 < L / 3; k1++) {
        for (k2 = k1; k2 <= L - k1 - k2; k2++) {
            k3 = L - k1 - k2;
            if (p2[k1] + p2[k2] + p2[k3] < P2 && p5[k1] + p5[k2] + p5[k3] < P3) {
                if (k1 == k2 || k2 == k3) {
                    ans += 3;
                } else {
                    ans += 6;
                }
            }
        }
    }

    free(p2);
    free(p5);

    printf("answer: %lld\n", ans);

    return 0;
}