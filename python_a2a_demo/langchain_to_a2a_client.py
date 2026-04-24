from python_a2a import HTTPClient

client = HTTPClient("http://localhost:5000")
response = client.send_message("What is the square root of 144?")
print(response.content)
response = client.send_message("In short, why speed of light is constant?")
print(response.content)
