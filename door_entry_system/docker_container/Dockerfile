from raspbian/stretch:latest

RUN sudo apt-get install python3 && sudo apt update && sudo apt install python3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["door_entry.py"]