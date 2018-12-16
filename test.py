# import os
# os.system('java -jar SearchModel.jar "बच्चन जी की गिनती हिन्दी के सर्वाधिक लोकप्रिय कवियों में होती है"')
import subprocess
output = subprocess.check_output('java -jar SearchModel.jar "बच्चन जी की गिनती हिन्दी के सर्वाधिक लोकप्रिय कवियों में होती है"', shell=True)
print("out = ",output.decode("utf-8"))