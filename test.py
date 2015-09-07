import os, time
import subprocess
import glob
import operator
from subprocess import STDOUT,PIPE
import re

email_arr = []
files_arr = []
stdin = ''
stdout = ''
stderr = ''
root_path = "F:\DigitalWallet"
extension = '.java'
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
def NewestDir(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)

    lister = sorted(dirs.iteritems(), key=operator.itemgetter(1))
    print glob.glob(1)
    return lister[-1][0]

def return_emails(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if files != []:
            files_arr.append(files)
            email_arr.append((re.search(r'[\w\.-]+@[\w\.-]+', root)).group(0))
    print email_arr

def return_files(email):
    for root, dirs, files in os.walk(root_path+"\\"+email+"\\"+NewestDir(root_path+"\\"+email), topdown=False): 
        for name in files:
            if name.lower().endswith(extension):
                print root+"\\"+name

return_emails(root_path)
return_files("ananyaannu22@gmail.com")
print "Done"
    
