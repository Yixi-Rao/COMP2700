#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char* msg; 

    msg = malloc(100);
    strcpy(msg, "You guessed the password, but where is the flag?\n");
    printf(msg);
    printf(*msg);
    return 0;
}