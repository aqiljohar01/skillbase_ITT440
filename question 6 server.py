import socket

def i_prime(n):
    if a < 2:
        return False
    for t in range(2, int(a**0.5) + 1):
        if a % t == 0:
            return False
    return True

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    number = int(data.decode())

    # Check if the number is prime
    result = is_prime(number)

    # Send the result back to the client
    response = str(result).encode()
    server_socket.sendto(response, client_address)
