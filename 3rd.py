import requests

def get_linked_data():
    # Make a request to the linked API
    response = requests.get('https://world.openfoodfacts.org/api/v0/product/737628064502.json')

    # Check if the request was successful
    if response.status_code == 200:
        # Access the data from the response
        data = response.json()

        # Process the data
        for api_name in data.keys():
            print(api_name)
    else:
        print('Failed to fetch linked data.')

# Call the function to retrieve and process the linked data
get_linked_data()

# Get user input
question = input("Enter your question: " )

# Process the user's question
# Add your code here to handle the user's question and generate an appropriate response
if "bank holidays" in question.product():
    print("Yes, I can provide information about bank holidays. What specific information are you looking for?")
else:
    print("I'm sorry, but I don't have information about that topic at the moment.")