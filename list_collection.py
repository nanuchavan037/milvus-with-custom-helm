from pymilvus import connections, utility

# Connect to Milvus
def connect_to_milvus(host: str, port: str):
    try:
        connections.connect(alias="default", host=host, port=port)
        print("Successfully connected to Milvus.")
    except Exception as e:
        print(f"Error connecting to Milvus: {e}")
        exit(1)

# List collections in Milvus
def list_collections():
    try:
        collections = utility.list_collections()
        if collections:
            print("Collections in Milvus:")
            for collection in collections:
                print(collection)
        else:
            print("No collections found.")
    except Exception as e:
        print(f"Error listing collections: {e}")

if __name__ == "__main__":
    # Replace with your actual host and port
    host = "a302345d8ec6048a1bbebec680a494d1-831671810.us-west-2.elb.amazonaws.com"
    port = "19530"
    connect_to_milvus(host, port)
    list_collections()
