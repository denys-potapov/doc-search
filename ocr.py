"""Wrapper for OCR module."""
import sys
import os

import fitz


LANG = 'ukr+eng'
DPI = 300


def get_text(stream):
    """Read document from data bytes."""
    doc = fitz.open(stream=stream)
    text = ''
    for page in doc:
        ocr = page.get_textpage_ocr(language=LANG, dpi=DPI)
        text += ocr.extractText()

    return text


if __name__ == '__main__':
    print(os.environ['TESSDATA_PREFIX'])
    preview = get_text(open(sys.argv[1], 'rb').read())
    print(preview)
