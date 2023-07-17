import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 8080)

# Get a number from the user
number = int(input('Enter a number: '))

# Send the number to the server
client_socket.sendto(str(number).encode(), server_address)

# Receive the result from the server
response, _ = client_socket.recvfrom(1024)
result = response.decode()

if result == 'True':
    print(number, 'is a Prime Number')
else:
    print(number, 'is not a Prime Number')

# Close the socket
client_socket.close()
