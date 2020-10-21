#include <stdlib.h> /* Needed to define exit() */
#include <unistd.h> /* Needed for fork() and getpid() */
#include <stdio.h> /* Needed for printf() */

int main(int argc, char **argv) {
    int pid; /* Process ID */

    switch(pid = fork()) {
        case 0: /* A fork returns 0 to the child */
            printf("I am the child process pid=%d\n", getpid());
            break;

        default: /* A fork returns a pid to the parent */
            printf("I am the parents process pid=%d, child pid=%d\n", getpid(), pid);
            break;

        case 1: /* Something went wrong */
            perror("fork");
            exit(1);
    }

    exit(0);
}
