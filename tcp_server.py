import socket
import sys
from argparse import ArgumentParser

MAX_RECV_DATA_SIZE = 100
BINARY_CHUNK_SIZE = 1024

DEFAULT_PORT = 3490
DEFAULT_BINARY_PATH = './build/example_app/example_app_fota_image_encrypted.bin'


def _main():
    parser = ArgumentParser(
        description='Run TCP server, wait for connection and send new firmware file to connected device')
    parser.add_argument('-b',
                        '--binary-file',
                        help='Path to the firmware file to be sent (*.bin)',
                        default=DEFAULT_BINARY_PATH)
    parser.add_argument('-p', '--port', help='TCP server port', default=DEFAULT_PORT)

    args = parser.parse_args()

    print(f"Using binary path: {args.binary_file}")
    print(f"Using port: {args.port}")

    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockfd.bind(('', args.port))
    sockfd.listen(10)

    print('Waiting for connections...')

    try:
        new_fd, addr = sockfd.accept()
        sockfd.close()
        print(f"Got connection from {addr}")

        user_input = " "
        while user_input:
            user_input = input("Press Enter to trigger update: ")

        with open(args.binary_file, 'rb') as file:
            already_sent = 0
            while True:
                buffer = file.read(BINARY_CHUNK_SIZE)
                if not buffer:
                    break

                already_sent += len(buffer)
                print(f"Sending {len(buffer)} bytes to {addr}: sent = {already_sent} bytes")
                new_fd.sendall(buffer)

                data = new_fd.recv(MAX_RECV_DATA_SIZE - 1)
                if not data:
                    break

        print(f"Closing {args.binary_file}")
        new_fd.close()
    except socket.error as e:
        print(f"Error accepting connection: {e}")
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    _main()
