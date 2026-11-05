# Raza Mentor

**Source-grounded study and practice · Raza Labs by Ali Raza**

![Original concept artwork](public/project-cover.webp)

An original study workbench with source-linked passages, practice questions, review tracking and session exports, using an actual local DeepTutor BM25 retrieval component.

[Working browser demo](https://aliraza2025.github.io/raza-mentor/) · [Product case study](CASE_STUDY.md) · [Portfolio](https://alirazaai.page/projects#ai-labs)

## What works

The local adapter imports build_bm25_retriever from DeepTutor and builds an in-memory LlamaIndex document store using the four original lessons. It returns original passages with source IDs. The native DeepTutor agent, model provider, embedding pipeline and web platform are not used. The browser keyword baseline is a separate implementation.

## Run locally

Requires Node.js 22+ and Python 3.11–3.13. No paid API or cloud account is needed.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm test
npm run build
RAZA_PYTHON="$PWD/.venv/bin/python" npm start
```

The public directory is source; docs is generated GitHub Pages output. The web server is loopback-only and serves a fixed asset allowlist.

## Verification

The five original test questions cover four expected sources and one unrelated query requiring no result. Actual retrieval and Opik metric controls were also run while outbound socket connections were blocked. See examples/retrieval-report.json.

## Ownership and upstream credit

Ali Raza’s original contribution is the product workflow, interface, source fixtures, adapters, tests and evaluation framing, with AI-assisted implementation. The upstream engine is [DeepTutor](https://github.com/HKUDS/DeepTutor), installed separately under its own license. This repository does not claim authorship of that engine or affiliation with its maintainers. Original project code is MIT-licensed. No private employer code, student records or customer data are included.

## Limits

The public page uses a keyword baseline. Local mode uses DeepTutor’s BM25 component, not its full agent platform. No generative tutor, semantic embeddings, real student records or learning-outcome improvements are claimed.

## Next validation

Test the source-finding and practice flow with consenting learners, then evaluate grounded explanations separately before adding a local generative model.
