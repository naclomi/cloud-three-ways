# To build:
#   docker login
#   docker build -t [username]/kmeans-test:0.1 .
#   docker push [username]/kmeans-test:0.1
# To run:
#   docker run --rm [username]/kmeans-test:0.1 .
# To run (on azure):
#   Create a task that pulls [username]/kmeans-test:0.1
FROM jupyter/scipy-notebook

COPY kmeans.py /home/joyvan/kmeans.py

ENTRYPOINT /bin/bash -c 'python3 /home/joyvan/kmeans.py'
