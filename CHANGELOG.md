# Changelog

All notable changes to the NESA Stage 6 IT Multimedia Portfolio Builder will be documented in this file.

## [1.0.0] - 2025-05-27

### Added
- Reorganized project structure for better maintainability and scalability
- Created directory structure: app/, data/, templates/, static/, utils/, docs/, examples/, tests/
- Added menu-driven interface with options for new questionnaire, loading responses, and listing resources
- Implemented user-friendly file naming with snake_case project titles
- Added support for multiple portfolio stages and student-specific data
- Created simple start.py script for easy application launching
- Added API key integration from .env file
- Enhanced statement generation with Australian spelling and community college voice
- Added "Press ENTER to return to main menu" prompts for better user experience
- Created rename_files.py script to update existing files to new naming convention

### Changed
- Moved all application code to the app/ directory
- Updated file paths in app_config.py to reflect new structure
- Modified interactive_questionnaire.py to work with the new package structure
- Updated imports to work with the new directory structure
- Enhanced the README with comprehensive project information and usage instructions
- Improved error handling in Gemini API integration

### Fixed
- Fixed Unicode encoding issues in test scripts
- Resolved file path issues for statement_intent_schema.json
- Fixed variable name mismatch in statement generation (statement_path vs output_file)
- Added proper handling for Gemini response objects
- Fixed missing save_and_generate method in InteractiveQuestionnaire class

## [0.1.0] - 2025-05-25

### Added
- Initial version of the Portfolio Builder
- Basic questionnaire functionality
- Integration with Gemini API for statement generation
- Simple file saving and loading
