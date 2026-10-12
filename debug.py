from pdf_utils import extract_pdf
from text_utils import split_in_chunks, clean_text

resume_raw = extract_pdf("Sumit_Gavali_Resume_.pdf")
jd_raw = open("job_description.txt", encoding="utf-8").read()

print("=== RESUME RAW ===")
print("length:", len(resume_raw))
print("first 200:", repr(resume_raw[:200]))
print("newline count:", resume_raw.count("\n"))
print("double-newline count:", resume_raw.count("\n\n"))

print("\n=== JD RAW ===")
print("length:", len(jd_raw))
print("first 200:", repr(jd_raw[:200]))
print("newline count:", jd_raw.count("\n"))
print("double-newline count:", jd_raw.count("\n\n"))