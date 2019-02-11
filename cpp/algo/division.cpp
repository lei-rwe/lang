/*
   Use of this program, for any purpose, is granted the author,
   Ian Kaplan, as long as this copyright notice is included in
   the source code or any source code derived from this program.
   The user assumes all responsibility for using this code.
   Ian Kaplan, October 1996
*/
#include <stdio.h>
#include <stdlib.h>

void unsigned_divide(unsigned int dividend,
             unsigned int divisor,
             unsigned int &quotient,
             unsigned int &remainder )
{
  unsigned int t, num_bits;
  unsigned int q, bit, d;
  int i;

  remainder = 0;
  quotient = 0;

  if (divisor == 0) return;

  if (divisor > dividend) {
    remainder = dividend;
    return;
  }

  if (divisor == dividend) {
    quotient = 1;
    return;
  }

  num_bits = 32;

  while (remainder < divisor) {
    bit = (dividend & 0x80000000) >> 31;
    remainder = (remainder << 1) | bit;
    d = dividend;
    dividend = dividend << 1;
    num_bits--;
  }

  /* The loop, above, always goes one iteration too far.
     To avoid inserting an "if" statement inside the loop
     the last iteration is simply reversed. */

  dividend = d;
  remainder = remainder >> 1;
  num_bits++;

  for (i = 0; i < num_bits; i++) {
    bit = (dividend & 0x80000000) >> 31;
    remainder = (remainder << 1) | bit;
    t = remainder - divisor;
    q = !((t & 0x80000000) >> 31);
    dividend = dividend << 1;
    quotient = (quotient << 1) | q;
    if (q) {
       remainder = t;
     }
  }
}  /* unsigned_divide */

int main(int argc, char *argv[]){
	unsigned int dividend = (unsigned int)(atoi(argv[1]));
    unsigned int divisor  = (unsigned int)(atoi(argv[2]));
    unsigned int quotient;
    unsigned int remainder;

    unsigned_divide(dividend, divisor, quotient, remainder);
    printf("%d / %d = %d ... %d\n", dividend, divisor, quotient, remainder);
}
