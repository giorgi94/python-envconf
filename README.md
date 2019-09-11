# python-envconf

A simple script to parse env configuration file. Unlike `dotenv` package, it doesn't append variables to `os`, instead it reads config file and returns `dict`, so we don't need to reload server to update global variables.
