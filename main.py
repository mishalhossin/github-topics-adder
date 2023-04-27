import requests
import os
import time
import random

# Replace your GitHub access token in env
access_token = os.environ['ACCESS_TOKEN']
# Replace with your GitHub username and repository name
username = 'your_username'
repo_name = 'your_repository_name'

# Read topics from wordlist.txt
with open('wordlist.txt', 'r') as file:
    all_topics = [line.strip() for line in file.readlines()]

# Set the API endpoint
api_url = f'https://api.github.com/repos/{username}/{repo_name}/topics'

# Set the headers for the API request
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github+json'
}

while True:
    # Select 20 random topics
    topics = random.sample(all_topics, 20)

    # Print the current set of topics
    print('Adding topics:', ', '.join(topics))

    # Make the API request to update the repository topics
    response = requests.put(api_url, json={'names': topics}, headers=headers)

    # Check the response
    if response.status_code == 200:
        print('Topics successfully added to the repository')
    else:
        print('Error:', response.status_code, response.text)

    # Wait for 20 seconds before updating the topics again
    time.sleep(20)
