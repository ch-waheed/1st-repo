import requests

def get_linked_data(product_code):
    # Make a request to the linked API
    url = f'https://world.openfoodfacts.org/api/v0/product/{product_code}.json'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Access the data from the response
        data = response.json()

        # Process the data
        for api_name in data.keys():
            print(data[api_name])
    else:
        print('Failed to fetch linked data.')

# Get user input
product_code = input("Enter the product code: ")

# Call the function to retrieve and process the linked data
get_linked_data(product_code)
