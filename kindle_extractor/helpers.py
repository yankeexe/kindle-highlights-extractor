""" Helper functions. """
import tempfile


def allowed_file(filename):
    """
    Check for file extension against the allowed extension set.

    :param str filename: name of the file (with extension) for the check.
    """
    ALLOWED_EXTENSIONS = {"txt"}

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def temp_file(suffix, delete=True):
    """
    Creates temporary file.

    :param str suffix: Suffix for the file. ex: '.txt', '.json'
    :param bool delete: If True delete tempfile auto. If False manual.
    """
    temp = tempfile.NamedTemporaryFile(suffix=suffix, delete=delete)
    return temp.name
