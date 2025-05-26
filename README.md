# NESA Stage 6 IT Multimedia Portfolio Builder

A comprehensive tool for students to create, manage, and submit their IT Multimedia portfolios for the NESA Stage 6 curriculum.

## Features

- Interactive questionnaire for Statement of Intent creation
- Support for multiple portfolio stages (Stage 1, 2, etc.)
- AI-assisted content generation using Gemini API
- Student response management
- Version control for portfolio documents
- Command-line interface

## Project Structure

```
nesa-portfolio-builder/
├── app/                           # Main application package
│   ├── __init__.py               # Package initialization
│   ├── __main__.py               # Command-line entry point
│   ├── app_config.py             # Configuration and paths
│   ├── interactive_questionnaire.py  # Main questionnaire logic
│   └── utils/                    # Utility modules
│       ├── __init__.py
│       ├── gemini_utils.py       # Gemini API integration
│       └── generate_statement_prompt.py  # Prompt generation
├── data/                         # Application data
│   ├── generated/                # Generated portfolio documents
│   ├── responses/                # Student response files
│   └── students/                 # Student-specific data
├── templates/                    # Document templates
│   ├── AI_TEMPLATE.md            # AI template
│   ├── QS_STATEMENT_OF_INTENT.md # Question template
│   ├── statement_template.md     # Statement template
│   └── stage_template.md         # Stage template
├── .env.example                  # Example environment variables
├── CHANGELOG.md                  # Project changelog
├── README.md                     # This file
├── requirements.txt              # Python dependencies
└── setup.py                     # Package installation script
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nesa-portfolio-builder
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

## Usage

### Starting the Questionnaire

```bash
# Start a new portfolio
python -m app

# Or use the installed command
nesa-portfolio
```

### Working with Existing Portfolios

```bash
# List all student portfolios
nesa-portfolio --list-students

# Work with a specific student's portfolio
nesa-portfolio --student-id STUDENT_ID
```

### Development

To run tests:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NESA for the Stage 6 IT Multimedia curriculum
- Google for the Gemini API
- The open-source community for valuable tools and libraries
