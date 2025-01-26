all: markov markov.png
	
markov:
	python3 run_markov.py
markov.png: simple_markov.dot
	dot -Tpng simple_markov.dot > markov.png
markov.svg: simple_markov.dot
	dot -Tsvg simple_markov.dot > markov.svg
clean:
	rm -f markov.png markov.svg`