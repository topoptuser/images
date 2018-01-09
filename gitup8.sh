#!/bin/sh

python hp-server-images.py 10
git config --local user.name topoptuser
git config --local user.email topoptuser@gmail.com
git add .
git commit -m up8
git push origin master
