# URL Checker

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

This Python script checks the availability of a list of URLs and categorizes them as "working" or "not working."

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/url-checker.git
   ```

2. Navigate to the project directory:

   ```shell
   cd url-checker
   ```

3. Run the script:

   ```shell
   python url_checker.py
   ```

## Usage

Modify the `urls` list in the `url_checker.py` script to include the URLs you want to check.

```python
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
print("working urls: ", Poductive_URLS)
print("not working urls: ", non_Poductive_URLS)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `"yourusername/url-checker"` in the installation instructions with the actual URL of your GitHub repository.

Don't forget to add a screenshot of your script's output by uploading the image as "script_output.png" into a "screenshots" folder in your repository.
