# GPTSplitter
GPTSplitter is a Python script that splits text input into multiple parts with a maximum length of 500 characters, to work around the limitation of OpenAI's GPT language model, which can only accept up to 2048 tokens at a time.

## Installation
- Clone or download the GPTSplitter repository.
- Install Python 3.6 or later.
## Usage
1) Prepare your text input by creating a file with the text you want to process, for example input.txt.
2) Run the script using the following command: python GPTSplitter.py
3) The script will prompt you to enter the name of the input file. Enter the name of the file you prepared in step 1.
4) The script will split the text into multiple parts with a maximum length of 500 characters and display them on the console.
5) You can then use the text parts as input for the OpenAI GPT language model.
## Example
Suppose you have a file input.txt with the following text:
``` bash 
This is an example text that is longer than 500 characters. It needs to be split into multiple parts to work with OpenAI's GPT language model, which has a maximum input length of 2048 tokens. GPTSplitter is a Python script that can split the text into parts with a maximum length of 500 characters, so you can use it with the GPT language model.
```
To split this text using GPTSplitter, run the following command:

``` bash 
python GPTSplitter.py
```
When prompted for the name of the input file, enter input.txt.

The script will output the following:
``` bash 
hey gpt i need ur help i send u msg in parts all parts is 500 character len of parts is 2 and update me in the message how much parts remain:
____________________________________________________________________
this part 1-remain parts 1
This is an example text that is longer than 500 characters. It needs to be split into multiple parts to work with OpenAI's GPT language model, which has a maximum input length of 2048 tokens. GPTSplitter is a Python script that can split the text into parts with a maximum length of 500 characters, so you can use it with the GPT language model.

this part 2-remain parts 0
, you can then use it as input for the GPT language model.
```
You can then use the text parts as input for the OpenAI GPT language model.
