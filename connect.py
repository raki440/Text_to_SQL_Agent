import requests
import os
API_URL = 'https://api.openai.com/v1/dashboard/billing/credit_grants'
# API_KEY = os.getenv('OPEN_AI_KEY')
API_KEY = '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'

headers = {
    "Authorization": f"Bearer {API_KEY}",
}

def test_usage(url: str):
    resp = requests.get(url=API_URL, headers=headers)
    print(resp.json())

if __name__ == "__main__":
    test_usage(url=API_URL) 