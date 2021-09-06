#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    int socket_desc, new_socket;
    struct sockaddr_in server, client;
    
    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_desc < 0) {
        perror("socket()");
    }
    
    // Prepare sock_addr
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(4545);

    // Bind socket
    if(bind(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("bind()");
    }

    // Listen for connection
    listen(socket_desc, 3);

    // Accept incoming connection
    int sizeOfStruct = sizeof(struct sockaddr_in);
    char message[2000], buffer[2000];

    while(new_socket = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&sizeOfStruct)) {
        // Receive data from client
        recv(new_socket, buffer, 2000, 0);
        printf("CLIENT: %s\n", buffer);

        // Send data to client
        fgets(buffer, 2000, stdin);
        send(new_socket, buffer, 2000, 0);
    }

    if(new_socket < 0)
        perror("accept()");

    return 0;
}
