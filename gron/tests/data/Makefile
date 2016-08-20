default:
	make clean
	make gen

clean:
	rm -f *answer*

gen:
	for i in *.json; do gron -m $$i > $${i%.json}-answer.json; done

.PHONY: clean gen

