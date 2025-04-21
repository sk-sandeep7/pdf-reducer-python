# 🐍 PDF Reducer Python

Did you face a problem where exporting your animated PowerPoint to a PDF created tons of nearly identical pages — one for every animation or click? Yeah, we've been there.

This script helps you automatically clean up those extra pages and reduce your PDF to only the unique, final slides. 

## 📦 Features
- Removes duplicate or nearly-identical pages caused by PowerPoint animations
- Keeps only visually distinct slides
- Lightweight and easy to use

## 🛠 Requirements
Install required Python packages with:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
```bash
python reduce_pdf_slides.py input_path.pdf output_path.pdf
```
- `input_path.pdf`: Path to your exported PowerPoint PDF
- `output_path.pdf`: Path where the cleaned-up PDF will be saved

## 📝 Example
```bash
python reduce_pdf_slides.py stats_lecture.pdf stats_clean.pdf
```

## 💡 How It Works
The script compares pages visually to detect and remove pages that are nearly the same — just like those added by animations like "appear on click."

## ✍️ Why I Made This
This whole thing started when my Probability and Statistics professor uploaded a PDF of her PowerPoint slides.

The file had around 60 pages, but while flipping through it, I realized only about 15 slides were actually different. The rest were just the same slides repeated with one extra bullet point, thanks to the animations from the original PowerPoint.

It was frustrating to read, hard to take notes on, and felt like a waste of scrolling time.

So I built this script to automatically clean it up — and make PDFs like that way easier to read and review.

I will work on making this a web app to make this tool more accessible.

## 📄 License
MIT — free to use, modify, and share.

Just don’t ask it to bring your animations back 😅
```
