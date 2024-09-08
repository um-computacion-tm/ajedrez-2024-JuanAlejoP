FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-JuanAlejoP.git

WORKDIR /ajedrez-2024-JuanAlejoP

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python game/client.py"]

# docker buildx build -t ajedrez-2024-juanalejop .
# docker run -i ajedrez-2024-juanalejop