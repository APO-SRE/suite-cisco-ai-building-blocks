#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/app/retrievers/elastic_retriever.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
 
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
from typing import List
from elasticsearch import Elasticsearch
#from app.llm.llm_factory import AzureOpenAIClient

class ElasticRetriever:
    """
    A retriever that uses Elasticsearch for vector-based (and/or hybrid) retrieval.
    """

    def __init__(self):
        self.elastic_host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.elastic_user = os.getenv("ELASTIC_USERNAME", "elastic")
        self.elastic_pass = os.getenv("ELASTIC_PASSWORD", "changeme")
        self.elastic_index = os.getenv("ELASTIC_INDEX", "cisco_docs")
        self.elastic_vector_field = os.getenv("ELASTIC_VECTOR_FIELD", "embedding")
        # For hybrid, you might store the text in a field named "content" and the vector in "embedding".
        self.es = Elasticsearch(
            self.elastic_host,
            basic_auth=(self.elastic_user, self.elastic_pass),
            verify_certs=False
        )

        # For embeddings
        #self.llm_client = AzureOpenAIClient()

    def retrieve_documents(self, user_input: str, top_k: int = 5) -> List[str]:
        """
        1) Get embedding for user_input
        2) Query Elasticsearch (k-NN or hybrid)
        3) Return doc chunks
        """
        embedding = self.llm_client.get_embedding(user_input)

        # EXAMPLE: a simple vector query in ES 8.x
        # If you want strictly vector search:
        # (Note: the field "embedding" must be mapped as a dense_vector or similar.)
        query = {
            "size": top_k,
            "query": {
                "knn": {
                    self.elastic_vector_field: {
                        "vector": embedding,
                        "k": top_k
                    }
                }
            }
        }

        # If you want a hybrid approach (BM25 + vector), you can do something like:
        # query = {
        #   "size": top_k,
        #   "query": {
        #       "bool": {
        #           "should": [
        #               { "match": { "content": user_input } },
        #               {
        #                   "script_score": {
        #                       "query": {"match_all": {}},
        #                       "script": {
        #                           "source": f"cosineSimilarity(params.queryVector, '{self.elastic_vector_field}') + 1.0",
        #                           "params": {"queryVector": embedding}
        #                       }
        #                   }
        #               }
        #           ]
        #       }
        #   }
        # }

        response = self.es.search(index=self.elastic_index, body=query)

        docs = []
        hits = response["hits"]["hits"]
        for hit in hits:
            # If your document content is stored in e.g. "content" field:
            doc_text = hit["_source"].get("content", "")
            docs.append(doc_text.strip())

        return docs
