#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int socket_desc;
    struct sockaddr_in server;
    char *message, *server_reply;

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_desc == -1)
        printf("Could not create socket.\n");

    server.sin_addr.s_addr = inet_addr("192.168.42.84");
    server.sin_family = AF_INET;
    server.sin_port = htons(22);

    // Connect to remote server
    if(connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0) {
        puts("Connection error.");

        return 1;
    }

    puts("Connected.");

    // Send some date
    message = "I'm in.";

    if(send(socket_desc, message, strlen(message), 0) < 0) {
        puts("Send failed.");

        return 1;
    }

    puts("Data sent\n");

    // Receive a reply from the server
    if(recv(socket_desc, server_reply, 2000, 0) < 0) {
        puts("Failed to receive reply from server.");

        return 1;
    }

    printf("Received reply from server %s\n", server_reply);
    close(socket_desc);

    return 0;
}
