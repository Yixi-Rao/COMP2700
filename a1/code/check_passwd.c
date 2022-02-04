#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "ctf.h"

char flag[32];


// remove trailing whitespace
void remove_whitespace(char *s)
{
    int i = 0; 
    while(s[i] != '\0') {
        if(s[i] == '\n' || s[i] == ' ' || s[i] == '\t' || s[i] == '\r') {
            s[i] = '\0'; 
            break; 
        }
        i++;
    }
}

void welcome()
{
    // Disable input/output buffering
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("COMP2700 Assignment 1\n");
    printf("=====================\n"); 
}

void ask_passwd(char * pass)
{
    char buf[20];
    printf("Enter password: ");
    fgets(buf,20,stdin);
    strcpy(pass, buf);
}

int main()
{
    char* msg; 
    char answer[14];

    welcome(); 
    msg = malloc(100);
    strcpy(msg, "You guessed the password, but where is the flag?\n");
    read_flag(flag); 

    ask_passwd(answer); 
    remove_whitespace(answer);
    answer[13] = '\0';

    if(strcmp(answer, "Q6VWQSXFZB") == 0) {
        printf("%s\n", msg); 
    }
    else printf("Sorry, try again\n");

    goodbye();
    return 0;
}

void goodbye()
{
    printf("\nProgram exited normally.\n");
}