while read p; do
	rm -rf "email/$p"
	cp -rf "apply/$p" email/$p
done <emaildirs.txt

rm -r $(find email/* | grep '.log\|.tex\|.aux\|.out\|vars.txt\|body.txt')
