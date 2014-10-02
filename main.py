import argparse
import re
import os

def Redbold(output):
    os.system("tput bold")
    os.system("tput setaf 1")
    print(output)
    os.system("tput sgr 0")
    
def Bold(output):
    os.system("tput bold")
    print(output)
    os.system("tput sgr 0")

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Youtube's playlist's url")
args = parser.parse_args()

Redbold("\nDownloading source code from url...")
Bold("Source code downloaded\nDownloading files...")
os.system("wget -o .wgetstdout \"" + args.url + "\" -O .sourceCode")
os.system("rm .wgetstdout")

sourceCode = open(".sourceCode", "r")
for line in re.findall("<ol class=\"playlist-videos-list .*</ol>", sourceCode.read(), re.DOTALL):
    for link in re.findall('/watch?.{14}', line):
        Redbold("\nDownloading " + link + " ...")
        os.system("youtube-dl -i -x -o \"%(title)s.%(ext)s\" http://www.youtube.com" + link)

os.system("rm .sourceCode")