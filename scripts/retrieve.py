"""Actual DeepTutor BM25 component; no LLM, embeddings or API calls."""
import contextlib,json,sys,time
from pathlib import Path
from types import SimpleNamespace
ROOT=Path(__file__).resolve().parents[1]
def retrieve(query,lessons):
    if not isinstance(query,str) or not query.strip() or len(query)>3000:raise ValueError("Ask a question using 1–3,000 characters.")
    with contextlib.redirect_stdout(sys.stderr):
        from llama_index.core.schema import TextNode
        from llama_index.core.storage.docstore import SimpleDocumentStore
        from deeptutor.services.rag.pipelines.llamaindex.retrievers import build_bm25_retriever
        store=SimpleDocumentStore()
        store.add_documents([TextNode(id_=l["id"],text=l["title"]+"\n"+l["text"]) for l in lessons])
        retriever=build_bm25_retriever(SimpleNamespace(docstore=store),ROOT/".cache/index",top_k=min(3,len(lessons)))
        if retriever is None:raise RuntimeError("Install the documented DeepTutor BM25 requirements.")
        hits=retriever.retrieve(query)
    by_id={l["id"]:l for l in lessons}
    return [{**by_id[h.node.node_id],"score":float(h.score)} for h in hits if h.node.node_id in by_id and (h.score or 0)>0]
if __name__=="__main__":
    payload=json.load(sys.stdin);started=time.perf_counter()
    lessons=json.loads((ROOT/"public/lessons.json").read_text())
    hits=retrieve(payload.get("query"),lessons)
    print(json.dumps({"runtime":"DeepTutor BM25 (actual local component)","hits":hits,"elapsedMs":round((time.perf_counter()-started)*1000,2),"generativeModel":False}))
