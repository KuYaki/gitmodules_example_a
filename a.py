import os
# noinspection PyUnresolvedReferences
import gitmodules
from gitmodules_example_b import b


def main():
    print("This is main project 'a' called from " +
          os.path.abspath(".") +
          " and it is going to call main function from its git submodule 'b':")
    b.main()


if __name__ == "__main__":
    main()
