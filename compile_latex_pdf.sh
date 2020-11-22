DIRS=$(ls -d apply/*)
for DIR in $DIRS
do
	pdflatex -aux-directory=$DIR -output-directory=$DIR $DIR'/letter.tex'
done
