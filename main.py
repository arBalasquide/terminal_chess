#!/usr/bin/env python3.7

import os
import socket

# host board will open a port at TCP to listen for connections
# if player is sending join request, start syncing instances of the board and turns
# pieces are gonna move by typing in moves like e4 kxf7
# pieces need ownership and mutable positions, so make the board and its pieces a class object

def host_board():
    # Create a board with certain settings i.e who is white and who is black? (maybe have a config file?)
    # Set ownership to turns
    sock = socket.socket()
    sock.connect((localhost, 4205)) # def IP address will be the local ip address of the hosting machine

def join_board():

def show_board():
    # Make this into a chess module that defines the board and pieces into their own class
    # 2 Classes Chess Board and Pieces
    # then other child classes for each piece, Bishop, Knight, etc

def main():
    os.system('clear')
    print("Welcome to Terminal Chess")
    print()
    print("1. Solo-board")
    print("2. Host Board")
    print("3. Join Board")


if __name__ == "__main__":
    main()