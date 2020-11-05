import Utils
import os
def add_score(points):#wrighting the score to the file score.txt
    score_file_source = Utils.SCORES_FILE_NAME

    if os.path.exists(score_file_source):
        score_file_txt = open(score_file_source, 'r+')
        score_file_txt.write(str(points))
    else:
        score_file_txt = open(score_file_source, 'w')
        score_file_txt.write(str(points))


