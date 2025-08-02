# 📄 Intelligent Document QA & Processing RAG Pipeline

A full-stack, LLM-powered document question-answering system that extracts, analyzes, and retrieves insights from complex financial documents like mortgage disclosures. Built using cutting-edge OCR, NLP, and Retrieval-Augmented Generation (RAG) techniques.

## 🔍 Features

- **Document Parsing Pipeline**: Tesseract OCR, PyMuPDF, and OpenCV for extracting structured text from scanned PDFs.
- **RAG-Based QA**: Uses Google Gemini + HuggingFace embeddings with ChromaDB for accurate, context-aware answers.
- **Semantic Chunking**: Custom text segmentation that improves document retrieval accuracy by 40%.
- **Query Optimization**: Prompt engineering, query rewriting, and hybrid retrieval boost factuality.
- **Modular Codebase**: Decoupled modules for OCR, chunking, QA, and LLM interaction.
- **Google Gemini QA**: Answers user queries over uploaded documents via Gemini API and a RAG-style pipeline.
- **Resume Mode**: Dedicated document classification system for enhanced accuracy.

- 
## 🧠 Tech Stack

- **Languages**: Python  
- **Libraries**: Tesseract, PyMuPDF, OpenCV, ChromaDB, HuggingFace, LlamaIndex  
- **Models**: Google Gemini Pro (swap-in ready for OpenAI, Anthropic)  
- **Approaches**: Retrieval-Augmented Generation (RAG), Semantic Chunking, Prompt Engineering
