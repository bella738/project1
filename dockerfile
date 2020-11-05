FROM python:3-alpine 

ADD MainGame.py ./
ADD live.py ./
ADD MemoryGame.py /
ADD GuessGame.py ./
ADD MainScore.py ./
ADD Score.py ./
ADD Utils.py ./
ADD Score.txt ./

workdir ./

RUN pip install
 
CMD ["python3","./MainGame.py"]
