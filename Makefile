NAME 			= ch_h_v
SRCS			= src/$(wildcard *.py)

$(NAME):
	zip -jr $(NAME).zip $(SRCS)
	echo '#!/usr/bin/env python' | cat - $(NAME).zip > $(NAME)
	chmod +x $(NAME)

all: $(NAME)

test: $(NAME)
	pytest --doctest-modules

clean:
	rm -f $(NAME).zip

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all test clean fclean re