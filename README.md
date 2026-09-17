# Ship 3: IBM Granite RAG Pipeline

**Built:** August 2026
**Author:** Evelyn Caro
**Status:** ✅ Built and working

**Naming note:** The runnable file is `Ship3_IBM_Granite_RAG_demo.py`. The notebook `Ship3_IBM_Granite_RAG_v1.ipynb` is preserved as the source of record. Both run the same pipeline. Ship 3 began as a copy of the Ship 2 IBM Granite notebook and was adapted for a different purpose — proving the pattern could cross platforms.

---

## Origin

The third ship proved the pattern could cross platforms.

If the architecture only worked on one vendor's model, it wasn't sovereign. Ship 3 ran 
the same RAG pattern on IBM Granite — a different LLM, a different vendor, the same 
local-first philosophy. This is where "sovereign" stopped being a slogan and started 
being a design constraint.

---

## What It Does

A Retrieval-Augmented Generation (RAG) pipeline built on IBM Granite, demonstrating 
cross-platform AI capabilities.

---

## Architecture

- **Runtime:** Local, sovereign execution
- **Model:** IBM Granite
- **Pipeline:** RAG
- **Data source:** Local files — the Mirror personal archive
- **Storage:** Vector database
- **Cloud dependency:** None (current)

---

## Pipeline

1. Read local documents from the Mirror archive
2. Chunk into pieces
3. Vectorize (embed) each chunk
4. Store vectors in a vector database
5. Query at runtime → retrieve relevant chunks → generate answer

---

## Integration

- Reads local data — the Mirror personal archive
- Chunks, vectorizes, stores in vector DB
- Queries the DB at runtime for retrieval-augmented answers
- **No cloud dependency.** Local-first. Sovereign.
- Demonstrates the pattern working on a second LLM vendor.

---

## Access and Copyright

This work was created by Evelyn Caro. DeepSeek is the only collaborator — used as a tool 
in the creative and technical process.

This is a personal portfolio project and is not open for collaboration or external access. 
The video and documentation speak for themselves.

Copyright © 2026 Evelyn Caro. All rights reserved. Copyright registration is pending.
