# Fleet Management

FastAPI + Jinja2 fleet management app with JSON-file persistence for:
- Equipment
- Work Orders
- Users

## Current State (February 2026)

Implemented:
- Server-rendered web pages (`/`, `/equipment`, `/equipment/{equip_id}`)
- Create and list equipment
- Create and list work orders on the home page
- Filter work orders by equipment on the equipment detail page
- Create users via API endpoint
- Static assets mounted from `/static`

Not fully implemented / in progress:
- Dedicated work order page template exists but is currently empty (`templates/workorder-page.jinja2`)
- No authentication or authorization enforcement
- No database yet (JSON files only)

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Jinja2 templates
- JSON file storage in `app/data/*.json`

## Run Locally

1. Create and activate virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install fastapi "uvicorn[standard]" jinja2 python-multipart
```

3. Start app:

```bash
python main.py
```

4. Open:
- UI: `http://127.0.0.1:8000`
- API docs: `http://127.0.0.1:8000/docs`

## Routes

### HTML Routes

- `GET /`
  - Renders `templates/home.jinja2`
  - Shows equipment/work order tables
  - Includes forms to create equipment and work orders

- `GET /equipment`
  - Renders `templates/equipment-page.jinja2`
  - Shows equipment list with links to detail pages

- `GET /equipment/{equip_id}`
  - Renders `templates/equipment-detail.jinja2`
  - Shows one equipment item and related work orders

- `GET /workorder`
  - Wired in router, but template is currently empty

### Equipment API

- `POST /api/equipment/new`
  - Form fields: `name`, `year`, `status`, `notes`
  - Creates equipment and redirects to `/`

- `GET /api/equipment/list`
  - Returns all equipment records

- `GET /api/equipment/{uuid}`
  - Returns one equipment record by UUID

### Work Order API

- `POST /api/workorders/add`
  - Form fields: `title`, `info`, `user`, `severity`, `equipment`
  - Creates work order and redirects to `/`

- `GET /api/workorder/list`
  - Intended to return all work orders
  - Currently broken (see Known Issues)

### User API

- `POST /api/user/new`
  - Form fields: `name`, `permission`, `company`, `email`, `password`, `username`
  - Creates user and returns created user payload

## Data Files

- `app/data/equipment_data.json`
- `app/data/workorders_data.json`
- `app/data/user_data.json`

## Project Layout

```text
fleet-Managment/
├── main.py
├── app/
│   ├── app.py
│   ├── routers/
│   │   ├── html.py
│   │   ├── equipment.py
│   │   ├── workorder.py
│   │   └── user.py
│   ├── services/
│   │   ├── equipment_storage.py
│   │   ├── workorder_storage.py
│   │   └── user_storage.py
│   └── data/
│       ├── equipment_data.json
│       ├── workorders_data.json
│       └── user_data.json
├── classes/
│   ├── Equipment.py
│   ├── WorkOrders.py
│   └── User.py
├── templates/
│   ├── layout.jinja2
│   ├── home.jinja2
│   ├── equipment-page.jinja2
│   ├── equipment-detail.jinja2
│   └── workorder-page.jinja2
└── static/
    ├── styles.css
    └── images/LOGO.png
```

## Known Issues

- `GET /api/workorder/list` has a naming conflict in `app/routers/workorder.py`.
  - The route handler `load_workorders()` calls itself recursively instead of the imported service function.
- `Equipment.from_dict()` and `WorkOrder.from_dict()` are missing `@classmethod` and currently do not rehydrate correctly.
- `WorkOrder.get_string()` references `self.equipment_id`, but the model stores `self.equipment`.
- `user_storage.load_users()` catches `FileExistsError` instead of `FileNotFoundError`.
- `templates/workorder-page.jinja2` is empty.
