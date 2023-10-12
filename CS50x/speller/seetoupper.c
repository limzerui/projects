#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main (int argc, char * argv[])
{
    char * word = "bear";
    int upW = toupper(word[0]);
    int upA = 'A';
    int val =  upW - upA;
    int raV = atoi(argv[1]);
    printf ("upW=%d,%c, upA=%d,%c, val=%d, raV=%d,%c\n", upW, upW, upA, upA, val, raV, raV);
    return 0;
}