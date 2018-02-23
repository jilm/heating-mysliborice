build/heat.pdf : build/blockdiagram.tex src/heat.tex build/room_numbers.tex build/bo.tex build/component_list.tex
	pdflatex --output-directory=build src/heat.tex

build/blockdiagram.tex : script/blockdiagram.py
	python3 script/blockdiagram.py > build/blockdiagram.tex

build/room_numbers.tex : script/room_numbers.py
	python3 script/room_numbers.py

build/bo.tex : script/bo2.py
	python3 script/bo2.py > build/bo.tex

build/component_list.tex : script/component_list.py
	python3 script/component_list.py

