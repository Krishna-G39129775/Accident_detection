import socket
import pandas as pd
from _thread import *
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5050
ThreadCount = 0
try:
    S.bind((socket.gethostname(), port))
except socket.error as e:
    print(str(e))
print('Waiting for a Connection..')
S.listen(10)

def threaded_client(client):
    client.send(str.encode('Welcome to the Server\n'))
    client.send(str.encode('We got an accident detected at our area\n go there immediately'))
    s = client.recv(1024).decode("utf-8")
    print(s)
    client.send(bytes("Select you option\nI.Insertion\nV-View\nD-Divide into different files\n", "utf-8"))
    ch = client.recv(10).decode("utf-8")
    if ch == 'I':
        n = client.recv(10).decode("utf-8")
        for i in range(1, int(n) + 1):
            client.send(bytes("Enter Date_Admitted", "utf-8"))
            Date_Admitted = client.recv(1000).decode("utf-8")
            client.send(bytes("Enter Time_Admitted", "utf-8"))
            Time_Admitted = client.recv(1000).decode("utf-8")
            client.send(bytes("Enter Patient_ID :", "utf-8"))
            client.send(bytes("Enter Patient_Name", "utf-8"))
            Patient_Name = client.recv(1000).decode("utf-8")
            Patient_ID = client.recv(1000).decode("utf-8")
            client.send(bytes("Enter Age :", "utf-8"))
            Age = client.recv(1000).decode("utf-8")
            client.send(bytes("Enter Gender :", "utf-8"))
            Gender = client.recv(1000).decode("utf-8")
            client.send(bytes("Enter yes if we Saved the patient or not :", "utf-8"))
            Saved = client.recv(1000).decode("utf-8")
            list1 = [[Date_Admitted,Time_Admitted,Patient_Name,Patient_ID,Age,Gender,Saved]]
            df2 = pd.DataFrame(list1,columns=['Date_Admitted','Time_Admitted','Patient_Name','Patient_ID','Age','Gender','Saved'])
            df2.to_csv(r'/Users/saikrishnapaila/Desktop/Hospital_dept/Patient.csv', mode='a', index=False, header=False)

    elif ch == 'V':
        client.send(bytes("/Users/saikrishnapaila/Desktop/Hospital_dept/Patient.csv", "utf-8"))



while True:
    client, addr = S.accept()
    print(f"Connection established to {addr} ")
    start_new_thread(threaded_client, (client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))