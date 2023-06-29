from fastapi import FastAPI,UploadFile
from typing import List
from minio_connection import minio_client
import io
import os
key:int = 1
app = FastAPI()

@app.post("/postData")
def post_data(my_data:List[UploadFile]):
    html_code = my_data[0].file.read().decode()
    css_code = my_data[1].file.read().decode()
    js_code =  my_data[2].file.read().decode()
  
    combined_data = f'<html><head><style>{css_code}</style></head><body>{html_code}</body><script>{js_code}</script></html>'
    global key
    if  not os.path.exists(str(key)):
        os.mkdir(f'files/{key}')
    with open(f"files/{key}/index.html","w") as f:    
        f.write(combined_data)
    key+=1
    return {f'http://localhost:8080/{key-1}/index.html'}

    # it will not work with minio as local http server only hosts current directory files
#     if not minio_client.bucket_exists('demo'):
#         minio_client.make_bucket("demo")

#     data =io.BytesIO(combined_data.encode('utf-8'))
#     minio_client.put_object(
#         bucket_name="demo",
#         object_name='index.html',
#         data=data,
#         length=data.getbuffer().nbytes
#     )
    
#     url =minio_client.presigned_get_object(
#         bucket_name="demo",
#         object_name='index.html',
#     )
#     print(url)

# def get_url():
#     url =minio_client.presigned_get_object(
#         bucket_name="demo",
#         object_name='index.html',
#     )
#     print(url)
#     return url

