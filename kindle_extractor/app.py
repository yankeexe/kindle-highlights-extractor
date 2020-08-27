import json
from itertools import zip_longest, islice
from collections import defaultdict

from werkzeug.utils import secure_filename
from flask import Flask, abort, request, send_file, render_template, redirect

from kindle_extractor import config, helpers


def create_app():
    """
    Application factory entrypoint.
    """

    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(config.Config)

    @app.route("/app")
    def homepage():
        return render_template("base.html")

    @app.route("/jsonify", methods=["POST"])
    def clippings_jsonify():
        """
        Takes the file input and process it.
        """
        # Create tempfile to hold the uploaded file.
        input_tempfile = helpers.temp_file(".txt")

        if not request.files:
            abort(406, "Request payload can only be files.")

        file = request.files["clippings"]
        print(request.files)
        filename = secure_filename(file.filename)
        print("secure filename", filename)

        if not filename:
            abort(404, "File not found.")

        if not helpers.allowed_file(filename):
            abort(
                415, "Allowed MIME type: text/plain",
            )

        file.save(input_tempfile)

        data_dict = defaultdict(list)

        with open(input_tempfile, "r", encoding="utf-8-sig") as txt:
            for item in zip_longest(*[iter(txt)] * 5, fillvalue=""):
                strings = " ".join(item)
                lists = list(strings.split("\n"))

                book_name = lists[0].encode("ascii", "ignore").decode("utf-8")
                clipping = lists[3].encode("ascii", "ignore").decode("utf-8").lstrip()

                # Check for empty string
                if clipping:
                    data_dict[book_name].append(clipping)

        # Remove duplicate values
        for key, value in data_dict.items():
            data_dict[key] = list(set(value))

        return redirect()

        # Output JSON file.
        output_tempfile = helpers.temp_file(".json", delete=False)
        print("output tempfile", output_tempfile)

        with open(output_tempfile, "w+") as f:
            json.dump(dict(data_dict), f, indent=4)

        return send_file(
            output_tempfile,
            mimetype="application/json",
            as_attachment=True,
            attachment_filename=f"{filename.split('.')[-2]}.json",
        )

    return app
