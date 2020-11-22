cp -r apply/* email/
rm -r $(find email/* | grep '.log\|.tex\|.aux\|.out\|.txt')
