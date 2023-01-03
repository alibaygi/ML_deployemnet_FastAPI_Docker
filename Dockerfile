FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./app /app/app



#sudo docker build -t social_net_image . ###when you are on social_network_ads
#sudo docker rm mycontainer
#####sudo docker run -d --name mycontainer -p 8000:8000 social_net_image
#sudo docker run -p 80:80 social_net_image