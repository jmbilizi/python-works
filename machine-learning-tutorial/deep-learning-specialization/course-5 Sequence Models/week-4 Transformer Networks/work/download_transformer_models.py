"""
Download script for HuggingFace transformer models and GloVe embeddings
Required for Week-4 Transformer Networks assignments
"""

import os
import urllib.request
import zipfile
from transformers import (
    DistilBertTokenizerFast, 
    TFDistilBertForTokenClassification,
    TFDistilBertForQuestionAnswering,
    DistilBertForQuestionAnswering
)

def download_models():
    """
    Download HuggingFace DistilBERT models, tokenizers, and GloVe embeddings for the assignments.
    
    Downloads the models to the appropriate directories:
    - W4A2_UGL: Named Entity Recognition model
    - W4A3_UGL: Question Answering models (TensorFlow and PyTorch)
    - W4A4_UGL_POS: GloVe 100d embeddings for positional encoding
    """
    
    print("HuggingFace Transformer Models + GloVe Embeddings Download Script")
    print("=" * 65)
    print("This script downloads all required models for Week-4 assignments:")
    print("- DistilBERT models from HuggingFace model hub")
    print("- GloVe 6B 100d embeddings from Stanford NLP")
    print("=" * 65)
    
    # W4A2 - Named Entity Recognition
    print("\n1. Downloading DistilBERT for Named Entity Recognition (W4A2)...")
    w4a2_model_dir = "W4A2_UGL/model"
    w4a2_tokenizer_dir = "W4A2_UGL/tokenizer"
    
    os.makedirs(w4a2_model_dir, exist_ok=True)
    os.makedirs(w4a2_tokenizer_dir, exist_ok=True)
    
    try:
        # Download tokenizer for W4A2
        tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
        tokenizer.save_pretrained(w4a2_tokenizer_dir)
        print(f"  ✓ Tokenizer saved to {w4a2_tokenizer_dir}")
        
        # Download model for W4A2 (we'll download with default num_labels, can be modified later)
        model = TFDistilBertForTokenClassification.from_pretrained('distilbert-base-uncased')
        model.save_pretrained(w4a2_model_dir)
        print(f"  ✓ NER Model saved to {w4a2_model_dir}")
        
    except Exception as e:
        print(f"  ✗ Error downloading W4A2 models: {e}")
    
    # W4A3 - Question Answering
    print("\n2. Downloading DistilBERT for Question Answering (W4A3)...")
    w4a3_model_tf_dir = "W4A3_UGL/model/tensorflow"
    w4a3_model_pt_dir = "W4A3_UGL/model/pytorch"
    w4a3_tokenizer_dir = "W4A3_UGL/tokenizer"
    
    os.makedirs(w4a3_model_tf_dir, exist_ok=True)
    os.makedirs(w4a3_model_pt_dir, exist_ok=True)
    os.makedirs(w4a3_tokenizer_dir, exist_ok=True)
    
    try:
        # Download tokenizer for W4A3
        tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-distilled-squad')
        tokenizer.save_pretrained(w4a3_tokenizer_dir)
        print(f"  ✓ Tokenizer saved to {w4a3_tokenizer_dir}")
        
        # Download TensorFlow model for W4A3
        tf_model = TFDistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
        tf_model.save_pretrained(w4a3_model_tf_dir)
        print(f"  ✓ TensorFlow QA Model saved to {w4a3_model_tf_dir}")
        
        # Download PyTorch model for W4A3
        pt_model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
        pt_model.save_pretrained(w4a3_model_pt_dir)
        print(f"  ✓ PyTorch QA Model saved to {w4a3_model_pt_dir}")
        
    except Exception as e:
        print(f"  ✗ Error downloading W4A3 models: {e}")
    
    # W4A4 - GloVe Embeddings
    print("\n3. Downloading GloVe embeddings for Positional Encoding (W4A4)...")
    w4a4_glove_dir = "W4A4_UGL_POS/glove"
    
    os.makedirs(w4a4_glove_dir, exist_ok=True)
    
    glove_file_path = os.path.join(w4a4_glove_dir, "glove.6B.100d.txt")
    
    if os.path.exists(glove_file_path):
        print(f"  ✓ GloVe embeddings already exist at {glove_file_path}")
    else:
        try:
            print("  Downloading GloVe 6B embeddings (this may take a while - ~862MB)...")
            url = "https://nlp.stanford.edu/data/glove.6B.zip"
            zip_filename = "glove.6B.zip"
            
            urllib.request.urlretrieve(url, zip_filename)
            print("  Download completed, extracting...")
            
            # Extract only the 100d embeddings
            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extract("glove.6B.100d.txt")
            
            # Move to correct location
            import shutil
            shutil.move("glove.6B.100d.txt", glove_file_path)
            
            # Clean up
            os.remove(zip_filename)
            
            print(f"  ✓ GloVe embeddings saved to {glove_file_path}")
            
        except Exception as e:
            print(f"  ✗ Error downloading GloVe embeddings: {e}")
            # Clean up on error
            if os.path.exists(zip_filename):
                os.remove(zip_filename)
            if os.path.exists("glove.6B.100d.txt"):
                os.remove("glove.6B.100d.txt")
    
    print("\n" + "=" * 50)
    print("Download completed!")
    print("\nNote: If you encounter any issues:")
    print("1. Make sure you have transformers library installed: pip install transformers")
    print("2. Make sure you have tensorflow installed: pip install tensorflow")
    print("3. Make sure you have torch installed: pip install torch")
    print("4. You may need to run this script from the week-4 work directory")

def check_requirements():
    """Check if required libraries are installed"""
    try:
        import transformers
        import tensorflow
        print(f"✓ transformers version: {transformers.__version__}")
        print(f"✓ tensorflow version: {tensorflow.__version__}")
        
        try:
            import torch
            print(f"✓ torch version: {torch.__version__}")
        except ImportError:
            print("⚠ torch not found - PyTorch models may not work")
            
        return True
    except ImportError as e:
        print(f"✗ Missing required library: {e}")
        print("Please install required packages:")
        print("pip install transformers tensorflow torch")
        return False

if __name__ == "__main__":
    print("Checking requirements...")
    if check_requirements():
        print("\nAll requirements satisfied!")
        response = input("\nDo you want to proceed with downloading models? (y/n): ")
        if response.lower() in ['y', 'yes']:
            download_models()
        else:
            print("Download cancelled.")
    else:
        print("\nPlease install missing requirements before running this script.")