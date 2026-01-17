# dashboard Component Catalog

## Available Components

### Card
A card container with optional title

### Grid
Grid layout with configurable columns

### Stack
Flex stack for horizontal or vertical layouts

### Metric
Display a single metric with optional trend indicator

### Chart
Display a chart from array data

### Table
Display tabular data

### List
Render a list from array data

### Button
Clickable button with action

### Select
Dropdown select input

### DatePicker
Date picker input

### Heading
Section heading

### Text
Text paragraph

### Badge
Small status badge

### Alert
Alert/notification banner

### Divider
Visual divider

### Empty
Empty state placeholder

## Available Actions

- `export_report`: Export the current dashboard to PDF
- `refresh_data`: Refresh all metrics and charts
- `view_details`: View detailed information
- `apply_filter`: Apply the current filter settings

## Visibility Conditions

Components can have a `visible` property:
- `true` / `false` - Always visible/hidden
- `{ "path": "/data/path" }` - Visible when path is truthy
- `{ "auth": "signedIn" }` - Visible when user is signed in
- `{ "and": [...] }` - All conditions must be true
- `{ "or": [...] }` - Any condition must be true
- `{ "not": {...} }` - Negates a condition
- `{ "eq": [a, b] }` - Equality check

## Validation Functions

Built-in: `required`, `email`, `minLength`, `maxLength`, `pattern`, `min`, `max`, `url`