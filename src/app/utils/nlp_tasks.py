#!/usr/bin/env python3
################################################################################
## suite-cisco-ai-building-blocks/src/app/utils/nlp_tasks.py
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
import logging
import yake

# Summaries
SUMMARIZER_TYPE = os.getenv("API_VECTOR_SUMMARIZER_TYPE", "sumy").strip().lower()
# Keywords
KEYWORD_EXTRACTOR_TYPE = os.getenv("API_VECTOR_KEYWORD_TYPE", "keybert").strip().lower()

# Summaries
_summarizer_pipeline = None
def summarize_text_sumy(text: str) -> str:
    if not text.strip():
        return ""
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lex_rank import LexRankSummarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = LexRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")

    max_sents = 5
    doc_sents = len(list(parser.document.sentences))
    if doc_sents < max_sents:
        max_sents = doc_sents
    summary_sents = summarizer(parser.document, max_sents)
    summary_str = " ".join(str(s) for s in summary_sents)
    return summary_str.strip()

def summarize_text_transformer(text: str) -> str:
    global _summarizer_pipeline
    if not _summarizer_pipeline:
        from transformers import pipeline
        logging.info("[nlp_tasks] Loading DistilBART summarizer pipeline...")
        _summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)
    if not text.strip():
        return ""
    out = _summarizer_pipeline(text, max_length=120, min_length=30, do_sample=False)
    return out[0]['summary_text'].strip() if out else ""

def summarize_text(text: str) -> str:
    if SUMMARIZER_TYPE in ["none", "", "null"]:
        return ""
    if SUMMARIZER_TYPE in ["sumy", "gensim", "lexrank"]:
        # Gensim is deprecated, use sumy
        return summarize_text_sumy(text)
    elif SUMMARIZER_TYPE in ["transformers", "transformer", "hf", "bart"]:
        return summarize_text_transformer(text)
    else:
        logging.warning(f"[nlp_tasks] Unrecognized SUMMARIZER_TYPE '{SUMMARIZER_TYPE}', defaulting to sumy.")
        return summarize_text_sumy(text)

# Keywords
_kw_model_keybert = None
def extract_keywords_keybert(text: str) -> list:
    global _kw_model_keybert
    if not _kw_model_keybert:
        from sentence_transformers import SentenceTransformer
        from keybert import KeyBERT
        model_name = os.getenv('API_VECTOR_EMBEDDINGS_MODEL', 'all-MiniLM-L6-v2')
        emb_model = SentenceTransformer(model_name)
        _kw_model_keybert = KeyBERT(emb_model)
        logging.info(f"[nlp_tasks] Initialized KeyBERT with model: {model_name}")
    results = _kw_model_keybert.extract_keywords(text, top_n=10)
    return [r[0] for r in results]

def extract_keywords_yake(text: str) -> list:
    import yake
    extractor = yake.KeywordExtractor(lan="en", n=3, top=10)
    results = extractor.extract_keywords(text)
    return [kw for (kw, score) in results]

def extract_keywords(text: str) -> list:
    # Check if user wants keywords
    enable_keywords = os.getenv("API_VECTOR_ENABLE_KEYWORDS", "false").lower() == "true"
    if not enable_keywords or not text.strip():
        return []
    if KEYWORD_EXTRACTOR_TYPE == "yake":
        return extract_keywords_yake(text)
    else:
        # default to keybert
        return extract_keywords_keybert(text)