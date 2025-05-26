# UI/UX Specification Document

## 1. Design Language

### 1.1 Color Palette
- **Primary**: `#1a73e8` (Google Blue)
- **Secondary**: `#4285f4` (Lighter Blue)
- **Background**: `#ffffff` (White)
- **Surface**: `#f8f9fa` (Light Gray)
- **Text**: `#202124` (Almost Black)
- **Secondary Text**: `#5f6368` (Gray)
- **Accent**: `#34a853` (Green for success)
- **Error**: `#ea4335` (Red for errors)
- **Warning**: `#fbbc04` (Yellow for warnings)

### 1.2 Typography
- **Primary Font**: 'Google Sans', Arial, sans-serif
- **Monospace**: 'Roboto Mono', monospace (for code)
- **Base Size**: 16px (1rem)
- **Scale**: 1.125 Major Third (1.125)
- **Line Height**: 1.5 for body, 1.25 for headings
- **Font Weights**: 400 (Regular), 500 (Medium), 700 (Bold)

### 1.3 Spacing System
- **Base Unit**: 4px
- **Scale**: 0.25rem (4px), 0.5rem (8px), 1rem (16px), 1.5rem (24px), 2rem (32px), 3rem (48px), 4rem (64px)

### 1.4 Border Radius
- **Small**: 4px
- **Medium**: 8px
- **Large**: 16px
- **Full**: 9999px (for pills and rounded elements)

## 2. UI Components

## 3. User Flow & Interaction

### 3.1 Application Flow
1. **Dashboard View**
   - Grid/List of all portfolio sections
   - Visual indicators for completion status
   - Quick actions for each section

2. **Section Workspace**
   - **Left Panel (40% width)**: 
     - Read-only Band 6 template
     - Section navigation
     - Export controls
   - **Right Panel (60% width)**:
     - Current question/input field
     - Contextual help
     - Navigation controls
     - Progress indicators

3. **Question Flow**
   - One question displayed at a time
   - Conditional logic for question display
   - Progress indicator (e.g., "Question 3 of 12")
   - Save & Continue functionality

### 3.2 Interactive Elements
- **Input Fields**
  - Text areas with character count
  - Rich text formatting options
  - Auto-save functionality
  - Validation indicators

- **Navigation Controls**
  - Previous/Next buttons
  - Section jump menu
  - Save & Exit option
  - View Full Template toggle

- **Help & Feedback**
  - Contextual help button
  - Example responses
  - Quality indicators
  - Feedback submission

### 3.3 Responsive Behavior
- **Desktop (>1024px)**: Side-by-side panels
- **Tablet (768px-1024px)**: Stacked panels with collapsible template
- **Mobile (<768px)**: Single panel with tabbed interface

### 3.4 Accessibility Features
- Keyboard navigation
- Screen reader support
- High contrast mode
- Adjustable text size
- Reduced motion option

## 4. UI Components

### 2.1 Navigation
- **Sidebar**: Collapsible, 280px width (64px when collapsed)
- **Top Bar**: 64px height, contains app title and user controls
- **Breadcrumbs**: Below top bar, shows current location
- **Menu Items**: 48px height, with icons and labels
- **Active State**: Solid background with left border highlight

### 2.2 Buttons
- **Primary**: Filled with primary color, 8px border radius
- **Secondary**: Outlined, 8px border radius
- **Text**: Text only with hover effect
- **Icon**: Circular, 40x40px
- **Floating Action Button (FAB)**: 56x56px, elevation 6, primary color

### 2.3 Cards
- **Elevation**: 1dp default, 8dp on hover
- **Padding**: 1.5rem
- **Border Radius**: 8px
- **Hover Effect**: Subtle scale (1.01) and elevation increase

### 2.4 Forms
- **Input Fields**: 56px height, 8px border radius
- **Labels**: 12px above field, animated on focus
- **Placeholder**: 16px, secondary text color
- **Focus State**: Primary color border bottom
- **Error State**: Red border and text below field

### 2.5 Editor
- **Toolbar**: Fixed at top when scrolling
- **Preview**: Split view with live preview
- **Markdown Syntax**: Color-coded in editor
- **Word Count**: Bottom right corner
- **Save Status**: Small indicator in bottom left

## 3. Layout

### 3.1 Grid System
- **Columns**: 12-column responsive grid
- **Gutter**: 1.5rem (24px)
- **Max Width**: 1280px
- **Side Margins**: 5% on large screens, 3% on medium, 4% on small

### 3.2 Breakpoints
- **Mobile**: 0-599px
- **Tablet**: 600-1023px
- **Desktop**: 1024px+

## 4. Animations & Transitions

### 4.1 Micro-interactions
- **Button Press**: 100ms scale down
- **Hover**: 200ms ease-in-out
- **Menu Open**: 300ms cubic-bezier(0.4, 0, 0.2, 1)
- **Page Transitions**: 250ms fade

### 4.2 Feedback
- **Success Toast**: Slide up, 3s duration
- **Error Message**: Shake animation
- **Loading Spinner**: Rotating 1s linear infinite

## 5. Accessibility

### 5.1 Keyboard Navigation
- **Tab Order**: Logical flow through form elements
- **Focus States**: Clear visual indicators
- **Skip Links**: For main content navigation

### 5.2 ARIA
- **Roles**: Properly defined for all interactive elements
- **Labels**: Descriptive for screen readers
- **Live Regions**: For dynamic content updates

## 6. Dark Mode (Future)
- **Background**: `#121212`
- **Surface**: `#1e1e1e`
- **On Surface**: `#e1e1e1`
- **Primary**: `#8ab4f8` (Lighter blue for better contrast)

## 7. Design Tokens
All design decisions are stored as CSS custom properties for easy theming and maintenance.
