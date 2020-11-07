FROM python:3.7-alpine
COPY MainScores.py ./

ADD live.py ./
ADD MemoryGame.py /
ADD GuessGame.py ./
ADD  MainGame.py ./
ADD Score.py ./
ADD Utils.py ./
ADD Score.txt ./

workdir ./

RUN pip install selenium
RUN pip install flask
 
CMD ["python3","./MainScores.py"]
