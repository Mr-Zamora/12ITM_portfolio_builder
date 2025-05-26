#!/usr/bin/env python3
"""
NESA Stage 6 IT Multimedia Portfolio Builder

This is a simple starter script that runs the Portfolio Builder application.
"""

import os
import sys
import subprocess

def main():
    """Run the Portfolio Builder application."""
    print("Starting NESA Stage 6 IT Multimedia Portfolio Builder...")
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run the application
    try:
        subprocess.run([sys.executable, "-m", "app"], cwd=current_dir)
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nError running the application: {str(e)}")
        print("Please make sure all dependencies are installed.")
        print("You can install them with: pip install -r requirements.txt")
        
    print("\nThank you for using the Portfolio Builder!")

if __name__ == "__main__":
    main()
