# auto commit docs

rm ../csv-to-custom-json-python.wiki/*
cp -pR docs/* ../csv-to-custom-json-python.wiki/

cd ../csv-to-custom-json-python.wiki
git add .
git commit -m "update-docs"
git push
cd ../csv-to-custom-json-python
pwd
git add docs/
git commit -m "auto-update-docs"
git push
