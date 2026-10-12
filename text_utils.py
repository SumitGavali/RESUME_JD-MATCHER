import re 

# All the bullet characters that show up in real PDFs/JDs.
# \uf0b7 is the Wingdings bullet — YOUR resume uses this.
BULLET_CHARS = r"[•\u2022\u25CF\u25AA\u2023\u2043\uf0b7\-\*]"

def clean_text(text:str)->str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
     # why two removes because some PDFs use \r\n and some use \r. We want to standardize to \n.
    text=re.sub(r"[ \t]+"," ", text) #removing extra spaces
    text = re.sub(r"\n{3,}", "\n\n", text)
    text="\n".join(line.strip() for line in text.split("\n")) #removing extra spaces at the beginning and end of each line
    return text.strip()

def split_in_chunks(text:str, chunk_size:int=30)->list[str]:
    if not (text and text.strip()): return []

    # 1. Normalize all bullets to " \n• "
    text = re.sub(rf"\s*{BULLET_CHARS}\s*", "\n• ", text)

    # 2. Normalize numbered lists: "1. " or "1) " at line start
    text = re.sub(r"\n\s*(\d+)[\.\)]\s+", r"\n• ", text)

    raw_parts = re.split(r"\n\s*\n|\n", text)

    chunks = []
    for part in raw_parts:
        part=part.strip()
        part=re.sub(rf"^{BULLET_CHARS}\s*", "", part).strip() # remove leading bullet if any

        if not part:
            continue

        if len(part) < chunk_size:
            continue
          # WHY: Short fragments like "EXPERIENCE", "Skills:", "2019-2023" carry
        #      little semantic value for embeddings — they add noise.

        if len(part) > 400:
            for s in re.split(r"(?<=[.!?])\s+", part):
                s = s.strip()
                if len(s) >= chunk_size:
                    chunks.append(s)

        else:
            chunks.append(part)
    seen=set()
    unique=[]
    for c in chunks:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    return unique