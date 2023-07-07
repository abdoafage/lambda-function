import requests

res = requests.post(
    "http://127.0.0.1:8000/functions/run/2843d737-98dc-41b7-9198-41c4711fb71d/",
    headers={
        "Authorization": "Token 55ef380b1afe64882b4cc750af2375998684d050",
        "Content-Type": "application/json",  # Set the appropriate content type for your request
    },
    json={"nums": [3, 4, 6, 1, 5, 7, 3]},
)

print(res.json())
