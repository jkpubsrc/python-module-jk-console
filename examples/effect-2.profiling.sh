#!/bin/bash

python3 -m cProfile -o effect-2.prof effect-2.py
snakeviz effect-2.prof

