import download as dl
import process as pr

#
# Downloading the required files as per the project's readme
url = "https://raw.githubusercontent.com/soyHenry/PI_DA/Full_Time/"
filename = "AccidentesAviones"

dl.getData(url, filename, ".csv")


""" #
# Downloading additional files to aid the data analysis
f = open("Project\data\\raw\\download_links.csv", "r")
linkList = dl.getLinks(f)
f.close

for url, filename, ext in linkList:
    dl.getData(url, filename, ext)

#
# Processing the main required files """

pr.process_accidents()