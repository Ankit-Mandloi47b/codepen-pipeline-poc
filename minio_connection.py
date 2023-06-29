from minio import Minio

try:
    minio_client = Minio(
        endpoint=f"localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )   
except Exception as e:
    print(e)