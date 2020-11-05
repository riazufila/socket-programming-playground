#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    int socket_desc, new_socket, c;
    struct sockaddr_in server, client;
    char message[2000] = "This message is from the server!";

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if(socket_desc == -1)
        printf("Could not create socket.");

    // Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( 4545 );

    // Bind the socket
    if(bind(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
        puts("Bind failed.");

    puts("Binding completed.");

    // Listen for connection
    listen(socket_desc, 3);

    // Accept incoming connection
    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);
    new_socket = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);

    if(new_socket < 0)
        perror("Accepting Connection Failed");

    // Send data to client
    send(new_socket, message, 2000, 0);

    return 0;
}
