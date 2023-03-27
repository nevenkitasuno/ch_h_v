NAME 			= ch_h_v
SRCS			= src/$(wildcard *.py)

$(NAME):
	zip -jr $(NAME).zip $(SRCS)
	echo '#!/usr/bin/env python' | cat - $(NAME).zip > $(NAME)
	chmod +x $(NAME)

all: $(NAME)

test:
	mypy $(SRCS)
	pytest --doctest-modules $(SRCS)

	ln -sr ch_h_v test/case_1/ch_h_v
	cd test/case_1; ./test.sh
	rm -f test/case_1/ch_h_v

clean:
	rm -f test/case_1/ch_h_v
	rm -f $(NAME).zip

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all test clean fclean re