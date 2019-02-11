// Write a function that takes in a string parameter and checks whether
// or not it is an integer, and if it is then return the integer value.

#include <stdio.h>
#include <stdlib.h>

int strtoint(const char *s)
{
    int index = 0, flag = 0;

    while( *(s+index) != '\0'){
        if( (*(s + index) >= '0') &&
                *(s + index) <= '9'){
            flag = 1;
            index++;
        }
        else {
            flag = 0;
            break;
        }
    }

    return ( flag ? atoi(s) : 0 );
}

int main()
{
    printf("%d\n", strtoint("0123"));
    printf("%d\n", strtoint("0123ii"));
}
