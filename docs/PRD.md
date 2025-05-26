# Product Requirements Document (PRD)
# NESA Stage 6 IT Multimedia Portfolio Assistant

## 1. Overview
A web-based tool to assist NESA Stage 6 Industrial Technology Multimedia students in creating their Major Project portfolio documentation. The application provides structured guidance through comprehensive portfolio sections with a mobile-first approach, similar to modern educational platforms like Khan Academy.

## 2. Core Features

### 2.1 Responsive Design
- Mobile-first approach with responsive layouts for all device sizes
- Touch-friendly interface for mobile users
- Optimized for both portrait and landscape orientations

### 2.2 Portfolio Structure

#### 1. Statement of Intent
- Project overview and objectives
- Scope and limitations

#### 2. Research
- **Materials**
  - File formats and compression
  - Graphics (Vector/Bitmap)
- **Resources**
  - Tutorials and media libraries
  - Potential songs and websites
  - Expert consultations
- **Processes**
  - Animation techniques
  - Camera angles
  - Other relevant processes
- **Technologies**
  - Software requirements
  - Hardware specifications

#### 3. Selection & Justification
- Materials and resources
- Processes and technologies
- Design choices

#### 4. Development of Ideas
- **Idea Generation**
  - Brainstorming sessions
  - Character concepts
  - Background sketches
- **Prototyping**
  - UI/Layout designs
  - Initial storyboards
  - Design modifications

#### 5. Project Management
- Time and action plan
- Financial planning
- Production records
- Copyright and legal considerations
- WHS and safety practices
- Presentation techniques
- Outsourcing details

#### 6. Final Evaluation
- Project outcomes
- Success metrics
- Lessons learned
- Future improvements

### 2.3 Interactive Features
- Contextual help tips
- Progress indicators
- Section completion tracking
- Auto-save functionality

### 2.4 Data Management
- Browser localStorage for session persistence
- Manual save/load functionality
- Data export in Markdown (.md) format

## 3. User Flow
1. User opens application
2. Enters Gemini API key (stored in session only)
3. Navigates through portfolio sections
4. Receives guided prompts and suggestions
5. Saves progress automatically to localStorage
6. Exports completed sections as .md files

## 4. Technical Specifications

### 4.1 Frontend
- **Framework**: Vanilla JavaScript
- **Styling**: CSS with mobile-first approach
- **State Management**: Browser localStorage
- **Rich Text**: Simple Markdown editor
- **Responsive**: Flexbox/Grid layout

### 4.2 Backend (Flask)
- **Framework**: Flask (Python)
- **Templates**: Jinja2
- **Sessions**: Server-side session management
- **API**: RESTful endpoints for Gemini integration

### 4.3 Data Flow
1. User input → localStorage (immediate save)
2. On export: localStorage → Formatted Markdown file
3. Gemini API: User input → Backend → Gemini → Response to frontend

## 5. Security
- API keys handled server-side only
- No persistent user data storage
- Session-based authentication
- Input sanitization

## 6. Constraints
- No user accounts
- Data persists only in current session (with localStorage fallback)
- Export limited to Markdown format
- Gemini API key required for AI features

## 7. Success Metrics
- Time to complete portfolio sections
- Number of sections completed
- Export usage statistics
- User feedback on guidance quality

## 8. Future Considerations
- Additional export formats
- Cloud save functionality
- Offline mode with service workers
- Template customization

## 9. Technical Dependencies
- Python 3.8+
- Flask 2.0+
- Google Generative AI Python SDK
- Modern web browser with JavaScript enabled
