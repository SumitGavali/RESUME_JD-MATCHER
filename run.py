from pdf_utils import extract_pdf
from text_utils import split_in_chunks, clean_text
from matcher import match   


if __name__ =="__main__":
    resume_raw = extract_pdf("Sumit_Gavali_Resume_.pdf")
    jd_raw=open("job_description.txt", encoding="utf-8").read()

    resume_clean=clean_text(resume_raw)
    jd_clean=clean_text(jd_raw)

    resume_chunk =split_in_chunks(resume_clean)
    jd_chunk=split_in_chunks(jd_clean)

    print(f"Resume chunks: {len(resume_chunk)}")
    print(f"JD chunks: {len(jd_chunk)}")

    score , missing , details= match(resume_chunk, jd_chunk)

    print(f"Overall score: {score:.3f}")
    print(f"Missing JD chunks: {len(missing)}")
    print(f"Details: {details}")
    print("--"*5)
    print("Top 5 matches:")
    for i, (jd_chunk, resume_chunk, score) in enumerate(sorted(details, key=lambda x: x[2], reverse=True)[:5]):
        print(f"{i+1}. Score: {score:.3f} | JD chunk: {jd_chunk[:50]:50} | Resume chunk: {resume_chunk[:50]:50}")
