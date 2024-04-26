FROM locustio/locust
WORKDIR /locust
COPY locustfile.py ./

# Diagnostic tools
RUN apt-get update && apt-get install -y net-tools iproute2

# Change ENTRYPOINT to shell script sending arguments to locust
ENTRYPOINT ["sh", "-c", "locust $0 $@"]
