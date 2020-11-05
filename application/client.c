#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
    int socket_desc;
    struct sockaddr_in server;

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_desc < 0)
        perror("socket()");

    server.sin_addr.s_addr = inet_addr("192.168.42.84");
    server.sin_family = AF_INET;
    server.sin_port = htons( 4545 );

    // Connect to remote server
    if(connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("connect()");

        return 1;
    }

    // Send some date
    char message[2000];
    fgets(message, 2000, stdin);
    send(socket_desc, message, 2000, 0);

    // Receive data
    char buffer[2000];
    recv(socket_desc, buffer, 2000, 0);
    printf("SERVER: %s\n", buffer);

    return 0;
}
