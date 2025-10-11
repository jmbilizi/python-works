"""
Download script for GloVe pre-trained word embeddings
Required for Week-2 NLP and Words Embeddings assignments
"""

import os
import urllib.request
import zipfile

def download_glove_embeddings():
    """
    Download GloVe 6B 50d word embeddings for the assignments.
    
    Downloads the embeddings from Stanford NLP group and extracts
    the required glove.6B.50d.txt file to both W2A1/data/ and W2A2/data/
    """
    
    # Create data directories if they don't exist
    w2a1_data_dir = "W2A1/data"
    w2a2_data_dir = "W2A2/data"
    
    os.makedirs(w2a1_data_dir, exist_ok=True)
    os.makedirs(w2a2_data_dir, exist_ok=True)
    
    # Check if files already exist
    w2a1_glove_path = os.path.join(w2a1_data_dir, "glove.6B.50d.txt")
    w2a2_glove_path = os.path.join(w2a2_data_dir, "glove.6B.50d.txt")
    
    if os.path.exists(w2a1_glove_path) and os.path.exists(w2a2_glove_path):
        print("GloVe embeddings already exist in both directories.")
        return
    
    # Download the zip file
    url = "https://nlp.stanford.edu/data/glove.6B.zip"
    zip_filename = "glove.6B.zip"
    
    print("Downloading GloVe embeddings (this may take a while - ~862MB)...")
    try:
        urllib.request.urlretrieve(url, zip_filename)
        print("Download completed.")
    except Exception as e:
        print(f"Error downloading file: {e}")
        return
    
    # Extract the specific file we need
    print("Extracting glove.6B.50d.txt...")
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            # Extract only the 50d embeddings
            zip_ref.extract("glove.6B.50d.txt")
            
        # Copy to both assignment directories
        import shutil
        shutil.copy("glove.6B.50d.txt", w2a1_glove_path)
        shutil.copy("glove.6B.50d.txt", w2a2_glove_path)
        
        # Clean up
        os.remove("glove.6B.50d.txt")
        os.remove(zip_filename)
        
        print("GloVe embeddings successfully installed in both W2A1/data/ and W2A2/data/")
        
    except Exception as e:
        print(f"Error extracting file: {e}")
        # Clean up on error
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
        if os.path.exists("glove.6B.50d.txt"):
            os.remove("glove.6B.50d.txt")

if __name__ == "__main__":
    print("GloVe Embeddings Download Script")
    print("=" * 40)
    print("This script downloads GloVe 6B 50d word embeddings")
    print("required for Week-2 NLP assignments.")
    print("File size: ~862MB download, ~171MB per extracted file")
    print("=" * 40)
    
    response = input("Do you want to proceed with the download? (y/n): ")
    if response.lower() in ['y', 'yes']:
        download_glove_embeddings()
    else:
        print("Download cancelled.")