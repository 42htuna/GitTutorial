# YENİ REPOSITORY OLUŞTURMAK:
echo "# GitTutorial" >> README.md
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/42htuna/GitTutorial.git
git push -u origin master

## YENİ BRANCH OLUŞTURMAK:
git checkout -b newBranch
git commit -m “Yeni Branch Eklendi”
git push origin newBranch
