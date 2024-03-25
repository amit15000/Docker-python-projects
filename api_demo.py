import requests

def fetch_random_fact():
    api_url = 'https://meowfacts.herokuapp.com/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        fact = response.json()
        return fact['data'][0]  # Extract the first fact from the response
    except requests.exceptions.RequestException as e:
        print("Error Occurred:", e)

def main():
    count = 1
    for _ in range(count):
        fact = fetch_random_fact()
        print(fact)

# def mainKaBhai():
#     print("Sumit")

if __name__ == "__main__":
    main()
    # mainKaBhai()
