from raspbian/stretch:latest

RUN sudo apt update && sudo apt-get install python3.7 && python3.7 -m pip install pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["door_entry.py"]