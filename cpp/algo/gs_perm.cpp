/*
	Generate permutations with only adjacent swaps allowed

	Given a string on length N. You can swap only the adjacent elements and
	each element can be swapped at most once. Find the no of permutations of the
	string that can be generated after performing the swaps as mentioned.

	Examples:
		Input : 12345
		Output: 12345 12354 12435 13245 13254
					21345 21354 21435
	Source: Goldman Sachs Interview
*/

#include <iostream>
using namespace std;

void perm(char s[], int index, int n)
{
	if ( index >= n || index + 1 >= n ){
		cout << s << endl;
		return;
	}

	perm(s, index + 1, n);

	swap(s[index], s[index+1]);
	perm(s, index + 2, n);
	swap(s[index], s[index+1]);
}

int main()
{
	char str[] = "12345";
	perm(str, 0, strlen(str));
}
