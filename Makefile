MAIN ?= thesis
ENGINE ?= xelatex

# Vendored biblatex that matches the system biber. Tectonic bundles an older
# biblatex than Homebrew's biber, which otherwise fails with a "biblatex
# control file version ... incompatible" error. See tools/biblatex/README.md.
BIBLATEX_DIR ?= tools/biblatex

.PHONY: pdf tectonic latexmk clean distclean

pdf: tectonic

tectonic:
	tectonic -Z search-path=$(BIBLATEX_DIR) --keep-logs --keep-intermediates $(MAIN).tex

latexmk:
	latexmk -$(ENGINE) -interaction=nonstopmode -halt-on-error $(MAIN).tex

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).run.xml $(MAIN).toc

distclean:
	$(MAKE) clean
	rm -f $(MAIN).pdf
