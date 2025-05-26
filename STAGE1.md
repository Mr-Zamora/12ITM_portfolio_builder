# Stage 1: Core Application Framework

## Objective
Set up the foundational structure of the NESA Portfolio Builder with basic navigation and responsive design.

## Technical Specifications

### 1. File Structure
```
12ITM_portfolio_builder/
│
├── app/                           # Main application package
│   ├── __init__.py                # Application factory and extensions
│   ├── config.py                  # Configuration settings
│   │
│   ├── routes/                    # Route definitions
│   │   ├── __init__.py
│   │   ├── auth.py               # Authentication routes (placeholder)
│   │   └── portfolio.py         # Portfolio section routes
│   │
│   ├── static/                    # Static files
│   │   ├── css/
│   │   │   ├── main.css         # Main stylesheet
│   │   │   └── mobile.css        # Mobile-specific styles
│   │   ├── js/
│   │   │   ├── main.js          # Main JavaScript
│   │   │   └── navigation.js     # Navigation logic
│   │   └── images/              # Image assets
│   │
│   ├── templates/                 # Jinja2 templates
│   │   ├── base.html            # Base template
│   │   ├── components/          # Reusable components
│   │   │   ├── header.html
│   │   │   ├── footer.html
│   │   │   └── navigation.html
│   │   └── sections/            # Section templates
│   │       ├── index.html       # Landing page
│   │       ├── statement.html    # Statement of Intent
│   │       └── research/        # Research section
│   │
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── session_manager.py    # Session management
│
├── tests/                        # Test files
│   ├── __init__.py
│   └── test_routes.py
│
├── .env                         # Environment variables
├── .gitignore
├── requirements.txt              # Python dependencies
└── run.py                       # Application entry point
```

### 2. Dependencies (requirements.txt)
```
Flask==2.3.3
python-dotenv==1.0.0
Werkzeug==2.3.7
Jinja2==3.1.2
itsdangerous==2.1.2
click==8.1.7
```

## Implementation Details

### 1. Application Factory (app/__init__.py)
- Initialize Flask application
- Configure secret key
- Register blueprints
- Initialize extensions
- Setup session management

### 2. Configuration (app/config.py)
- Base configuration class
- Development/Production settings
- Session configuration
- API endpoints

### 3. Routes (app/routes/portfolio.py)
- Define route for each main section:
  - /statement
  - /research
  - /selection
  - /development
  - /management
  - /evaluation
- Handle session management
- Basic error handling

### 4. Templates

#### base.html
- HTML5 structure
- Responsive meta tags
- Navigation include
- Content block
- Mobile menu toggle
- Footer include

#### navigation.html
- Main navigation menu
- Mobile menu
- Active state indicators
- Section progress indicators

### 5. Static Files

#### main.css
- CSS variables for theming
- Base typography
- Layout utilities
- Responsive breakpoints
- Animation keyframes

#### main.js
- Mobile menu toggle
- Smooth scrolling
- Session management helpers
- Event listeners

## Testing Requirements

### 1. Unit Tests (tests/test_routes.py)
- Test route accessibility
- Session management
- Error handling
- Response codes

### 2. Manual Testing
- [ ] Navigation works on mobile/desktop
- [ ] Session persists on page refresh
- [ ] All sections are accessible
- [ ] No console errors
- [ ] Responsive design works

## Success Criteria
- [ ] All files created as per structure
- [ ] Basic navigation between sections
- [ ] Mobile-responsive design
- [ ] Session persistence working
- [ ] No critical errors in console
- [ ] All tests passing

## Next Steps
1. Review the project structure
2. Install required dependencies
3. Implement base templates
4. Add basic styling
5. Test navigation
6. Verify session management
