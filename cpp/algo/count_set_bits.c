#include <stdio.h>

// First version:
int CountSetBits(int Num) {
	int count = 0;
	for (; Num; Num >>= 1) {
		if (Num & 1)
			count++;
	}
	return count;
}

// Optimized version:
int CountSetBits_2(int Num)
{
	int count = 0;
	for(; Num; count++){
		Num &= Num -1;
	}
	return count;
}

int main(){
	int x = 0b110000111;
	printf("%d - %d\n", CountSetBits(x), CountSetBits_2(x));
}
