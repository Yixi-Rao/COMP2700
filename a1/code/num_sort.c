#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "ctf.h"


#define MAX_ELEMENTS 14
#define LIMIT 7
#define GUARD 2984

char flag[32]; 

void welcome()
{
    // Disable input/output buffering
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("Welcome to num_sort.\n");
}

void Win()
{
    read_flag(flag);
    printf("%s\n", flag);
}

int add_entries(int * arr, int i)
{
    char answer[20];
    int k = 0; 
    int end=0; 
    
    if(i >= MAX_ELEMENTS) {
        printf("Buffer is full\n");
        return i; 
    }

    printf("Input your numbers. Type 'end' to end the input.\n");
    while(end < LIMIT) 
    {
        printf(">> ");
        fgets(answer, 19, stdin);
        if(strcmp(answer,"end\n") == 0)
            break; 
        k = atoi(answer); 
        
        arr[i++] = k; 
        ++end; 
    }

    return i; 
}

int cmpfunc(const void *a, const void *b)
{
    return (*((int*)a) < *((int *)b));
}

void sort(int * arr, int n)
{
    qsort(arr, n, sizeof(int), cmpfunc);
}

void show_list(int arr[], int n)
{
    int i=0;
    if(n == 0) {
        printf("Your list is empty.\n"); 
        return; 
    }
    printf("Here are the elements of the list: \n"); 
    for(i=0; i<n; ++i)
    {
        printf("%d\n", arr[i]); 
    }
}


int main()
{
    int a = 0; 
    int numbers[MAX_ELEMENTS]; 
    int max = 0;  
    int n = 1;
    char select[8];

    welcome(); 
    while(n != 5) {
        printf("[1] Add entries to list\n");
        printf("[2] Reset list\n"); 
        printf("[3] Sort list\n");
        printf("[4] Show list\n"); 
        printf("[5] Exit\n"); 
        printf("> "); 
        fgets(select, 7, stdin);
        n = atoi(select);
        switch(n) {
            case 1: 
                max=add_entries(numbers, max);
                break;
            case 2:
                max=0;
                break;
            case 3:
                sort(numbers, max); 
                break;
            case 4:
                show_list(numbers, max); 
                break;
        }
    }
 
    goodbye(); 

    if(a == GUARD) 
    {
        Win(); 
    }

    return 0;
}

void goodbye()
{
    printf("Goodbye..\n");
}