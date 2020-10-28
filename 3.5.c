#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

void sigint_handler(int sig) {
    printf("Don't try to end this program!\n");
}

int main(void) {
    int number;
    int pipefds[2];
    int buffer;

    pipe(pipefds);
    pid_t pid = fork();

    if(pid == 0) {
        printf("Please enter a number: ");
        scanf("%d", &number);
        close(pipefds[0]);
        write(pipefds[1], &number, sizeof(number));
        exit(EXIT_SUCCESS);
    }
    else if(pid > 0) {
        wait(NULL);
        close(pipefds[1]);
        read(pipefds[0], &buffer, sizeof(number));
        close(pipefds[0]);
        printf("The number entered is %d", &number);
    }
    else {
        perror("Error");
    }

    return 0;
}
