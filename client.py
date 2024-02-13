import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


add_drug = {"Escitalopram": "is used to treat depression and generalized anxiety disorder (GAD). It is an antidepressant that belongs to a group of medicines known as selective serotonin reuptake inhibitors (SSRIs). \nDownload PDF: https://drive.google.com/drive/u/0/folders/1YZ1FVDazwwfYziFPaof3fw8AAmGLOkjr \nDownload Image: https://drive.google.com/drive/u/0/folders/1ARpKysnw1KaZ9eB3q7wtBVlzqddudV9F"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print("Client Sending \n Upload Escitalopram")
    upload_string = "Upload " + str(add_drug)
    s.sendall(bytes(upload_string, 'utf-8'))
    data = s.recv(1024)
    data = data.decode('utf-8')
    sentences = data.split("\n")
    print("Received\n")
    for sentence in sentences:
        print(sentence)
    print()


    print("Client Sending \n Download Escitalopram")
    s.sendall(b"Download Escitalopram")
    data = s.recv(1024)
    data = data.decode('utf-8')
    sentences = data.split("\n")
    print("Received\n")
    for sentence in sentences:
        print(sentence)
    print()