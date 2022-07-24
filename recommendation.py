from sklearn.neighbors import NearestNeighbors
import numpy as np
import joblib
import pymysql

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from emotextanalysis import emotext
from typing import List
from collections import namedtuple
from emotextanalysis import emotext
import json
import os.path
import types

# 读取配置文件
with open('config.json') as f:
    config = json.load(f)

engine = create_engine(config['db'])

Base = automap_base()
Base.prepare(engine, reflect=True)

# 数据表读入
Track = Base.classes.musics
Comment = Base.classes.comments
TrackEmotion = Base.classes.track_emotions
Album = Base.classes.albums
Artist = Base.classes.artists

session = Session(engine)

# 模型和数据导入
savefile = os.path.join('savemodel', '1658559234-1.joblib')

nbrs = joblib.load(savefile)
datafile = os.path.join('savedata', '1658558322-1.json')

with open(datafile, 'r') as f:
    data = json.load(f)


# print(data)


def softmax_dict(x: dict):
    s = sum(v for v in x.values())
    for k in x:
        x[k] /= s
    return x


def keys(self):
    return self._fields


def values(self):
    return tuple(self)


def emotion_vector(emotions: List[TrackEmotion]):
    elems = dict.fromkeys(emotext.emotions, 0)
    elems.update({x.emotion: x.intensity for x in emotions})
    ev = Emotion(**elems)

    return ev


Emotext = emotext.Emotions()

Emotion = namedtuple('Emotion', emotext.emotions)

Emotion.keys = keys
Emotion.values = values

# 推荐系统得到音乐
def recommend_from_text(text: str):
    # emotext
    r = Emotext.emotion_count(text)
    r.emotions = softmax_dict(r.emotions)
    e = Emotion(**r.emotions)

    # recommend
    distances, indices = nbrs.kneighbors([e], 1)

    # result tracks
    tracks = []
    for i in range(len(indices[0])):
        idx = indices[0][i]
        id = data['ids'][idx]
        t = session.query(Track).filter_by(music_id=id)[0]
        e = session.query(TrackEmotion).filter_by(music_id=t.music_id).all()
        tracks.append(t)

    return e, distances, tracks

# 输出推荐歌曲的相关信息！
def print_nbrs(distances, tracks):
    for d, t in zip(distances[0], tracks):
        a = session.query(Album).filter_by(album_id=t.album_id)[0]
        singer = session.query(Artist).filter_by(artist_id=a.artist_id)[0]

        # 这里我只是print， 有必要可以修改！
        print(f'dist={d:.4f}: ({t.music_id})\t {t.music_name} - {singer.artist_name}')


if __name__ == "__main__":
    # 测试用例
    emotion, distances, tracks = recommend_from_text('后悔也都没有用 还不如一切没有发生过 不过就是又少一个诗人 换一个人沉迷你的笑')
    print_nbrs(distances, tracks)
