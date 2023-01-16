# Set base image
FROM python:3.9

#set working directory
WORKDIR /uiapp

COPY ./requirements.txt /uiapp/requirements.txt
#Copy all the files to /app directory
COPY . /uiapp
##
RUN pip install --no-cache-dir --upgrade -r /uiapp/requirements.txt

# Expose port
EXPOSE 8501

# Execute command when container starts
CMD ["streamlit", "run", "stream_app.py"]

# To build this Docker image for frontend subdir, run the following (from main directory)
# docker build -t <app-name e.g. streamlitui>:latest -f frontend/Dockerfile frontend/
# Command to run Docker image: docker run -d -p 8501:8501 <streamlit-app-name>:latest
#######before
#docker build -t social_net_image . ###when you are on social_network_ads aroudn 80 second
#docker rm mycontainer
#####docker run -d --name mycontainer -p 80:80 social_net_image
##### http://127.0.0.1/docs #manual http://0.0.0.0/80