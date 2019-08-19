#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 20:44
import os
from surprise import Reader, Dataset

# 指定文件路径
file_path = os.path.expanduser('./popular_music_suprise_format.txt')
# 指定文件格式
reader = Reader(line_format='user item rating timestamp', sep=',')
# 从文件读取数据
music_data = Dataset.load_from_file(file_path, reader=reader)
# 分成5折
music_data.split(n_folds=5)

music_data.raw_ratings[:20]

from surprise import NormalPredictor, evaluate

algo = NormalPredictor()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

from surprise import BaselineOnly, evaluate

algo = BaselineOnly()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

from surprise import KNNBasic, evaluate

algo = KNNBasic()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

### 使用均值协同过滤
from surprise import KNNWithMeans, evaluate

algo = KNNWithMeans()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

### 使用协同过滤baseline
from surprise import KNNBaseline, evaluate

algo = KNNBaseline()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

### 使用SVD
from surprise import SVD, evaluate

algo = SVD()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

### 使用SVD++
from surprise import SVDpp, evaluate

algo = SVDpp()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])

### 使用NMF
from surprise import NMF

algo = NMF()
perf = evaluate(algo, music_data, measures=['RMSE', 'MAE'])
print_perf(perf)
