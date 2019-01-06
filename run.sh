#!/bin/bash
song='YiCiJiuHao'
X='D'
C='C'
#direction=None
python inflexion.py -f ./songs/${song}_${X}.txt -s ./songs/${song}_${C}.txt -x ${X} -c ${C} #-d ${direction} 
