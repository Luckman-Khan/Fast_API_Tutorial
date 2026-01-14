import json
import urllib.request
import urllib.parse
import sys

BASE_URL = "http://127.0.0.1:8002"

def create_user(name, email, password):
    url = f"{BASE_URL}/user/"
    data = {
        "name": name,
        "email": email,
        "password": password
    }
    encoded_data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/json'}, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Create User Status: {response.status}")
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Create User Failed: {e.code} - {e.read().decode()}")
        return None
    except Exception as e:
        print(f"Create User Error: {e}")
        return None

def login(email, password):
    url = f"{BASE_URL}/login"
    # OAuth2PasswordRequestForm expects form data, not JSON
    data = {
        "username": email,
        "password": password
    }
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/x-www-form-urlencoded'}, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Login Status: {response.status}")
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Login Failed: {e.code} - {e.read().decode()}")
        return None
    except Exception as e:
        print(f"Login Error: {e}")
        return None

def main():
    email = "testverif@example.com"
    password = "secretpassword"
    
    print("--- 1. Creating User ---")
    # Try to create user (might already exist)
    user = create_user("Test Verif", email, password)
    
    print("\n--- 2. Logging In ---")
    token_resp = login(email, password)
    
    if token_resp and "access_token" in token_resp:
        print("\nSUCCESS: Login successful, token received.")
        print(f"Token Type: {token_resp.get('token_type')}")
    else:
        print("\nFAILURE: Could not log in.")
        sys.exit(1)

if __name__ == "__main__":
    main()
