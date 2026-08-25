# -*- coding: utf-8 -*-
"""
Plain-text dump of a .docx's body paragraphs. No external deps (python-docx
not required) - reads word/document.xml directly out of the zip.

Usage: python extract_docx_text.py <path-to-docx>
Prints the extracted text to stdout.
"""
import sys
import zipfile
import re

def extract(path):
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "\n")
    text = re.sub(r"<[^>]+>", "", xml)
    return text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_docx_text.py <path-to-docx>")
        sys.exit(1)
    print(extract(sys.argv[1]))
