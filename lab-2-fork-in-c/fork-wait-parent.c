#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void childTask() {
    printf("Hello, I'm the child.\n");
}

void parentTask() {
    printf("And I am the parent\n");
}

int main(void) {
    pid_t pid = fork();

    if(pid == 0) {
        childTask();
        exit(EXIT_SUCCESS);
    }
    else if(pid > 0) {
        wait(NULL);
        parentTask();
    }
    else
        printf("Unable to create child process.");

    return EXIT_SUCCESS;
}
