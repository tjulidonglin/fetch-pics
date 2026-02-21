#!/bin/bash
echo "Please verify your repository URL:"
curl -s https://github.com/tjulidonglin/fetch-pics | head -50 | grep -i title || echo "404: Repository not found"

echo ""
echo "Local git remote:"
git remote -v

echo ""
read -p "Press enter to push..." 
git push -u origin master
