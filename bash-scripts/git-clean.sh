#!/bin/bash
# find top 10 files
git rev-list --objects --all | grep -f <(git verify-pack -v .git/objects/pack/*.idx| sort -k 3 -n | cut -f 1 -d " " | tail -10)

echo -n "Clean all git commit?(y/n)? "
read answer
echo -n "Branch name? (common use: master or main)"
read branchName
if [ "$answer" != "${answer#[Yy]}" ] ;then
    git checkout --orphan latest_branch
    git add -A
    git commit -am "Final Release"
    git branch -D $branchName
    git branch -m $branchName
fi

## see https://github.com/18F/C2/issues/439
echo -n "Start?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo "Cleanup refs and logs"
            rm -Rf .git/refs/original
            rm -Rf .git/logs/

            echo "Cleanup unnecessary files"
            git gc --aggressive --prune=now

            echo "Prune all unreachable objects"
            git prune --expire now
            break;;
        No ) exit;;
    esac
done
echo -n "Push to github now?(y/n)"
read pushConfrmtn
if [ "$pushConfrmtn" != "${pushConfrmtn#[Yy]}" ] ;then
	git push -f origin $branchName
fi
