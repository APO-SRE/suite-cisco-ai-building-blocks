#!/usr/bin/env python3
################################################################################
## ai-building-blocks-database/scripts/utils/chunking.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
from __future__ import annotations

"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_file(filepath_or_text, chunk_size=1000, chunk_overlap=200):
    """
    Processes either a file path or raw text, splits into manageable chunks, 
    and returns them as a list of strings.

    Args:
        filepath_or_text (str): Path to the file or raw text to process.
        chunk_size (int): Max size of each chunk (chars).
        chunk_overlap (int): Overlap size (chars) between chunks.

    Returns:
        List[str]: List of text chunks.
    """
    text = ""
    if os.path.isfile(filepath_or_text):
        with open(filepath_or_text, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = filepath_or_text

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    return chunks
