# Milvus Helm Chart

This README provides instructions for deploying the Milvus chart using Helm. The chart includes deployments for Milvus, etcd, MinIO, and Attu, as well as the necessary services.

## Prerequisites

- Kubernetes cluster (Minikube or any other Kubernetes environment)
- Helm 3.x installed
- `kubectl` configured to interact with your Kubernetes cluster

## Install the Helm Chart

Install the Helm chart using the following command:

```bash
helm install milvus-release milvus-chart
```

## Verify Deployment

Check the status of the deployed resources:

```bash
kubectl get all -n milvus
```

## Access the Services

The services are exposed using NodePort. You can access them using the node IP and the assigned node ports:

### If you are using minikube
Attu: http://<NODE_IP>:30005
Etcd: http://<NODE_IP>:30001
Milvus:
gRPC: http://<NODE_IP>:30003
HTTP: http://<NODE_IP>:30004
MinIO: http://<NODE_IP>:30002

### if you are using cluster (EKS, AKS) and Network Type LoadBalancer
Attu: http://<External_IP>:8000
Milvus:
gRPC: http://<External_IP>:19530
HTTP: http://<External_IP>:9091

Replace <NODE_IP> with the IP address of your Kubernetes node. If you're using Minikube, you can get the IP with:

```bash
minikube ip
```

## Uninstall the Helm Chart

To uninstall the Helm chart and remove all associated resources:

```bash
helm uninstall milvus-release
```

## Using Python Scripts

#### Note: 
If you want to communicate with Milvus using code rather than the UI, you need to expose the Milvus service appropriately. For EKS or AKS, use a LoadBalancer service type, and for Minikube, use a NodePort.


### 1. connection.py

This script establishes a connection to the Milvus server. Ensure Milvus is running and accessible before running this script.

Usage:

```bash
python connection.py
```

This will attempt to connect to the Milvus server using the provided host and port. Modify the host and port variables in the script to match your Milvus service configuration.

### 2. manage_collection.py

This script performs operations such as creating a collection, inserting data, creating an index, loading the collection into memory, and querying the collection.

Usage:

```bash
python manage_collection.py
```

This script will:

Create a collection with the specified schema.
Insert sample data into the collection.
Flush the collection to ensure data persistence.
Create an index on the embeddings field.
Load the collection into memory.
Query the collection to retrieve inserted entities.
Ensure that connection.py is executed successfully before running manage_collection.py.

### 3. list_collection.py

Listing Collections
The list_collection.py script lists all the collections in Milvus.

```bash
python  list_collection.py
```

### Note:

Replace host with your actual host IP or External ip in case of LoadBalancer in connection.py and manage_collection.py to connect with your Milvus database.

