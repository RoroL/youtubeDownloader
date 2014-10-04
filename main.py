import argparse
import re
import os
import time

def Redbold(output):
    os.system("tput bold")
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
    
def Bold(output):
    os.system("tput bold")
    print(output)
    os.system("tput sgr 0")
    
start = time.time()
countFiles = 0

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Youtube's playlist's url")
parser.add_argument("-f", "--file", help="Url listing file")
args = parser.parse_args()

if args.url:
    
    Redbold("\nDownloading source code from url...")
    os.system("wget -o .wgetstdout \"" + args.url + "\" -O .sourceCode")
    os.system("rm .wgetstdout")
    Bold("Source code downloaded\nDownloading files...")
    
    sourceCode = open(".sourceCode", "r")
    for line in re.findall("<ol class=\"playlist-videos-list .*</ol>", sourceCode.read(), re.DOTALL):
        for link in re.findall('/watch?.{14}', line):
            countFiles += 1
            Redbold("\n" + str(countFiles) + "/" + str(len(re.findall('/watch?.{14}', line))) + ": Downloading " + link + " ...")
            os.system("youtube-dl -i -x -o \"%(title)s.%(ext)s\" http://www.youtube.com" + link)

if args.file:    
    Redbold("\nListing urls from file...")
    os.system("cat ./" + args.file + " > .sourceCode")
    Bold("Urls loaded\nDownloading files...")
    
    os.system("cat .sourceCode | wc -l > .countFiles")
    
    sourceCode = open(".sourceCode", "r")
    for link in sourceCode:
        link = link.split(".com")[1][:-1]
        
        countFiles += 1
        Redbold("\n" + str(countFiles) + "/" + str(open(".countFiles", "r").readline()[:-1]) + ": Downloading " + link + " ...")
        os.system("youtube-dl -i -x -o \"%(title)s.%(ext)s\" http://www.youtube.com" + link)
    os.system("rm .countFiles")

os.system("rm .sourceCode")

end = time.time()
time = end-start

Bold("\n... Infos ...")
Bold("- Processing time : " + str(time))