import httpx


login_payload = {
    "email": "igor@example.com",
    "password": "07031964"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)

my_access_token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {my_access_token}"}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Status Code:", response.status_code)
print("Response Code:", response.json())

