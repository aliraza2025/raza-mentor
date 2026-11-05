# Raza Mentor — product case study

## Problem and audience

Learners need to distinguish a source passage from an explanation and check what they understood. The prototype explores a source-first coaching flow connected to Ali’s academic-coaching interests. No interviews or validated learning needs are claimed.

## Role

Independent product design and development by Ali Raza, with AI-assisted implementation. I scoped a verifiable local workflow, selected an upstream component, authored fixtures, built the interface and separated implementation evidence from outcome claims.

## Product decisions

Keep evidence visible beside practice. Preserve exact source text. Abstain on unrelated questions. Track the latest practice result while retaining every attempt. Keep sessions in memory until export. Use local lexical retrieval before attempting generated explanations.

## Implemented and checked

The five original test questions cover four expected sources and one unrelated query requiring no result. Actual retrieval and Opik metric controls were also run while outbound socket connections were blocked. See examples/retrieval-report.json.

## Evidence limits

The public page uses a keyword baseline. Local mode uses DeepTutor’s BM25 component, not its full agent platform. No generative tutor, semantic embeddings, real student records or learning-outcome improvements are claimed.

## Proposed next decision

Test the source-finding and practice flow with consenting learners, then evaluate grounded explanations separately before adding a local generative model.
