#!/bin/bash
RED='\033[0;31m'
GRN='\033[0;32m'
YLW='\033[0;33m'
bCYN='\033[1;36m'
RST='\033[0m'
printf "\033c"
echo -e "\n\n$bCYN ************************************************* $RST \n"
echo -e "$bCYN           Creating a new repo on Github              $RST \n"
echo -e "$bCYN ************************************************* $RST \n\n"
echo -en "$YLW Did you create a blank repo on Github website? (y/n) >>  $RST"
read answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
	echo -en "$YLW Paste the repo name here. >> $RST"
     	read repoName
	# echo -en "$YLW Paste the repo url here. >> $RST"
   #   	read repoURL
	echo -en "$YLW Branch name? (common use: master or main) >> $RST"
		read branchName
else
	echo -en "$RED Please create a balnk repo first on Github website. $RST\n"
	exit
fi

echo -en "$YLW Add this folder to Github? (yes/no) >>  $RST"
read yn
if [ "$yn" != "${yn#[Yy]}" ] ;then
				echo -en "$YLW Creating README.md, enter message >>  $RST"
		  		  	read readmeMsg
				  	echo "# $readmeMsg" >> README.md
				  echo -en "$GRN initialising git  $RST\n"
				  	git init
				  echo -en "$GRN Adding all file in this folder to git.  $RST\n"
				  	git add .
				  echo -en "$GRN Commiting to git with 'first commit' message.  $RST\n"
				   git commit -m "first commit"
				 echo -en "$GRN Setting branch $branchName   $RST\n"
				 	git branch -M main
				 echo -en "$GRN Adding repo URL 'https://github.com/pankajpopli/$repoName.git' as origin.    $RST\n"
				 	git remote add origin https://github.com/pankajpopli/$repoName.git
				echo -en "$YLW Push to Github? (y/n) >>   $RST"
				read pushconfirm
				if [ "$pushconfirm" != "${pushconfirm#[Yy]}" ] ;then
					git push -u origin main
					echo -en "$GRN Repo added succesfully. $RST\n"
				else
					echo -en "$RED Exiting now. $RST\n"
					exit
				fi
else
	echo -en "$RED Exiting now. $RST\n"
	exit
fi