#!/bin/bash

python3 -m cProfile -o effect-1.prof effect-1.py
snakeviz effect-1.prof

