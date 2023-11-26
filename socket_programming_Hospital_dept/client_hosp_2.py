import socket
import pandas as pd

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5050
print('Waiting for connection')
try:
    c.connect((socket.gethostname(), port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024).decode('utf-8')
print(Response)
cl = c.recv(1000).decode("utf-8")
print(cl)
c.send(bytes("we are going there immediately".encode("utf-8")))
cl = input(c.recv(1000).decode("utf-8"))
c.send(cl.encode("utf-8"))
if cl == 'I':
    n = int(input("Enter number of rows to be inserted : "))
    c.send(str(n).encode("utf-8"))
    for i in range(1, n + 1):
        Date_Admitted = input(c.recv(1000).decode("utf-8"))
        c.send(Date_Admitted.encode("utf-8"))
        Time_Admitted = input(c.recv(1000).decode("utf-8"))
        c.send(Time_Admitted.encode("utf-8"))
        Patient_Name = input(c.recv(1000).decode("utf-8"))
        c.send(Patient_Name.encode("utf-8"))
        Patient_ID = input(c.recv(1000).decode("utf-8"))
        c.send(Patient_ID.encode("utf-8"))
        Age = input(c.recv(1000).decode("utf-8"))
        c.send(Age.encode("utf-8"))
        Gender = input(c.recv(1000).decode("utf-8"))
        c.send(Gender.encode("utf-8"))
        Saved = input(c.recv(1000).decode("utf-8"))
        c.send(Saved.encode("utf-8"))

elif cl == 'V':
    print(pd.read_csv(c.recv(5000).decode("utf-8")))

elif cl == 'D':
    df = pd.read_csv(r'C:/Users/surya/Desktop/CN_Casestudy/Patient.csv')
    pat1 = df[df['Gender'] == 'Male']
    pat1.to_csv(r'C:/Users/surya/Desktop/CN_Casestudy/Male_Patient.csv', index=False)
    print(pd.read_csv(r'C:/Users/surya/Desktop/CN_Casestudy/Male_Patient.csv'))
    pat2 = df[df['Gender'] == 'Female']
    pat2.to_csv(r'C:/Users/surya/Desktop/CN_Casestudy/Female_Patient.csv', index=False)
    print(pd.read_csv(r'C:/Users/surya/Desktop/CN_Casestudy/Female_Patient.csv'))





c.close()