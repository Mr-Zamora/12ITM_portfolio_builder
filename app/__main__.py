#!/usr/bin/env python3
"""
NESA Stage 6 IT Multimedia Portfolio Builder

This is the main entry point for the Portfolio Builder application.
It provides a command-line interface for students to work on their portfolio.
"""

import argparse
import sys
import json
import os
from pathlib import Path

from app.interactive_questionnaire import InteractiveQuestionnaire
from app.app_config import RESPONSES_DIR, GENERATED_DIR

def main():
    """Main entry point for the Portfolio Builder application."""
    parser = argparse.ArgumentParser(
        description="NESA Stage 6 IT Multimedia Portfolio Builder"
    )
    
    # Create a subparser for different commands
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # New questionnaire command
    new_parser = subparsers.add_parser('new', help='Start a new questionnaire')
    new_parser.add_argument(
        '--student-id',
        help='Student ID for the new questionnaire',
        default=None
    )
    
    # Load existing responses command
    load_parser = subparsers.add_parser('load', help='Load existing responses')
    load_parser.add_argument(
        '--responses-file',
        help='Path to the responses file to load',
        type=str
    )
    load_parser.add_argument(
        '--student-id',
        help='Student ID to load responses for',
        type=str
    )
    
    # List command
    list_parser = subparsers.add_parser('list', help='List available resources')
    list_parser.add_argument(
        '--students',
        action='store_true',
        help='List all student portfolios'
    )
    list_parser.add_argument(
        '--responses',
        action='store_true',
        help='List all response files'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command specified, show a menu of options
    if not args.command:
        print("\nNESA Stage 6 IT Multimedia Portfolio Builder")
        print("-" * 50)
        print("Please select an option:")
        print("1. Start a new questionnaire")
        print("2. Load existing responses")
        print("3. List available resources")
        print("4. Exit")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-4): ")
                
                if choice == '1':
                    args.command = 'new'
                    args.student_id = None
                    break
                elif choice == '2':
                    args.command = 'load'
                    # Initialize attributes for the 'load' command
                    args.responses_file = None
                    args.student_id = None
                    break
                elif choice == '3':
                    args.command = 'list'
                    # Initialize attributes for the 'list' command
                    args.students = True
                    args.responses = True
                    # Show both students and responses
                    list_response_files()
                    print("\n")
                    list_student_portfolios()
                    # Return to main menu
                    input("\nPress ENTER to return to the main menu...")
                    main()  # Restart the main function to show the menu again
                    return
                elif choice == '4':
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\nExiting...")
                return
    
    # Handle commands
    if args.command == 'list':
        if args.students:
            list_student_portfolios()
        elif args.responses:
            list_response_files()
        else:
            # Default to listing both
            list_response_files()
            print("\n")
            list_student_portfolios()
        # Return to main menu
        input("\nPress ENTER to return to the main menu...")
        main()  # Restart the main function to show the menu again
        return
    
    elif args.command == 'load':
        # Load existing responses
        if args.responses_file:
            responses_path = Path(args.responses_file)
        elif args.student_id:
            # Find responses file for student ID
            responses_path = find_responses_for_student(args.student_id)
        else:
            # List available response files and prompt user to select one
            responses_path = select_responses_file()
        
        if responses_path and responses_path.exists():
            # Run questionnaire with loaded responses
            questionnaire = InteractiveQuestionnaire()
            questionnaire.load_responses_from_file(responses_path)
            questionnaire.run()
        else:
            print(f"Error: Could not find responses file.")
            return
    
    else:  # 'new' command
        # Run the interactive questionnaire
        questionnaire = InteractiveQuestionnaire(student_id=args.student_id)
        questionnaire.run()

def list_student_portfolios():
    """List all student portfolios in the data directory."""
    print("\nAvailable student portfolios:")
    print("-" * 40)
    
    students = []
    for student_dir in GENERATED_DIR.glob('*'):
        if student_dir.is_dir():
            student_id = student_dir.name
            statements = list(student_dir.glob('statement_of_intent_*.md'))
            students.append({
                'id': student_id,
                'statements': len(statements),
                'latest': max(statements).name if statements else 'No statements'
            })
    
    if not students:
        print("No student portfolios found.")
        return
    
    # Sort by student ID
    students.sort(key=lambda x: x['id'], reverse=True)
    
    # Print table
    print(f"{'Student ID':<20} {'Statements':<12} Latest File")
    print("-" * 60)
    for student in students:
        print(f"{student['id']:<20} {student['statements']:<12} {student['latest']}")
    print()
    
    return students

def list_response_files():
    """List all response files in the responses directory."""
    print("\nAvailable response files:")
    print("-" * 40)
    
    responses = []
    for response_file in RESPONSES_DIR.glob('*.json'):
        if response_file.is_file():
            # Try to load the file to get student info
            try:
                with open(response_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Check if it's the new format with metadata
                    if isinstance(data, dict) and 'student_id' in data:
                        student_id = data['student_id']
                        timestamp = data.get('timestamp', 'Unknown')
                        responses.append({
                            'file': response_file,
                            'student_id': student_id,
                            'timestamp': timestamp,
                            'size': response_file.stat().st_size
                        })
                    else:
                        # Old format without metadata
                        responses.append({
                            'file': response_file,
                            'student_id': 'Unknown',
                            'timestamp': response_file.stat().st_mtime,
                            'size': response_file.stat().st_size
                        })
            except (json.JSONDecodeError, IOError):
                # If we can't read the file, just show basic info
                responses.append({
                    'file': response_file,
                    'student_id': 'Unknown (Error reading file)',
                    'timestamp': response_file.stat().st_mtime,
                    'size': response_file.stat().st_size
                })
    
    if not responses:
        print("No response files found.")
        return []
    
    # Sort by timestamp (newest first)
    responses.sort(key=lambda x: x['timestamp'] if isinstance(x['timestamp'], (int, float)) else 0, reverse=True)
    
    # Print table
    print(f"{'#':<3} {'Student ID':<20} {'File':<30} {'Size':<10}")
    print("-" * 65)
    for i, response in enumerate(responses, 1):
        filename = response['file'].name
        size_kb = response['size'] / 1024
        print(f"{i:<3} {response['student_id']:<20} {filename:<30} {size_kb:.1f} KB")
    print()
    
    return responses

def select_responses_file():
    """Prompt the user to select a response file from the available options."""
    responses = list_response_files()
    
    if not responses:
        return None
    
    while True:
        try:
            choice = input("\nEnter the number of the response file to load (or 'q' to quit): ")
            
            if choice.lower() == 'q':
                return None
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(responses):
                return responses[choice_num - 1]['file']
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(responses)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def find_responses_for_student(student_id):
    """Find the most recent response file for a given student ID."""
    # Look for response files matching the student ID pattern
    matching_files = list(RESPONSES_DIR.glob(f'*{student_id}*.json'))
    
    if not matching_files:
        print(f"No response files found for student ID: {student_id}")
        return None
    
    # Sort by modification time (newest first)
    matching_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    # Return the most recent file
    return matching_files[0]

if __name__ == "__main__":
    main()
