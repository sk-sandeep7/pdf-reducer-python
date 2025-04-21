import sys
import numpy as np
from pathlib import Path
from pypdfium2 import PdfDocument

def reduce_pdf_slides(input_path, output_path):
    
    input_pdf = PdfDocument(input_path)
    total_pages = len(input_pdf)
    
   
    keep_indices = []
    prev_pixels = None
    
    for page_num in range(total_pages):
        page = input_pdf.get_page(page_num)
        current_pixels = page.render(scale=0.3, grayscale=True).to_numpy()
        
        if prev_pixels is not None:
            # Check if previous page is fully contained in the current page
            is_redundant = np.all(prev_pixels >= current_pixels)
            if not is_redundant:
                keep_indices.append(page_num - 1)
        
        prev_pixels = current_pixels
    
    keep_indices.append(total_pages - 1)
    
    # Create new PDF with non-redundant pages
    output_pdf = PdfDocument.new()
    output_pdf.import_pages(input_pdf, keep_indices)
    output_pdf.save(output_path)
    print(f"Reduced {total_pages}-page PDF to {len(keep_indices)} pages. Saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please ensure the follwing syntax: python reduce_pdf_slides.py input.pdf output.pdf")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    reduce_pdf_slides(input_path, output_path)