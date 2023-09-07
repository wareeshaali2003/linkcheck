from urllib.request import urlopen
from urllib.error import *

# List of URLs to check
urls = [
    "http://ebook.pldworld.com/_eBook/FPGA%EF%BC%8FHDL/-Eng-/The%20Complete%20Verilog%20Book%20(Vivek%20Sagdeo).pdf",
    "https://athena.ecs.csus.edu/~arad/csc205/intro_verilog_hdl.pdf",  # This URL should fail
    "https://ia800201.us.archive.org/30/items/springer_10.1007-978-1-4757-6682-0/10.1007-978-1-4757-6682-0.pdf",
]

# Lists to store working and non-working URLs
Poductive_URLS = []
non_Poductive_URLS = []

# Loop through the list of URLs
for url in urls:
    try:
        html = urlopen(url)
    except HTTPError as e:
        non_Poductive_URLS.append(url)
    except URLError as e:
        non_Poductive_URLS.append(url)
    else:
        Poductive_URLS.append(url)

# Print the lists of working and non-working URLs
print("working urls: ",Poductive_URLS )
print("not working urls: ",non_Poductive_URLS)
