#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int socket_desc;
    struct sockaddr_in server;
    char *message;

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_desc == -1)
        printf("Could not create socket.\n");

    server.sin_addr.s_addr = inet_addr("192.168.42.84");
    server.sin_family = AF_INET;
    server.sin_port = htons(22);

    // Connect to remote server
    if(connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0) {
        puts("Connection error.\n");

        return 1;
    }

    puts("Connected.\n");

    // Send some date
    message = "I'm in.\n";

    if(send(socket_desc, message, strlen(message), 0) < 0) {
        puts("Send failed.\n");

        return 1;
    }

    puts("Data sent\n");

    return 0;
}
