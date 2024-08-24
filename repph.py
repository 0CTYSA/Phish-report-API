import requests
import json
import os

# Function to obtain abuse contact information for multiple URLs


def get_abuse_contact_info_bulk(api_key, urls):
    contact_info_results = {}
    for url in urls:
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.get(
            f'https://phish.report/api/v0/hosting', params={'url': url}, headers=headers)
        if response.ok:
            contact_info_results[url] = response.json()
        else:
            contact_info_results[url] = {'error': response.text}
    return contact_info_results

# Function to initiate the downloading of multiple URLs


def start_takedown_bulk(api_key, urls):
    takedown_responses = {}
    for url in urls:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            'url': url,
            'ignore_duplicates': True
        }
        response = requests.post(
            f'https://phish.report/api/v0/cases', json=payload, headers=headers)
        if response.ok:
            takedown_responses[url] = response.json()
        else:
            takedown_responses[url] = {'error': response.text}
    return takedown_responses

# Function to save the results in JSON files in a 'results' folder


def save_results_to_files(results, folder='results'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for url, data in results.items():
        # Extract the domain from the URL
        domain = url.split('//')[-1].split('/')[0]
        file_path = os.path.join(folder, f"{domain}.json")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


# Prompting the user to enter the URLs through the terminal
urls_to_check = []
print("Please enter the URLs you wish to verify (maximum 10). Type 'done' when you are done:")
while len(urls_to_check) < 10:
    url_input = input("Enter URL or 'done' to finish: ")
    if url_input.lower() == 'done':
        break
    urls_to_check.append(url_input)

# Assuming that we already have the API key
api_key = 'your_real_api_key_here'  # Replace this with the actual API key

# Obtain contact information for mass abuse and save results
contact_info_bulk = get_abuse_contact_info_bulk(api_key, urls_to_check)
save_results_to_files(contact_info_bulk)

# Initiate deregistration process for multiple malicious URLs and save results
takedown_responses_bulk = start_takedown_bulk(api_key, urls_to_check)
save_results_to_files(takedown_responses_bulk)
