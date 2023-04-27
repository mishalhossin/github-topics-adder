# Topics Adder

This is a Python script that allows you to add random topics to a GitHub repository using the GitHub API.

## Installation

1. Clone this repository using : 
```
git clone https://github.com/mishalhossin/github-topics-adder.git
```
2. Change into the cloned directory using :
```
cd your_repository_name
```
3. Install the required dependencies using :
```
pip install os random requests
```

## Usage

1. Replace `your_username` and `your_repository_name` with your actual GitHub username and repository name, respectively in `topics_adder.py`
2. Set your GitHub access token as an environment variable named `ACCESS_TOKEN`.
3. Create a wordlist of topics in a file named `wordlist.txt`, with one topic per line.
4. Run the script using 
```
python topics_adder.py
```

The script will select (note 20 is the max topics for github) 20 random topics from your `wordlist.txt` file, and add them to your repository's topics using the GitHub API. The topics will be added every 20 seconds until the script is terminated.

## Wordlist Validator

The `wordlist_validator.py` script can be used to validate the contents of your `wordlist.txt` file. It will load the file, remove any special characters and spaces from each topic, and check if they are valid topics according to the GitHub API's naming conventions. It will then output the list of valid topics and overwrite your `wordlist.txt` file with only the valid topics.

To use the `wordlist_validator.py` script, simply run 
```
python wordlist_validator.py
```
The script will output the list of valid topics to the console and overwrite your `wordlist.txt` file with only the valid topics.
