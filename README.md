# CubeDave's Cube Shop

A full-stack web shop for Rubik's cubes — built with SvelteKit, FastAPI, and SQLite.

**Live:** https://cubedave.ch

---

## Stack

| Layer | Technology |
|---|---|
| Frontend | SvelteKit 5 + Tailwind CSS 4 |
| Backend | FastAPI + SQLAlchemy |
| Database | SQLite |
| Proxy | Nginx + Let's Encrypt |
| Deployment | Docker + Docker Compose |

---

## Run locally

```bash
docker compose up -d --build
```

App: http://localhost
API docs: http://localhost/docs

---

## Run tests

```bash
cd app
source .venv/bin/activate
pytest test_main.py -v
```

---

## Documentation

[Full project documentation](documentation/project-doc.md)
