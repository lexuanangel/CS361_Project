import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
drugs = {"Omeprazole": "Omeprazole is used to treat certain conditions where there is too much acid in the stomach. \nDownload PDF: https://drive.google.com/drive/u/0/folders/1YZ1FVDazwwfYziFPaof3fw8AAmGLOkjr \nDownload Image: https://drive.google.com/drive/u/0/folders/1ARpKysnw1KaZ9eB3q7wtBVlzqddudV9F",
         "Albuterol": "used to prevent and treat wheezing, difficulty breathing, chest tightness, and coughing caused by lung diseases such as asthma and chronic obstructive pulmonary disease (COPD; a group of diseases that affect the lungs and airways). \nDownload PDF: https://drive.google.com/drive/u/0/folders/1YZ1FVDazwwfYziFPaof3fw8AAmGLOkjr \nDownload Image: https://drive.google.com/drive/u/0/folders/1ARpKysnw1KaZ9eB3q7wtBVlzqddudV9F"
        }

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            name = data.decode('utf-8')
            print(name, "Upload" in name)
            if ("Upload" in name):
                name = name[name.index("{"):]
                dic = eval(name)
                for key, val in dic.items():
                    drugs[key] = val
                print("Added the drugs in dictionary")
                print("Drugs contain ", drugs.keys())
                string = "Drug " + str(dic.keys()) + " Uploaded. The current drug list contains " + str(drugs.keys())
                conn.sendall(bytes(string, 'utf-8'))
            elif("Download" in name):
                name = name[name.index(" ") + 1 : ]
                # print(name, name in drugs)
                if name in drugs:
                    conn.sendall(bytes(drugs[name], 'utf-8'))
                else:
                    conn.sendall(b"Drug is not found")
            # print("Received ", data)
