# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
#Copy all the files to /app directory
COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#Run main1.py when container launches. 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#cd app Go to the project directory (in where your Dockerfile is, containing your app directory).
#docker build -t social_net_image . ###when you are on social_network_ads aroudn 80 second
#docker rm mycontainer
#####docker run -d --name mycontainer -p 80:80 social_net_image
##### http://127.0.0.1/docs #manual http://0.0.0.0/80


