"""Top-level package for League App."""
__app_name__ = "League App"
__version__ = "1.0.0"

(
    SUCCESS,
    PROCESSING_ERROR,
    FILE_READ_ERROR,
    FILE_WRITE_ERROR,
) = range(4)

ERRORS = {
    PROCESSING_ERROR: "Processing error",
    FILE_READ_ERROR: "File read error",
    FILE_WRITE_ERROR: "File write error",
}
