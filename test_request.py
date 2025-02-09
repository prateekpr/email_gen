import requests

url = "http://127.0.0.1:8000/generate-email/"
payload = {
    "name": "John Doe",
    "experience": 5,
    "skills": "Python, Automation Testing",
    "job_description": "Looking for an SDET with experience in Playwright and API testing."
}
response = requests.post(url, json=payload)
print(response.json())
