#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define _XOPEN_SOURCE
#include <crypt.h>

#include "ctf.h"

#define PREFIX "/ctf/readlog/00OTH7"

void check(char *s)
{
    int i;
    for(i=0; i < strlen(s); ++i)
    {
        if(!isalnum(s[i]) && s[i] != '.')
        {
            printf("File names can only contain alphanumeric characters\n");
            exit(1);
        }
    }
}

void showlog(char *filename)
{
    FILE * fp;
    char buffer[1024];
    char plaintext[1024];
    int n = 0; 
    fp = fopen(filename, "r");
    if(fp == NULL)
    {
        printf("Failed opening log file %s\n", filename);
        exit(1);
    }
    
    n=fread(buffer, 1, 1024, fp); 
    if(n >= 1)
    {
        decrypt_log(plaintext, buffer, n); 
        printf("%s\n", plaintext);
    } 
    else printf("Failed reading the log file %s\n", filename);
}

void userlog(char *s)
{
    char filename[128] = PREFIX; 

    strcat(filename, "/user/");
    strcat(filename, s);
    showlog(filename);
}


// remove newline
void remove_newline(char *s)
{
    int i = 0; 
    while(s[i] != '\0') {
        if(s[i] == '\n') {
          s[i] = '\0'; 
          break; 
        }
        i++;
    }
}

int auth(char *passwd)
{
    char str[]="$6$abcdef$T7Fkett7UpQGQBZO75cAJuoDUyTXTmbt1h646lXIid2TGOj37vQwDJCKmGCxVmcaj393PnovjbdCnZ14qd8/j0";
    char * hash;
    char salt[]="$6$abcdef";

    hash = crypt(passwd, salt); 
    if(strcmp(hash, str) == 0)
        return 1;

    return 0; 
}

void systemlog(char *s)
{
    char filename[128] = PREFIX; 
    char password[20]; 

    strcat(filename, "/system/");
    strcat(filename, s);
    
    printf("Enter the password to view system logs: "); 
    fgets(password, 20, stdin);
    remove_newline(password); 

    if(auth(password))
        showlog(filename);
    else
        printf("Incorrect password\n");     
}

int main(int argc, char *argv[])
{
    char filename[16];

    printf("Working directory: %s\n", PREFIX);
    if(argc != 3)
    {
        printf("Usage:\n");
        printf("To show user logs, run:   %s -u <filename>\n", argv[0]);
        printf("To show system logs, run: %s -s <filename>\n", argv[0]);  
        return 0;     
    }
    strncpy(filename, argv[2], 15);
    filename[15] = '\0';

    check(filename);

    if(strcmp(argv[1], "-u") == 0)
        userlog(filename);
    else if(strcmp(argv[1], "-s") == 0)
        systemlog(filename);
    else printf("Invalid option\n");

    return 0;
}