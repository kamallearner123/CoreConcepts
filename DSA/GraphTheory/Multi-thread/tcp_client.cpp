// Write TCP cliet program that connects to the server and sends the message to the server.

#include <iostream>
#include <string>
#include <thread>
#include <vector>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>



int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: ./tcp_client <ip> <port>" << std::endl;
        return -1;
    }

    int port = std::stoi(argv[2]);
    int client_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (client_fd < 0) {
        std::cerr << "Failed to create socket" << std::endl;
        return -1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    inet_pton(AF_INET, argv[1], &server_addr.sin_addr);

    if (connect(client_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        std::cerr << "Failed to connect" << std::endl;
        return -1;
    }

    std::string message;
    while (true) {
        std::cout << "Enter message: ";
        std::getline(std::cin, message);
        if (message == "exit") {
            break;
        }
        send(client_fd, message.c_str(), message.size(), 0);
        char buffer[1024];
        memset(buffer, 0, sizeof(buffer));
        recv(client_fd, buffer, sizeof(buffer), 0);
        std::cout << "Received: " << buffer << std::endl;
    }

    close(client_fd);
    return 0;
}

// Usage: ./tcp_client <ip> <port>
// Enter message: Hello
// Received: Hello
// Enter message: exit




