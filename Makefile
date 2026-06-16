.PHONY: validate test evals qa

validate:
	python3 scripts/validate_repo.py

test:
	python3 -m unittest discover -s tests -v

evals:
	python3 scripts/run_evals.py --summary

qa: validate test evals
