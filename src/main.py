import download as dl

#
# Downloading the required files as per the project's readme
url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/"
filename1 = "homicidios"
filename2 = "lesiones"

dl.getData(url + filename1, "homicides", ".xlsx")
dl.getData(url + filename2, "injuries", ".xlsx")


#
# Downloading additional files to aid the data analysis
f = open("Project\data\\raw\\download_links.csv", "r")
linkList = dl.getLinks(f)
f.close

for url, filename, ext in linkList:
    dl.getData(url, filename, ext)

#
# Processing the main required files
import process as pr

pr.process_homicides_facts()
pr.process_homicides_victims()
pr.process_injuries_facts()
pr.process_injuries_victims()