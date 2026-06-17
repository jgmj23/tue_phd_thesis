MAIN ?= thesis
ENGINE ?= xelatex

.PHONY: pdf tectonic latexmk clean distclean

pdf: tectonic

tectonic:
	tectonic --keep-logs --keep-intermediates $(MAIN).tex

latexmk:
	latexmk -$(ENGINE) -interaction=nonstopmode -halt-on-error $(MAIN).tex

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).run.xml $(MAIN).toc

distclean:
	$(MAKE) clean
	rm -f $(MAIN).pdf
