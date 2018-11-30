#include <stdio.h>
#include <stdlib.h>

// Can I put a queen on (i, col)?
#define attack(i, j, col) (hist[j] == i || abs(hist[j] - i) == col - j)

int count = 0;

// Use an array to memorize the positions.
//  hist[j] = i : for the j-th column, a queen is on the i-th row
//  Hence, (hist[j], j) has one queen

// Check the col-th column, which position can hold a QUEEN
void solve(int n, int col, int *hist){
    /*
    printf("Checking %3d%3d for hist=", n, col);
    for (int c=0; c<col; ++c) printf("%2d", hist[c]);
    putchar('\n');
    */
    if (col == n) {
        // We find one solution, print it out
        printf("No. %5d:  ", ++count);
        for (int i = 0; i< n; ++i) printf("%3d", hist[i]);
        putchar('\n');
    }else{
        for (int i = 0, j = 0; i < n; i++) {
            for (j = 0; j < col && !attack(i, j, col); j++);
            if (j < col) continue;  // Find one attack
     
            hist[col] = i;
            solve(n, col + 1, hist);
        }
    }
}
 
int main(int n, char **argv)
{
    if (n <= 1 || (n = atoi(argv[1])) <= 0) n = 8;
    int hist[n];
    solve(n, 0, hist);
}
