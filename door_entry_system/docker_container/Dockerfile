from raspbian/stretch:latest

RUN sudo apt update && sudo apt install python3-dev && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["door_entry.py"]