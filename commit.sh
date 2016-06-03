cd docs
make html
cd ..
git add -f *
git commit -m 'Modify description of function getCall()'
git push -u origin master
