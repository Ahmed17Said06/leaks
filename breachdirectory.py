import requests
import json

def search_breach_directory(email):
    url = "https://breachdirectory.p.rapidapi.com/"
    querystring = {"func": "auto", "term": email}
    headers = {
        "x-rapidapi-host": "breachdirectory.p.rapidapi.com",
        "x-rapidapi-key": ""
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    email_to_search = "Megan_Arnold"
    print(f"Searching for breaches related to: {email_to_search}")
    results = search_breach_directory(email_to_search)

    if results:
        with open('breach_directory_results.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
        print("Results saved to breach_directory_results.json")
    else:
        print("No results found or an error occurred.")