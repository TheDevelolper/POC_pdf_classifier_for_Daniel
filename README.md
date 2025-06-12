

# Getting Started

> Note I developed this using Windows however the dependencies should be cross platform. Perhaps containers could be employed to eliminate any environment issues. 

> I added a script (`setup.ps1`) if using powershell for Windows. It will install all the pre-requites for you. I created it as a way to document what I'd done to make it all work, the steps are detailed below anyway:


## Install Poppler

For pdf classification we convert the PDF's to images as some PDF files may be scans without any text data. We can then use a simple sklean Support Vector Machine to classify the documents based on how they look.

Poppler is needed for the PDF to image conversion here are instructions on how to install Poppler

Windows

```powershell 
winget install poppler
```


Ubuntu 
``` bash
sudo apt update
sudo apt install poppler-utils
```

Fedora
``` bash
sudo dnf install poppler-utils
```

Arch Linux / Manjaro:
``` bash
sudo pacman -S poppler
```

### Verify Poppler Installation
Once your're done verfy the install with: 
``` bash
pdfinfo -v
```

## Adding Example Data

You can add data to the examples folder, subfolders are used as labels:
e.g. `examples/invoices/*.pdf` will all be labelled as invoices by convention.

## Install Python Packages

The requirements.txt file lists all of the python packages to be installed. You can install them with the following command: 

```
pip install -r requirements.txt
```

> Note This was a quick harness, I've not specified versions. I couldn't be bothered. 🤷🏽

## Running The Code
Once you've supplied sample data you're ready to run the thing like so:

```powershell
> python main.py
```

The application should then perform 4 steps:

1) Convert the PDF files into images saving them into the processed directory
2) Train the classifier on a subset of the documents (not all of them)
3) Perform predictions on all of the documents
4) Produce an accuracy report in the console.

