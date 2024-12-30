import requests
import time
import json

# Define the API endpoint and API key
API_ENDPOINT = "https://leak-lookup.com/api/search"
API_KEY = ""

# Available query types
AVAILABLE_TYPES = [
    "email_address",
    "username",
    "ipaddress",
    "phone",
    "domain",
    "password",
    "fullname",
]

def query_leaks_lookup_all_types(query_value):
    combined_results = {}

    for query_type in AVAILABLE_TYPES:
        print(f"\nQuerying for type: {query_type}")
        
        # Prepare payload as application/x-www-form-urlencoded
        payload = {
            "key": API_KEY,
            "type": query_type,
            "query": query_value,
        }
        print(f"Payload being sent: {payload}")

        try:
            # Send POST request with payload as form data
            response = requests.post(API_ENDPOINT, data=payload)

            # Debugging: Print full response
            print(f"Response for type '{query_type}': {response.text}")

            # Check for valid response
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()

            # Check if API returned data
            if data.get("error") == "false":
                combined_results[query_type] = data.get("message", {})
            else:
                print(f"API returned an error for type '{query_type}': {data.get('message')}")
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Leaks-lookup API for type '{query_type}': {e}")


        time.sleep(3)  # Adjust delay as needed to compat rate-limiting

    return combined_results

if __name__ == "__main__":
    # Value to search for
    query_value = "susan james"
    print(f"Querying Leaks-lookup API for all available types with value: {query_value}")
    results = query_leaks_lookup_all_types(query_value)

    # Save results to a JSON file
    with open('leaks_lookup_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Display results
    if results:
        print("\nResults:")
        for query_type, breaches in results.items():
            print(f"\nQuery Type: {query_type}")
            for breach, details in breaches.items():
                print(f"  Breach: {breach}")
                if details:
                    for entry in details:
                        print(f"    Entry: {entry}")
                else:
                    print("    No data found.")
    else:
        print("No results or an error occurred.")
