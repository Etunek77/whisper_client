import requests
import os
import json

url = "http://127.0.0.1:5000/transcribe?model=tiny.en&language=english"
file_name = "Recording.m4a"
file_path = "Recording.m4a"
file = open(file_path,"rb")

content_type = "audio/m4a"


audio_file = {"audio_file":(file_name, file, content_type)}

response = requests.post(url,files=audio_file)


output_path = "output"
if not os.path.exists(output_path):
    os.mkdir(output_path)

transcript_text_path = os.path.join(output_path, "{}.txt".format(file_name))
status_code = response.status_code
response = response.json()
# print(response.status_code)
print(response)
# print(response.keys())

if status_code==200:
    with open(transcript_text_path,"w") as f:
        f.write(response["text"])

