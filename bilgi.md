# YENİ REPOSITORY OLUŞTURMAK:

echo "# GitTutorial" >> README.md

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/42htuna/GitTutorial.git

git push -u origin master


<<<<<<< HEAD
=======

>>>>>>> fb6187212302142512905039a57ca6c2e8cc9677
## YENİ BRANCH OLUŞTURMAK:

git checkout -b newBranch

git commit -m “Yeni Branch Eklendi”

git push origin newBranch
