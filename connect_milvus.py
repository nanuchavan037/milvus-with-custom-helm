from pymilvus import connections

# Connect to Milvus
def connect_to_milvus(host: str, port: str):
    try:
        connections.connect(alias="default", host=host, port=port)
        print("Successfully connected to Milvus.")
    except Exception as e:
        print(f"Error connecting to Milvus: {e}")
        exit(1)

if __name__ == "__main__":
    # Replace with your actual host and port
    connect_to_milvus("192.168.49.2", "30003")
