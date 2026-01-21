#!/usr/bin/env python
"""Entry point for running the Flask app"""
import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
