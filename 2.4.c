#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>

void childTask() {
    char name[30];

    printf("Enter your name: ");
    fgets(name, 30, stdin);
    printf("Your name is %s", name);
}

void parentTask() {
    printf("Waiting for child process to finish...\n");
    wait(NULL);
    printf("Job is done.\n");
}

int main(void) {
    for(int i = 0; i < 5; i++) {
        int pid = fork();

        if(pid == 0) {
            childTask();
        }
        else if(pid > 0) {
            parentTask();
        }
    }

    return 0;
}
