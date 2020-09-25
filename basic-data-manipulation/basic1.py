import pandas
import os
import time

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data)
    else:
        print("File does not exist")
        
    print("Waiting")
    time.sleep(10)
