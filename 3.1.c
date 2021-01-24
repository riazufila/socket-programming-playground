#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <signal.h>

int main(void) {
    void sig_handler(int sig);
    char s[200];

    if(signal(SIGINT, sig_handler) == SIG_ERR || signal(SIGQUIT, sig_handler) == SIG_ERR || signal(SIGTSTP, sig_handler) == SIG_ERR) {
        perror("signal");
        exit(1);
    }

    printf("Enter a string:\n");

    if(fgets(s, 200, stdin) == NULL)
        perror("gets");
    else
        printf("You entered %s\n", s);
    return 0;
}

void sig_handler(int sig) {
    printf("%d", sig);
    if(sig == 2)
        printf("This is a special signal handler for SIGINT\n");
    else if(sig == 3)
        printf("This is a special signal handler for SIQUIT\n");
    else
        printf("This is a special signal handler for SIGTSTP\n");
}
