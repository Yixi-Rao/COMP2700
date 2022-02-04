int main() {
    char *correct;
    correct = malloc(150);
    char passwd[14];
    char input[20];
    int index = 0;

    strcpy(correct, "password is correct!");
    printf("type the password: ");
    fgets(input, 20, stdin);
    strcpy(passwd, input);

    while (passwd[index] != '\0') {
        if (passwd[index] == ' ' || passwd[index] == '\n'){
            passwd[index] = '\0';
            break;
        }
        index++;
    }
    passwd[13] = '\0';

    if (strcmp(passwd, "0123456789") == 0) {
        printf("%s\n", correct);
        return 0;
    } else {
       printf("false");
       return 0; 
    }
        
}