import os
import subprocess
from subprocess import STDOUT,PIPE
import re

email_arr = []
files_arr = []
file_path = ""
directory_list = list()
stdin = ''
stdout = ''
stderr = ''
out = open('output.txt', 'w')
def execute_java(roots):
    cmd = 'java -cp '+roots+' DigitalWalletHidden'
    proc = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    out.write("Output is: "+stdout+"\n\n")
        
def compile_java(roots):
    cmd = 'javac '+roots+'\*.java'
    proc = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    if stdout == '' or stdout.find("Xlint") != -1 and stdout.find("error") == -1:
        out.write("Successfully Compiled\n\n")
        execute_java(root)
    else:
        out.write("Compilation Errors: \n\n"+stdout+"\n\n")
################################################################################
def return_emails(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if files != []:
            files_arr.append(files)
            email_arr.append((re.search(r'[\w\.-]+@[\w\.-]+', root)).group(0))
    return email_arr
print return_emails("F:\DigitalWallet")

def return_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if files != []:
            files_arr.append(files)
    return files_arr
print return_files("F:\DigitalWallet")
print "Done"
    
