#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>

void childTask() {
    char name[30];

    printf("Enter your name: ");
    fgets(name, 30, stdin);
    printf("Your name is %s", name);
    exit(0);
}

void parentTask(int i) {
    printf("Waiting for child process to finish...\n");
    wait(NULL);
    if(i == 3)
        printf("Job is done.\n");
}

int main(void) {
    for(int i = 0; i < 4; i++) {
        int pid = fork();

        if(pid == 0) {
            childTask();
        }
        else {
            parentTask(i);
        }
    }

    return 0;
}
