import re
import csv

# To clean up the noise in the file
def cleanup(t):
    t=t.lower()
    t=re.sub(r"http\S+","",t)
    t=re.sub(r"[^a-zA-Z\s]","",t)
    t=re.sub(r"(.)\1{2,}",r"\1\1",t)
    t=re.sub(r"\s+"," ",t).strip()
    return t

# To count the words in text
def countwords(t):
    words=t.split()
    count={}
    for w in words:
        count[w]=count.get(w,0)+1
    
    return count

# To make the CSV file from two list first its heading and second is the data
def makecsv(filename,head,body):
    with open(filename,"w") as f:
        fi=csv.writer(f)
        fi.writerow(head)
        fi.writerows(body)

# Main code starts here
with open("Python/Practice/Hello.txt","r") as f:
    t=f.read()

t=cleanup(t)

count=countwords(t)

top=sorted(count.items(),key=lambda x:x[1],reverse=True)
top10=top[:10]

makecsv("Python/Practice/Final.csv",["Word","Count"],top10)
print("\nCSV file has been created\n")
