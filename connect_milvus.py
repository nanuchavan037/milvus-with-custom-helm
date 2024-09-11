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
    host = "a48df2f8eb0334f53820dcd250a2b318-1929392595.us-west-2.elb.amazonaws.com"
    port = "19530"
    connect_to_milvus(host, port)
