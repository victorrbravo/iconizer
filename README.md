Author: Victor Bravo victor.bravo@wizeline.com
# Iconizer

## Description

**Description:** Transform a photo into an icon using OpenAI. It also generates a description for the input image

Dependencies: pip install openai, pip install pillow, pip install requests


Notes: This script is using the OpenAI API, you need to have an account and an API key.
To achieve accurate icon generation, we utilize the dall-e-3 model. 
Please note that this model may not be available with the free plan

## How to use

You should define an Environment Variable before executing the script.
You can use this command:

export OPENAI_API_KEY=<OPENAI_API_KEY> 


usage: ./convert.py [-h] -f FILENAME -o OUTPUT

or python convert.py [-h] -f FILENAME -o OUTPUT

options:
  -h, --help            show this help message and exit

  -f FILENAME, --filename FILENAME. Enter the file path for the JPEG image.

  -o OUTPUT, --output OUTPUT. Specify the file path for the generated icon.


## Acknowledgments

This project was inspired by or based on the work done in the following GitHub repository:
- [chatGPT-sprint-1023](https://github.com/wizelineacademy/chatGPT-sprint-1023)
