rm -r email/*
cp -r apply/* email/
rm -r $(find email/* | grep '.log\|.tex\|.aux\|.out\|vars.txt\|body.txt')
