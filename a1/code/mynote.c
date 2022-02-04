#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ctf.h"


void welcome()
{
     // Disable input/output buffering
     setbuf(stdin, NULL);
     setbuf(stdout, NULL);
     setbuf(stderr, NULL);

     printf("Welcome to mynotes\n");
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

void encrypt_notes(char * filename)
{
     char password[32] = "";
     char encfile[150] = "";
     char cmd[200];
     
     strcat(encfile, filename); 
     strcat(encfile, ".enc"); 

     printf("Enter password: ");
     fgets(password, 32, stdin);
     remove_newline(password);
     if(strcmp(password, "") == 0)
     {
          // no password given, use default password
          default_password(password); 
     } 

     sprintf(cmd, "/usr/bin/openssl enc -aes-128-cbc -in %s -out %s -k %s -pbkdf2", filename, encfile, password); 
     system(cmd); 
}

// Sanitise input to prevent code injection
void sanitise(char * s)
{
    while(*s)
    {
        if(*s == ';' || *s == '&' || *s == '|' || *s == '>' || *s == '<') {
            *s = '\0';
            return; 
        }
        ++s;
    }
}

void decrypt_notes(char * filename)
{
     char password[32] = "";
     char decfile[100] = "";
     char cmd[200];
     
     printf("Enter file to decrypt: ");
     fgets(decfile, 100, stdin); 
     remove_newline(decfile); 

     printf("Enter password: ");
     fgets(password, 32, stdin);
     remove_newline(password);

     strcpy(filename, decfile);
     strcat(filename, ".plain"); 

     sprintf(cmd, "/usr/bin/openssl enc -d -aes-128-cbc -in %s -out %s -k %s -pbkdf2", 
               decfile, filename, password); 
     system(cmd); 
}


int  main(int argc, char * argv[], char *envp[])
{  
     char command[256];
     char menu[10];
     char notes[128];
     char filename[128] = "";
     char input[128]; 

     welcome();
     strcat(filename,"mynotes.txt");     
     do {
          printf("Current File: [%s]", filename); 
          printf("\nWhat would you like to do? \n");
          printf("[1] Switch notes\n"); 
          printf("[2] Add notes\n");
          printf("[3] Read notes\n");
          printf("[4] Encrypt notes\n");
          printf("[5] Decrypt file\n"); 
          printf("[6] Quit\n");
          printf("Enter your choise (1-6): ");
          fgets(menu,10,stdin);

          switch(menu[0]) {
               case '1': 
                    printf("Enter the file name: ");
                    fgets(input, 128, stdin); 
                    remove_newline(input); 
                    sanitise(input); 
                    if(strcmp(input,"") != 0) 
                         strcpy(filename, input); 
                    break;
               case '2':
                    printf("Please type in your notes (128 characters max.):\n");
                    fgets(notes, 128, stdin);
                    sanitise(input); 
                    sprintf(command, "/bin/echo '%s' >> %s", notes, filename);
                    system(command);
                    break;
               case '3':
                    sprintf(command,"/bin/cat %s", filename);
                    system(command);
                    break;
               case '4':
                    encrypt_notes(filename); 
                    break;
               case '5':
                    decrypt_notes(filename);
                    break;
          }
     }
     while(menu[0] != '6');

     goodbye();
     return 0;
}

void goodbye()
{
     printf("Goodbye..\n");
}