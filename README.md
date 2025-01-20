<!-- -*- mode: gfm; coding: utf-8; fill-column: 80; -*- -->
# fetch-slack-emoji

## Python environment

Set up the virtual environment:

``` sh
pdm py install cpython@3.12
pdm use -f cpython@3.12
```

Install dependencies:

``` sh
pdm install
```

## Git hooks

``` sh
pdm run pre-commit install
```

## Usage

[This][get-emoji-file] is how I got the `emoji.json` file. Then, you can use
this Python script like so:

``` sh
pdm run download --emoji-file downloads/emoji.json --out-dir downloads/emoji
```


<!-- links -->
[get-emoji-file]: https://gist.github.com/lmarkus/8722f56baf8c47045621?permalink_comment_id=2970482#gistcomment-2970482
