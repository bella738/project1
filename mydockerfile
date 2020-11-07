FROM python:3

COPY MainGame.py ./

ADD live.py ./
ADD MemoryGame.py /
ADD GuessGame.py ./
ADD MainScores.py ./
ADD Score.py ./
ADD Utils.py ./
ADD Score.txt ./

workdir ./

RUN pip install selenium
RUN pip install flask
 
CMD ["python3","./MainGame.py"]
