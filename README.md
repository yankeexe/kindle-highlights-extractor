# Kindle Hightlights Extractor

Extract highligts from "My Clippings.txt" file on Kindle.

Group and manage those highlights on a JSON format.

## Usage

### Start the server

```bash

$ flask run

```

### Using httpie

```bash

$ http -df POST http://localhost:5000/jsonify file@'<filepath or filename>'

```
