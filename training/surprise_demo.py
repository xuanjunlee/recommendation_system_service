#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 19:57
from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf

data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)
algo = SVD()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)
