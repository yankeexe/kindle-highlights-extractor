# Kindle Hightlights Extractor

Extract highligts from "My Clippings.txt" file on Kindle.

Group and manage those highlights on a JSON format.

> **Independent function for the project:** [extractor-function](https://github.com/yankeexe/kindle-highlights-extractor)

## Usage

### Start the server

```bash

$ flask run

```

### Using httpie

```bash

$ http -df POST http://localhost:5000/jsonify file@'<filepath or filename>'

```
