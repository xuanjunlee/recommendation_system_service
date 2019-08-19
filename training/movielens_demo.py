#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 20:34
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import evaluate, print_perf

data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)
algo = KNNWithMeans()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf)
print(data.raw_ratings[1])
