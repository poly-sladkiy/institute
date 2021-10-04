from subprocess import call
import os

fp = open("result.txt", "w")
res = call(('dir', r'c:\Windows\System32'), shell=True, stdout=fp)
fp.close()
print(res)