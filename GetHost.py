import socket

print("     GetHost  \n Twitter: @moodix0 \n Github: @moodix0 \n")


def host():
    try:
        url = input("Enter URL: ")
        try:
            host = socket.gethostbyname(url)
            try:
                hostname = socket.gethostbyaddr(host)
                print("IP: ", host)
                print("Host Info: ", hostname)
            except Exception as e:
                print("IP: ", host)
                print(f"Host Info: Could not retrieve host info. Reason: {e}")
        except socket.gaierror:
            print(f"Error: '{url}' is not a valid hostname or could not be resolved.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
host()
