# python_playground

## Description
In this I am going to start some python projects with the goal of working on some smaller AI works.

Thanks given to **ChatGPT** and **Artificial Intelligence for Developers (in easysteps)*** book found on [https://www.ineasysteps.com] or a visit local library.

So more to come.

# Preparing

## Install Python
[Python Install](https://www.python.org/downloads)

Be sure to check the **Add python.exe to the PATH** box. Then choose **Custom Installation.** Then **Next**. And another **Next** to **Finish**.

## Installing PIP
<!-- CTRL+E to get the special single quote -->
`python -m ensurepip --upgrade`
or
`python.exe -m pip install --upgrade pip`

## Installing pygame
Pygame allows for graphics to be created.
`pip install pygame`

## To Install Tensorflow you need 3.11.9 version
Python 3.13 will not work with Tensorflow at this time.

### Set up Virtual Environment
I ran into issue with switching between 3.11 and 3.13 due to permissioning issues with running the python scripts.

So I went with creating a virtual environment for 3.11 using the following:
`py -3.11 -m venv venv311`

When I want to run a script inside that environment I just need to enter in the following:
`venv311\Scripts\activate`

Then I can run the script like normal. Note that the virtual environment is a path to a activate bash script so take note of the virtual environments full path for future reference.

## Install Tensor Flow
Need Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, 2019, and 2022.
https://learn.microsof.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170

Be sure to run this in the virtual environment.

`pip install tensorflow`

`pip install tensorflow_datasets`

`pip install matplotlib`

# Python Scripts

## Eliza.py
This is a simple deterministic script that will similar to a therapist will use the information you input to ask a deeper question related to the words used in the input provided. A generic feedback loop.

`py Eliza.py`

## Dolittle.py
This is a manual learning script which will ask a question in attempt to identify the Animal you are thinking of. If it doesn't answer correctly it will ask for the Animal and a question that is unique to that Animal.
It stores the questions and answers which it will use in the future question. This script will identify the best question to ask that will have the greatest chance at slimming the universe until it identifies the Animal.
As this build over time this is a very time consumming process. But shows an option of learning over time rather than relying on a Data Lake to be used.

`py Dolittle.py`

## pdf_keyword_search.py
Ability to provide a list of words to be identified within a folder holding PDF files. It will search each PDF for the word or words and create a CSV file with the results of the word used and which PDF file (by name) has it.
This one was personally created and not from the text book.

`py pdf_keyword_search.py`

### Required installs to run the program
`pip install pdfplumber`

`pip install pdfplumber rapidfuzz`

## FlatworldGame
This is a visual version that builds off each other. See ReadMe within that folder for more information.

## Image Reader
mnist.py create a model that identifies varios images with written numbers.
SpitChar.py will split each number from an image that it recognizes as a number.
ocr.py will take the split images of a single number and extract the correct number which it will then recreate the numbers in the same order as original image.

Makes use of Image folder with Input holding the original image file (used a JPG) and the Output will be where SplitChar will establish in order each number found as it's own image.

### Notes
Use a thicker pen such as a marker as thin numbers are hard for the reader to identify. Even after this my written 8 returned as a 5 but all the other numbers were correctly identified and repeated.
Check out the Image folders to see the example input and output.

# Other Installs
To allow for speeding up the neural networks training process.

## Install WSL2
https://learn.microsoft.com/en-us/windows/wsl/install

> [!IMPORTANT]
> **To launch Ubuntu enter `wsl.exe -d Ubuntu`.**

Regular Update and upgrade packages required. So make the following a habit:
`sudo apt update && sudo apt upgrade`
https://learn.microsoft.com/en-us/windows/wsl/setup/environment

Using **Windows Terminal** you can enter `Ctrl+Shift+P` to get the **Command Palette**.
https://learn.microsoft.com/en-us/windows/terminal/install#invoke-the-command-palette

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

**Linux and Bash**
https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

> [!CAUTION]
> Tensor Flow requires Python 3.8, 3.9, 3.10, 3.11. Which means Python 3.12+ is not yet supported. Version of Python as of this writing is 3.13.3.
> Using WSL2 you can install Python 3.11 and pip (using `pyenv`).

## Install pyenv with Python version 3.11.9
1. From CMD prompt enter in `wsl.exe -d Ubuntu`.
2. Enter `sudo apt update`.
3. Enter ```sudo apt install -y build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev git```
4. Enter `curl https://pyenv.run | bash`
5. Then Enter in the following:
   ```
   # Add pyenv to shell
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   exec "$SHELL"
   ```
6. Enter `pyenv install 3.11.9`.
7. Enter `pyenv global 3.11.9`.


## Install CuDNN and CUDA toolkit
https://docs.nvidia.com/deeplearning/cudnn/installation/linux.html

> [!WARNING]
> If above doesn't work then you should follow steps [Install pyenv with Python version 3.11.9](#Install-pyenv-with-Python-version-3.11.9).
> Used **ChatGPT** to assist in resolution.
