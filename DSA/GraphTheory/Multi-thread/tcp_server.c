// Create a tcp server with multi-thread use c code and pthread

#include <stdio.h>
#include <stdlib.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

// use a buffer pool copy all messages in the buffer pool
// After running for 10 secs, print all messages in the buffer pool


// use a buffer pool copy all messages in the buffer pool

// After running for 10 secs, print all messages in the buffer pool

// use a buffer pool copy all messages in the buffer pool

char* buffer_pool[1024]; // 1MB 
// protect buffer_pool_size and buffer_pool using mutex lock
int buffer_pool_size = 0;

// create a mutex lock
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;


void* print_buffer_pool(void* arg) {
    while (1) {
        sleep(10);
        // acquire mutex lock
        pthread_mutex_lock(&mutex);

        printf("Buffer pool:\n");
        for (int i = 0; i < buffer_pool_size; i++) {
            printf("%s\n", buffer_pool[i]);
        }

        // release mutex lock
        pthread_mutex_unlock(&mutex);
    }
}

void add_to_buffer_pool(const char* message, int bytes) {
    // concatenate message to buffer_pool
    char* new_message = (char*)malloc(bytes);
    memcpy(new_message, message, bytes);
    buffer_pool[buffer_pool_size++] = new_message;
}


void* handle_client(void* arg) {
    int client_fd = *(int*)arg;
    char buffer[1024];
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        int bytes = recv(client_fd, buffer, sizeof(buffer), 0);
        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        // add message to buffer pool
        pthread_mutex_lock(&mutex);
        add_to_buffer_pool(buffer, bytes);
        pthread_mutex_unlock(&mutex);

        send(client_fd, buffer, strlen(buffer), 0);
    }
    close(client_fd);
    return NULL;
}

int main(int argc, char* argv[]) {

    // init mutex lock
    pthread_mutex_init(&mutex, NULL);

    if (argc != 2) {
        fprintf(stderr, "Usage: ./tcp_server <port>\n");
        return -1;
    }

    int port = atoi(argv[1]);
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) {
        fprintf(stderr, "Failed to create socket\n");
        return -1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        fprintf(stderr, "Failed to bind\n");
        return -1;
    }

    if (listen(server_fd, 10) < 0) {
        fprintf(stderr, "Failed to listen\n");
        return -1;
    }

    // call print_buffer_pool in a new thread
    pthread_t tid_pool;
    pthread_create(&tid_pool, NULL, print_buffer_pool, NULL);


    while (1) {
        struct sockaddr_in client_addr;
        int client_fd = accept(server_fd, NULL, NULL);
        if (client_fd < 0) {
            fprintf(stderr, "Failed to accept\n");
            return -1;
        }

        pthread_t tid;
        pthread_create(&tid, NULL, handle_client, &client_fd);
        pthread_detach(tid);
    }

    close(server_fd);
    // join print_buffer_pool thread
    pthread_join(tid_pool, NULL);

    return 0;
}

