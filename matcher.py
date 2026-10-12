import numpy as np
from sentence_transformers import SentenceTransformer
import sklearn 

_model=None #this means we have to load model only once.
def get_model():
    global _model
    if _model is None:
        _model=SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def cosine_sim(a,b):
    return float(np.dot(a,b)/(np.linalg.norm(a))*(np.linalg.norm(b)))

def match(resume_chunks,jd_chunks, threshold=0.5):
    model=get_model()
    resume_embs=model.encode(resume_chunks,normalize_embeddings=True)
      # WHY: Convert resume text chunks to vectors. Normalize so cosine = dot product
      # HOW: encode() handles batching internally; returns shape (N_resume, 384).
    jd_embs=model.encode(jd_chunks,normalize_embeddings=True)
    sim_matrix = jd_embs @ resume_embs.T
    # WHY: Matrix multiply of normalized vectors gives ALL pairwise cosine sims.
    #      Shape: (N_jd, N_resume). This is the "how" — one vectorized op, not a loop.
    # HOW: (N_jd,384) @ (384,N_resume) → (N_jd, N_resume).
    best_idx=sim_matrix.argmax(axis=1)
    best_scores = sim_matrix.max(axis=1)
     # WHY: The actual similarity value of that best match.
    # HOW: max along axis=1 → shape (N_jd,).
    overall=float(best_scores.mean())
    missing , details =[],[]
    for i , jd_chunk in enumerate(jd_chunks):
        score=float(best_scores[i])
        resume_chunk=resume_chunks[best_idx[i]]
          # WHY: Fetch the actual resume text (not just its index) for the report.
        details.append((jd_chunk, resume_chunk, score))

        if score<threshold:
            missing.append(jd_chunk)
    return overall , missing , details