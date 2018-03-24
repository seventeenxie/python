import json,os
a={'a':111,"b":['fff','ffff']}


f=open(os.getcwd()+'\\test.txt','w')
f.write(json.dumps(a))
f.close()