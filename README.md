# python_test

My first thought in order to do this assignment was to use python requests library. Later I realised that this was not possible
since python requests does not support API token authorization. Since I do not know how to provide token authorization inside a
web framework like Django, I just used the API token as if it was an API key. The result of course is not the one expected,
since authorization cannot be provided this way. At least you can see how the python code woudl work if I was given an API key
instead of an API token.
