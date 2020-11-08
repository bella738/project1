FROM python:3.7-alpine
COPY MainScores.py ./
COPY Score.txt ./

ADD live.py ./
ADD MemoryGame.py /
ADD GuessGame.py ./
ADD  MainGame.py ./
ADD Score.py ./
ADD Utils.py ./

workdir ./

RUN pip install selenium
RUN pip install flask
 
CMD ["python3","./MainScores.py"]
