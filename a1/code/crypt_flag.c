#include <stdio.h>
#include <libgen.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define _XOPEN_SOURCE
#include <crypt.h>

#include "ctf.h"


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

int main(int argc, char *argv[])
{
    char cmd[100] = "";
    char pass[32]; 
    char key[33]; 
    char iv[33];
    char env_key[100] = "MYKEY="; 
    char env_iv[100] = "MYIV=";
    char *file_dir = dirname(realpath(argv[0], NULL));

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    chdir(file_dir);
    load_key(iv,key); 

    // set the environment variables for the decryption key
    strcat(env_key, key); 
    if(putenv(env_key))
    { 
        printf("Failed setting environment variable MYKEY.\n");
        exit(1);
    }
    strcat(env_iv, iv); 
    if(putenv(env_iv))
    { 
        printf("Failed setting environment variable MYIV.\n");
        exit(1);
    }

    printf("Enter the password to unlock the flag: ");
    fgets(pass, 31, stdin);
    strtok(pass, "\n"); 
    sanitise(pass);

    if(auth(pass)) {
        system("./decrypt.sh");
    }
    else {
        sprintf(cmd, "/bin/echo \"\u274c Wrong password: %s\"", pass); 
        system(cmd); 
    }
    
    return 0;
}
