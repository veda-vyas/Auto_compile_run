import os, time
import subprocess
import glob
import operator
from subprocess import STDOUT,PIPE
import re
import difflib
import filecmp
from Levenshtein import distance

email_arr = []
#stdin = ''
#stdout = ''
#stderr = 0''
root_path = "F:\DigitalWallet"
filename = "DigitalWallet.java"
#out = open('output.txt', 'w')
#def execute_java(roots):
    #cmd = 'java -cp '+roots+' DigitalWalletHidden'
   # proc = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
  #  stdout,stderr = proc.communicate(stdin)
 #   out.write("Output is: "+stdout+"\n\n")
        
#def compile_java(roots):
    #cmd = 'javac '+roots+'\*.java'
    #proc = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    #stdout,stderr = proc.communicate(stdin)
    #if stdout == '' or stdout.find("Xlint") != -1 and stdout.find("error") == -1:
      #  out.write("Successfully Compiled\n\n")
     #   execute_java(root)
    #else:
        #out.write("Compilation Errors: \n\n"+stdout+"\n\n")
################################################################################
def NewestDir(directory):
    os.chdir(directory)
    dirs = {}
    for dir in glob.glob('*'):
        if os.path.isdir(dir):
            dirs[dir] = os.path.getctime(dir)
    return sorted(dirs.iteritems(), key=operator.itemgetter(1))[-1][0]

def return_emails(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if files != [] and (re.search(r'[\w\.-]+@[\w\.-]+', root)).group(0) not in email_arr:
            email_arr.append((re.search(r'[\w\.-]+@[\w\.-]+', root)).group(0))
    #print email_arr

def return_files(email,extension):
    for root, dirs, files in os.walk(root_path+"\\"+email+"\\"+NewestDir(root_path+"\\"+email), topdown=False): 
        for name in files:
            if name.endswith(extension):
                return root+"\\"+name
    return "Nofile"

def file_similarity(path1, path2):
    with open(path1,'rb') as f1:
        with open(path2,'rb') as f2:
            seq = difflib.SequenceMatcher(None, f1.read(),f2.read())
            d = seq.ratio()*100
            return d

def lev_similarity(path1, path2):
    with open(path1,'rb') as f1:
        with open(path2,'rb') as f2:
            return int(distance((f1.read()).strip(' \t\n\r'),(f2.read()).strip(' \t\n\r'))/100)

return_emails(root_path)
count = 0
sim_arr = []
stor_arr = []
out = open(str(filename[:-5])+'.txt','w')
out.write("Email\tComparing with\tRatio\tLevenshtein Distance\n")
for email in email_arr:
    path1 = return_files(email,filename)
    for to_compare_email in email_arr:
        path2 = return_files(to_compare_email,filename)
        if email != to_compare_email:
            if path1 != "Nofile" and path2 != "Nofile":
                out.write(str(email) +'\t'+ str(to_compare_email) +'\t'+ str(file_similarity(path1,path2)) + '\t' +str(lev_similarity(path1,path2)))
                out.write('\n')
            else:
                out.write(str(email) +'\t'+ str(to_compare_email) +'\tNo File' + '\t\n')
    print email
print "Done"
