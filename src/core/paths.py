# src/core/paths.py
"""
    This file defines the paths used in the program.
"""
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
src_dir = os.path.join(root_dir, "src")
core_dir = os.path.join(src_dir, "core")
image_dir = os.path.join(src_dir, "images")
font_dir = os.path.join(src_dir, "fonts")
