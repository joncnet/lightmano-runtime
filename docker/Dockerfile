## build : docker build -t lightmano .
## run :   docker run --net=host --rm --privileged -it lightmano

FROM ubuntu:19.10
MAINTAINER Roberto Riggio <rriggio@fbk.eu>

# Installing python dependencies
RUN apt update
RUN apt -y install python3-pip wget unzip
RUN pip3 install tornado==6.0.3 pymodm==0.4.1 influxdb==5.2.3 kubernetes==10.0.1

# Fetching the latest repository from lightmano.
RUN wget https://github.com/joncnet/lightmano-runtime/archive/master.zip
RUN unzip master.zip
RUN rm master.zip
RUN ln -sf /lightmano-runtime-master/conf/ /etc/lightmano
RUN mkdir -p /var/www
RUN ln -sf /lightmano-runtime-master/webui/ /var/www/lightmano

# Run the controller
ENTRYPOINT ["python3.7", "/lightmano-runtime-master/lightmano-runtime.py"]

# Expose Web GUI
EXPOSE 8888
