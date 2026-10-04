# Ship 3 — IBM Granite Standard RAG Pipeline — Local

**The ship that proved the pattern was portable — without ever touching the cloud it was never going to use.**

Ship 3 of A Mirror of My Becoming™. Built August–September 2026 on an 8 GB Intel MacBook Air. Runs fully local: IBM Granite 4.1 (3B) as the LLM and nomic-embed-text for embeddings, both served through Ollama. No cloud account, no API key, no data leaving the machine.

**Author:** Evelyn Caro

---

## What it does

Standard RAG, end to end, in one script:

1. Loads documents (`data/CURATED_PUBLIC_DATA.md` — deliberately public data, which is why this repo can be public)
2. Chunks them — 500 characters, 50 overlap
3. Embeds every chunk locally through nomic-embed-text
4. Persists chunks + embeddings into a local Chroma vector store (`./chroma_db`)
5. Answers questions by retrieving the top relevant chunks and passing them to Granite 4.1 for generation

First run builds the store. Every run after that loads it. Docker and docker-compose files are included for the same behavior in a container.

---

## Why it exists

Ship 1 ran on AWS and was lost to AWS. Ship 3 asked the next question: **whose model?** DeepSeek 1.5B runs through Ollama, but the fleet needed a second model to prove the pattern wasn't locked to one. IBM Granite 4.1 (3B) is small enough to run on consumer hardware and open enough to run anywhere. The answer: swap the model, keep the pattern, prove it end to end — locally. Ship 3 is the receipt that the RAG pattern was never locked to a vendor — model or platform.

---

## Requirements

- Python 3 with: `langchain`, `langchain-community`, `langchain-text-splitters`, `langchain-ollama`, `langchain-chroma`
- [Ollama](https://ollama.com) running locally, with `granite4.1:3b` and `nomic-embed-text` pulled
- `data/CURATED_PUBLIC_DATA.md` — your own corpus, in one markdown file

---

## Quickstart

1. Install the packages named at the top of Ship3_IBM_Granite_RAG_demo.py
2. Pull the models: ollama pull granite4.1:3b && ollama pull nomic-embed-text
3. Put your corpus in data/CURATED_PUBLIC_DATA.md
4. Run: python3 Ship3_IBM_Granite_RAG_demo.py
First run builds the store. Every run after loads it.
text


---


---

## The fleet

- **[Ship 1](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship1-deepseek-rag-local)** — DeepSeek RAG, rebuilt local after AWS lost the original
- **[Ship 2](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship2-ibm-granite-agentic)** — IBM Granite Agentic RAG
- **[Ship 3](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship3-ibm-granite)** — IBM Granite Standard RAG
- **[Ship 4](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship4-ibm-granite-agentic)** — IBM Granite Agentic RAG
- **[Ship 5](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship5-ibm-granite-agentic-evidenceflow)** — IBM Granite Agentic RAG with EvidenceFlow

**[Suite: Ingestion Tools](https://github.com/qaevelyn/a-mirror-of-my-becoming-suite-ingestion-tools)** — the tooling that gets documents into the vector stores these ships read from.

**[A Mirror of My Becoming™](https://github.com/qaevelyn/a-mirror-of-my-becoming)** — the parent index for the entire practice.

**[Fleet index + SETUP.md](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-pipelines)** — how to point any ship at your own corpus.

---


## License

Dual-licensed:

- **AGPL-3.0** — free to use, modify, and redistribute under the terms of the license. Full text in [LICENSE](LICENSE).
- **Commercial license** — available for organizations that need to use the code without the AGPL-3.0 obligations. Contact the author for pricing.

Free does not mean free to exploit. If you build a product on this work, the author expects to be paid.

---

## Author

**Evelyn Caro** — Sovereign AI Builder.

**[qaevelyn.github.io](https://qaevelyn.github.io)** · Commercial licensing: **evelyn.caro.cloud@gmail.com**

---

© 2026 Evelyn Caro. All rights reserved.
