from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
import random

# Connect to Milvus
def connect_to_milvus(host: str, port: str):
    """
    Establish a connection to Milvus.

    Args:
        host (str): The host address of the Milvus server.
        port (str): The port number of the Milvus server.
    """
    try:
        connections.connect(alias="default", host=host, port=port)
        print("Successfully connected to Milvus.")
    except Exception as e:
        print(f"Error connecting to Milvus: {e}")
        exit(1)

# Create a collection schema
def create_collection(schema_name: str, description: str):
    """
    Create a collection in Milvus with the specified schema.

    Args:
        schema_name (str): The name of the collection.
        description (str): Description of the collection.

    Returns:
        Collection: The created Milvus collection.
    """
    fields = [
        FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="random", dtype=DataType.DOUBLE),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8)
    ]
    schema = CollectionSchema(fields, description=description)

    # Check if the collection already exists
    if utility.has_collection(schema_name):
        print(f"Collection {schema_name} already exists.")
        return Collection(name=schema_name)
    else:
        # Create a new collection
        try:
            collection = Collection(name=schema_name, schema=schema)
            print(f"Collection {schema_name} created successfully.")
            return collection
        except Exception as e:
            print(f"Error creating collection: {e}")
            exit(1)

# Insert data into the collection
def insert_data(collection):
    """
    Insert sample data into the specified collection.

    Args:
        collection (Collection): The Milvus collection to insert data into.
    """
    data = [
        [i for i in range(10)],  # primary key field: 10 int64 values
        [random.random() for _ in range(10)],  # random field: 10 float values
        [[random.random() for _ in range(8)] for _ in range(10)]  # embeddings field: 10 vectors, each with 8 dimensions
    ]

    try:
        insert_result = collection.insert(data)
        print(f"Inserted data into {collection.name}. Insert result: {insert_result.primary_keys}")
    except Exception as e:
        print(f"Error inserting data: {e}")
        exit(1)

# Flush the collection to ensure data persistence
def flush_collection(collection):
    """
    Flush the collection to ensure data persistence.

    Args:
        collection (Collection): The Milvus collection to flush.
    """
    try:
        collection.flush()
        print(f"Flushed data for {collection.name}.")
    except Exception as e:
        print(f"Error flushing data: {e}")
        exit(1)

# Create an index on the embeddings field
def create_index(collection):
    """
    Create an index on the embeddings field of the specified collection.

    Args:
        collection (Collection): The Milvus collection to create an index on.
    """
    try:
        index_params = {
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128},
            "metric_type": "L2"
        }
        collection.create_index(field_name="embeddings", index_params=index_params)
        print(f"Index created on collection {collection.name}.")
    except Exception as e:
        print(f"Error creating index: {e}")
        exit(1)

# Load the collection into memory
def load_collection(collection):
    """
    Load the collection into memory.

    Args:
        collection (Collection): The Milvus collection to load.
    """
    try:
        collection.load()
        print(f"Collection {collection.name} loaded into memory.")
    except Exception as e:
        print(f"Error loading collection into memory: {e}")

# Query the collection to retrieve inserted entities
def query_collection(collection):
    """
    Query the collection to retrieve entities based on a condition.

    Args:
        collection (Collection): The Milvus collection to query.

    Returns:
        list: The results of the query.
    """
    try:
        results = collection.query(expr="pk >= 0", output_fields=["pk", "random", "embeddings"])
        print(f"Queried entities: {results}")
    except Exception as e:
        print(f"Error querying collection: {e}")

if __name__ == "__main__":
    # Replace with your actual Milvus connection details and collection name
    host = "192.168.49.2"  # Milvus host
    port = "30003"  # Milvus port
    collection_name = "hello_milvus"
    description = "hello_milvus is the simplest demo to introduce the APIs"

    # Connect to Milvus
    connect_to_milvus(host, port)

    # Create collection and perform operations
    collection = create_collection(collection_name, description)
    insert_data(collection)
    flush_collection(collection)
    create_index(collection)
    load_collection(collection)
    query_collection(collection)

