#!/usr/bin/python3
try:
    import requests
except ImportError :
    print("Request Module not Installed , please run 'pip install requests' ")
from random import choice
import argparse
import os
import time
fun = ['LetsGo',"Hurrayy","Try_Harder","Duh","/AdMIn$","Just_SuDO_it !","h4k3r","4N0NYM0US"]


# parser        
parser = argparse.ArgumentParser(description="Search For hidden Directories Easily.",epilog= "Example:---> dir.py -u http://examplesite.com/ -w /home/path/to/wordlist.txt --verbose")
# arguments
parser.add_argument("-u","--url",dest="url",type=str,help="Specify the Target url for Brute forcing .")
parser.add_argument("-w","--wordlist",dest="wordlist",type=str,help="Specify the path to the wordlist.")
parser.add_argument("-v","--verbose",dest="verb",action="store_true",help="Shows verbose output with Not found Pages Listed. " )
args = parser.parse_args()

verbose = ["True" if args.verb else "False"]     #  For showing verbose=TRUE/FALSE IN banner
banner ="""  
======Version 1.20=======
 +-+-+-+-+-+-+
 |D|i|r|.|p|y|
 +-+-+-+-+-+-+
  {0}
  +-------------------~~
  | URL : {1}      
  | WORDLIST : {2}     
  | VERBOSE : {3}      
  +-------------------~~
  
""".format(choice(fun),args.url,args.wordlist,verbose)

# Function
def real():
    r1 = requests.get(args.url)
    if r1.status_code == 200:
        print("\n[ INFO ] Checking if url is valid ...")
        time.sleep  (1.5)
        print("[ INFO ] {0} is VALID URL.(200)\n".format(args.url))
    if not args.wordlist :
            print( "[ ! ] Please specify the wordlist ( -w [PATH] )")
    elif args.wordlist:
        p = os.path.exists(args.wordlist)                    # Path validation
        if p == False: 
            print("\n[ ! ] The specified path doesn't exists .")
        else:     
            with open(args.wordlist,"r") as f: 
                lines = f.readlines()                        # Converting each line into item in list called 'lines'
                print("Trying ...\n")
            for i in lines:
                newurl = args.url + i                        # the specified url + the i in lines
                req = requests.get(newurl)                   # GET REQ
                if not args.verb:    #If -v is not called
                        if req.status_code in range(200,302):        # 200-301 = successful response
                            st = req.status_code             
                            print("[ + ] FOUND---",newurl,"(Status Code:{0})".format(st))
                elif args.verb :                             # if -v called by  user 
                    if req.status_code in range(200,302):
                        print("[ + ] FOUND---",newurl,"(Status Code:{0})".format(req.status_code))
                    elif req.status_code not in range(200,302):
                        print("[ - ] NOT Found---",newurl,"(Status Code:{0})".format(req.status_code))
           
                
start_time = time.time()     # Keeping track of start time . 

try:
    print(banner)                   
    real()  # / Calling the function /
    print("\n[ Finished in {0} seconds ]\n".format(time.time()- start_time)) # time = current time - start_time 
    print("=============================")
# Error Handling
except requests.exceptions.MissingSchema:            # If no http:// or forgot to call -w 
    print("""[!] Some Error Occured
         -- Did you forget http:// ?
         -- Did you specify the correct url ?
         -- Did you specify the Wordlist ?

         Type -h or --help to Learn more .
         """)
except requests.exceptions.ConnectionError or urllib3.exceptions.ProtocolError:  #if Wrong URL 
    print("""[!] The specified URL seems wrong,Try again.
                ---> Try adding  "/" at the End of URL? 
                ---> Is the protocol Correct ?
                ---> Does that Url even exist ? xD """)

except KeyboardInterrupt:                                                       
    print('[!] KeyboardInterrupt-->Reason : User Declined . ')       # interactive response to keyint


#----------------------- CODED BY: H4wK! ---------------------V-1.2-------------# 
#                 Github:https://github.com/H4wK-101/
