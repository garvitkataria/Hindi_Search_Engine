import os
s = "रबीन्द्रनाथ टैगोर".encode("utf-8")
s1="rabindranath"
op = os.system('java -jar SearchModel.jar '+s1)
print(op)
