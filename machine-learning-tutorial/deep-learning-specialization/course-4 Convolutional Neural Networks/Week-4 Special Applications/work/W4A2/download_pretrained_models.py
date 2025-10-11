#!/usr/bin/env python3
"""
Download required pretrained models for Neural Style Transfer (W4A2)
"""

import os
import urllib.request
from pathlib import Path

def download_vgg19_mat():
    """Download VGG19 MatConvNet model (.mat format)"""
    url = "https://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.svg"
    Path("pretrained-model").mkdir(exist_ok=True)
    filepath = "pretrained-model/imagenet-vgg-verydeep-19.mat"
    
    if os.path.exists(filepath):
        print("✓ VGG19 .mat file already exists")
        return True
    
    try:
        print("Downloading VGG19 MatConvNet model (.mat)...")
        print("This may take a while (328MB file)...")
        urllib.request.urlretrieve(url, filepath)
        print("✓ VGG19 .mat download complete!")
        return True
    except Exception as e:
        print(f"✗ Failed to download VGG19 .mat: {e}")
        return False

def download_vgg19_keras():
    """Download VGG19 Keras weights (.h5 format)"""
    url = "https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
    Path("pretrained-model").mkdir(exist_ok=True)
    filepath = "pretrained-model/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
    
    if os.path.exists(filepath):
        print("✓ VGG19 Keras weights already exist")
        return True
    
    try:
        print("Downloading VGG19 Keras weights (.h5)...")
        print("This may take a while (76MB file)...")
        urllib.request.urlretrieve(url, filepath)
        print("✓ VGG19 Keras weights download complete!")
        return True
    except Exception as e:
        print(f"✗ Failed to download VGG19 Keras weights: {e}")
        return False

def verify_downloads():
    """Verify all files were downloaded successfully"""
    files = [
        "pretrained-model/imagenet-vgg-verydeep-19.mat",
        "pretrained-model/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5"
    ]
    
    print("\n=== Verification ===")
    all_present = True
    for filepath in files:
        if os.path.exists(filepath):
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            print(f"✓ {filepath} ({size_mb:.1f} MB)")
        else:
            print(f"✗ Missing: {filepath}")
            all_present = False
    
    return all_present

if __name__ == "__main__":
    print("=== Downloading Pretrained Models for Week 4 ===")
    print()
    
    success1 = download_vgg19_mat()
    success2 = download_vgg19_keras()
    
    if verify_downloads():
        print("\n✓ All models downloaded successfully!")
        print("You can now run the Week 4 assignments.")
    else:
        print("\n✗ Some downloads failed. Check the errors above.")
        print("\nManual download links:")
        print("• VGG19 .mat: http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat")
        print("• VGG19 .h5: https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5")
