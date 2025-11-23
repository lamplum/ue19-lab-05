import requests

def get_random_joke():
    api_url = "https://v2.jokeapi.dev/joke/Any?type=single"
    
    print("Interrogation de JokesAPI...")
    
    try:
        response = requests.get(api_url, timeout=10)
        
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("error"):
            print("Erreur de l'API :", data.get("message", "Erreur inconnue"))
            return
            
        joke = data.get("joke")
        if joke:
            print(">>>", joke)
        else:
            print("Le format de la blague n'est pas le format 'single' attendu.")
            
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête API : {e}")

if __name__ == "__main__":
    get_random_joke()
