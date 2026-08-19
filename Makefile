.PHONY: check lint format all clean tools

all: tools clean lint format check

tools:
	sudo pipx install --global flake8 pyright black pyflakes pytest cfbs cfengine

clean:
	rm -rf tests/deploy/out

lint: clean tools
	cfbs status
	cfbs validate
	./ci/linting.sh
	cfengine lint --strict no ./

format: lint
	cfengine format --check

check: format
#	pytest promise-types/ -v
	bash tests/deploy/test.sh
