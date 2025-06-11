#!/usr/bin/env python3
################################################################################
## suite-cisco-ai-building-blocks/src/db_scripts/indexers/elastic_indexer.py
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
import os, json
from elasticsearch import Elasticsearch
from .base_indexer import BaseIndexer
from app.utils.embedding import embed_text
class ElasticIndexer(BaseIndexer):
    def __init__(self, index_name: str):
        super().__init__(index_name)
        self.host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.user = os.getenv("ELASTIC_USER", "elastic")
        self.password = os.getenv("ELASTIC_PASSWORD", "changeme")
        self.client = Elasticsearch(self.host, http_auth=(self.user, self.password))
    
    def create_index(self):
        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(index=self.index_name, body={
                "mappings": {
                    "properties": {
                        "content": {"type": "text"},
                    }
                }
            })
            print(f"Created Elasticsearch index {self.index_name}.")
        else:
            print(f"Elasticsearch index {self.index_name} already exists.")
    
    def index_documents(self, docs: list):
        for doc in docs:
            self.client.index(index=self.index_name, document=doc)
        print(f"Elasticsearch: Indexed {len(docs)} documents in {self.index_name}.")

class PlatformFunctionIndexer(ElasticIndexer):
    def index_functions(self, platform: str, diet_list: list[dict], full_spec: dict):
        docs = [
            {"id": f"{platform}:{fn['name']}", "content": json.dumps(fn)}
            for fn in diet_list
        ]
        self.index_documents(docs) 