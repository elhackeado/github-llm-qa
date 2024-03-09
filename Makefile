init:
	pip install -r requirements.txt
	rm -rf issues || true
	rm -rf chroma_storage || true
	mkdir -p documents
	python3 scrape-discussions.py
	python3 load_data.py

run:
	python3 main.py