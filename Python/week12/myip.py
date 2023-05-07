import socket


def main():
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)

    print("Az IP címed:", ip_address)

if __name__ == "__main__":
    main()