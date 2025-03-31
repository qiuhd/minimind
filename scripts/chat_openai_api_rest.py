import requests

proxies = { 
              "http"  : '', 
              "https" : '', 
              "ftp"   : ''
            }

def send_completion_request():
    url = "http://127.0.0.1:8998/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = '''
        {
            "model": "MiniMind",
            "messages": [
                {
                    "role": "user",
                    "content": "讲个关于小猪的童话故事"
                }
            ]
        }
'''
    response = requests.post(url, headers=headers, data=data, proxies=proxies)
    return response.json()

# Example usage:
api_key = "YOUR_OPENAI_API_KEY"
response = send_completion_request()
print(response['choices'][0]['message']['content'])