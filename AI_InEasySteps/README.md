# python_playground

## Description
Thanks given to **Artificial Intelligence for Developers (in easysteps)*** book found on [https://www.ineasysteps.com] or a visit local library. Note that I did require **ChatGPT** assistance as some of the projects were not running appropriately without some tweaks from the original.

So more to come.

# Preparing
Go to main Python_Arena ReadMe file for steps on how to instill the information required to run the projects.

# Python Scripts

## Eliza.py
This is a simple deterministic script that will similar to a therapist will use the information you input to ask a deeper question related to the words used in the input provided. A generic feedback loop.

`py Eliza.py`

## Dolittle.py
This is a manual learning script which will ask a question in attempt to identify the Animal you are thinking of. If it doesn't answer correctly it will ask for the Animal and a question that is unique to that Animal.
It stores the questions and answers which it will use in the future question. This script will identify the best question to ask that will have the greatest chance at slimming the universe until it identifies the Animal.
As this build over time this is a very time consumming process. But shows an option of learning over time rather than relying on a Data Lake to be used.

`py Dolittle.py`

### Required installs to run the program
`pip install pdfplumber`

`pip install pdfplumber rapidfuzz`

## FlatworldGame
This is a visual version that builds off each other. See ReadMe within that folder for more information.

## Image Reader
mnist.py create a model that identifies varios images with written numbers.
SpitChar.py will split each number from an image that it recognizes as a number.
ocr.py will take the split images of a single number and extract the correct number which it will then recreate the numbers in the same order as original image. Note that this will add the numbers 
from prior runs to get a new grand total.

Makes use of Image folder with Input holding the original image file (used a JPG) and the Output will be where SplitChar will establish in order each number found as it's own image.

![new](https://github.com/user-attachments/assets/9dff49b8-cac7-438a-83ba-695c8456734a)


### Output for Input image from ocr.py
```
new = 7261945350
Total: 7261945350
```

### Notes
Use a thicker pen such as a marker as thin numbers are hard for the reader to identify. Even after this my written 8 returned as a 5 but all the other numbers were correctly identified and repeated.
Check out the Image folders to see the example input and output.