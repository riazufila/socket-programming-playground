#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <signal.h>

int main(void) {
    void sigint_handler(int sig);

    if(signal(SIGINT, sigint_handler) == SIG_ERR) {
        perror("Signal");
        exit(1);
    }

    int number;
    int pipefds[2];
    int buffer;
    pipe(pipefds);

    pid_t pid = fork();

    if(pid == 0) {
        close(pipefds[0]);
        printf("Enter a number to check if its primary or not: ");
        scanf("%d", &number);
        write(pipefds[1], &number, sizeof(number));
        printf("Passing control back to parent...\n");

        exit(EXIT_SUCCESS);
    }
    else if(pid > 0) {
        printf("Passing control to child process...\n");
        wait(NULL);
        close(pipefds[1]);
        read(pipefds[0], &buffer, sizeof(int));
        close(pipefds[0]);

        if(buffer <= 3) {
            if(buffer == 1) {
                printf("%d is not a prime number.\n", buffer);
            }
            else {
                printf("%d is a prime number.\n", buffer);
            }
            
            exit(EXIT_SUCCESS);
        }

        if(buffer > 3) {
            for(int i = 2; i <= buffer / 2; i++) {
                if(buffer % i == 0) {
                    printf("%d is not a prime number.\n", buffer);
                    exit(EXIT_SUCCESS);
                }
                else {
                    printf("%d is a prime number.\n",buffer);
                    exit(EXIT_SUCCESS);
                }
            }
        }

        printf("Job is done.\n");
    }
    else {
        perror("Error");
    }

    return EXIT_SUCCESS;
}

void sigint_handler(int sig) {
    printf("Don't try to end this program!\n");
}

