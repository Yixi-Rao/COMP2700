#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include "ctf.h"

#define BUFSIZE 25
#define MAXGAME 10

char flag[32]; 

void welcome()
{
	setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

	printf("Win %d games to receive the prize!\n", MAXGAME); 
}

// secure random number generator using /dev/urandom
int getrand()
{
	static int i = 0;
	static unsigned char randbuf[64];

	int fd; 
	int val; 

	if(i == 0)
	{
		fd = open("/dev/urandom", O_RDONLY); 
		if(fd < 0)
		{
			printf("random number generation failed\n");
			exit(1);
		}
		read(fd, randbuf, 32); 
		close(fd); 
	}
	
	val=(int) randbuf[i]; 
	i = (i+1) % 64;
	return val; 
}

void Win()
{
	read_flag(flag); 
	printf("%s\n", flag); 
}

int
main(int argc, char *argv[])
{
    int pos = 0; // 0: even, 1: odd
	int c=1; 
	int valid; 
	int human;
	int computer; 
	int win=0;
	int game=1;
	char answer[BUFSIZE]; 

	welcome();

    printf("Choose a positon: \n");
    printf("[1] Even\n");
    printf("[2] Odd\n");
    do {
        printf("> "); 
        fgets(answer, BUFSIZE, stdin);
        if(answer[0] == '1') { pos = 0; break; }
        else if(answer[0] == '2') { pos = 1; break; }
        else printf("Invalid selection\n"); 
    } while(1);

	while(c) {
		if(game > MAXGAME) {
			printf("Maximum number of games reached\n");
			break; 
		}

		computer = getrand() % 10 + 1; 
		do {
			printf("[#%2d] Input a number between 1-10\n", game);
			printf("> "); 
			fgets(answer,BUFSIZE,stdin);
			human=atoi(answer);
			valid=0;
			if(human < 1 || human > 10) {
				valid=0; 
				printf("That's not a valid move: ");
				printf(answer); 
			} else valid=1;
		} while(!valid); 

		printf("Computer's move: %d\nYour move: %d\n", computer, human); 
		if((computer + human) % 2 == pos) {
			printf("You won this round.\n");
			++win;
		}
		else {
			printf("You lost this round.\n"); 
		}

		++game; 				
		printf("Play again?\n[1] Yes\n[2] No\n> ");
		fgets(answer, BUFSIZE, stdin); 
		if(answer[0] == '1') c = 1; 
		else c=0;
	}
	
	printf("You won %d times.\n", win); 

	if (win == MAXGAME) {
		Win();
	}
	else {
		printf("Sorry no prize for you!\n");
	}
	goodbye();
	return 0;
}

void goodbye()
{
	printf("Goodbye...\n");
}


