# coding_challenge

## Local Test
1-Clone the repository into your local machine.

2-Execute the server with the following command.

- `python auth_server.py`

3-The server will be available at `http://127.0.0.1:5000/token`

## Docker Local Test

1-Clone the repository into your local machine.

2-Build the Docker image, run the following command.

- `docker build -t auth_server:tag .`

3-The server will be available at `http://127.0.0.1:5000/token`

4-To build the docker images and push it to a private registry

- `docker build -t <privateRegistryUrl>/auth_server:tag .`
- `docker push <privateRegistryUrl>/auth_server:tag`

## Deploy to a Kubernetes Cluster

1-Clone the repository into your local machine.

2-Ensure you have a running k8s cluster and kubectl configured to communicate with it.

3-Change in the manifest file "k8s_auth_server.yaml" the image tag value to the private registry url under line 17.

4-Deploy the server to the cluster, run the following command

- `kubectl apply -f k8s_auth_server.yaml`

5-Find the NodePort assigned to the auth server service, run the following command

- `kubectl get service server-service`

6.1-If you are running k8s locally, you can access the server using `http://localhost:<NodePort>/token`, replacing `<NodePort>` with the assigned NodePort.

6.2-If you are using a remote Kubernetes cluster, use the appropriate IP address or hostname of the cluster's node along with the assigned NodePort to access the server using the `/token` Endpoint.