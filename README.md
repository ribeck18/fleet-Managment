# Fleet Management

A FastAPI-based fleet management web app for tracking equipment and work orders, with server-rendered pages using Jinja2 and JSON file storage.

## Current Status

This is an in-progress CRUD project. The app currently supports:

- Creating equipment records from the home page
- Listing equipment records
- Creating work orders from the home page
- Listing work orders on the home page

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Jinja2 templates
- JSON file persistence (no database yet)

## Project Structure

```text
fleet-Managment/
├── main.py
├── app/
│   ├── app.py
│   ├── routers/
│   │   ├── html.py
│   │   ├── equipment.py
│   │   └── workorder.py
│   ├── services/
│   │   ├── equipment_storage.py
│   │   └── workorder_storage.py
│   └── data/
│       ├── equipment_data.json
│       └── workorders_data.json
├── classes/
│   ├── Equipment.py
│   └── WorkOrders.py
├── templates/
│   ├── layout.jinja2
│   └── home.jinja2
└── static/
    └── images/LOGO.png
```

## Quick Start

1. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install fastapi "uvicorn[standard]" jinja2 python-multipart
```

3. Start the app.

```bash
python main.py
```

4. Open in browser:

- App UI: `http://127.0.0.1:8000`
- Interactive API docs: `http://127.0.0.1:8000/docs`

## Routes

### HTML

- `GET /`
  - Renders `templates/home.jinja2`
  - Shows equipment and work order tables

### Equipment API

- `POST /api/equipment/new`
  - Form fields: `name`, `year`, `status`, `notes`
  - Creates equipment and redirects to `/`

- `GET /api/equipment/list`
  - Returns all equipment records from `app/data/equipment_data.json`

### Work Order API

- `POST /api/workorders/add`
  - Form fields: `title`, `info`, `user`, `severity`, `equipment`
  - Creates a work order and redirects to `/`

- `GET /api/workorder/list`
  - Intended to return all work orders
  - See Known Issues below

## Data Storage

Data is stored in JSON files:

- `app/data/equipment_data.json`
- `app/data/workorders_data.json`

Each equipment and work order is assigned a UUID. Work orders also store a timestamp (`date`) at creation.

## Known Issues

- `GET /api/workorder/list` currently has a naming conflict in `app/routers/workorder.py`:
  - The route handler function is named `load_workorders`, same as the imported service function.
  - This causes recursive self-calls instead of reading from storage.
- The work order form field is named `equipment`, while saved records use `equipment_id`.
- UI is functional but still basic (inline styles, limited validation).

## Notes

- Static files are mounted at `/static` in `app/app.py`.
- Router registration is in `app/app.py`.
- Application entry point is `main.py` (runs Uvicorn with reload enabled).
