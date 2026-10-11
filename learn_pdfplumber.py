import pdfplumber


def extract(path):
    with pdfplumber.open(path) as pdf:
        first_page = pdf.pages[8]
        text = first_page.extract_text()
        return text

def every_text(path):
    all_texts=[]
    with pdfplumber.open(path)as pdf:
        for page in pdf.pages:
            text=page.extract_text()

            if text:
                all_texts.append(text)
    return "\n".join(all_texts)

def get_pdf_info(path):
    with pdfplumber.open(path) as pdf:
        return {
            "page_count" : len(pdf.pages),
            "metadata": pdf.metadata
        }

def extract_tables(path):
    all_table=[]

    with pdfplumber.open(path) as pdf :
        for page_number, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table in tables:
                all_table.append({"page":page_number,
                "data": table})
    return all_table



if __name__ == "__main__":
    result1 = extract("LLM Papers.pdf")
    result2 =every_text("LLM Papers.pdf")
    result3 = extract_tables("LLM Papers.pdf")
    meta = get_pdf_info("LLM Papers.pdf")
tables = extract_tables("LLM Papers.pdf")

print("Tables found:", len(tables))

for table in tables:
    print("Page:", table["page"])
    print(table["data"])
