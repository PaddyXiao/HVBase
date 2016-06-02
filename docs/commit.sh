#!/bin/bash
make html
git add -f *
git commit -m 'Modify html content'
git push -u origin master
