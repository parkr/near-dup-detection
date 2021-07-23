.PHONY: test
test:
	python -m ndd.ndd
	python -m ndd.unit.ndindex_spec
	python -m ndd.unit.ngram_spec
