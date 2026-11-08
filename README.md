# Python Django Template

Production-oriented Django starter for Adios.

## Deploy

```sh
adios up
```

## Configuration

* **Runtime:** `python@3.13`
* **Build:** Installs dependencies, then collects static assets from `backend/`
* **Release:** Declares migrations as a separate release command
* **Start:** Runs Gunicorn from `backend/` and binds to `${PORT:-8080}`
* **Health:** Verifies both Django and PostgreSQL with a read-only `SELECT 1`

## Notes

* The Django project root is `backend/`
* `DJANGO_SETTINGS_MODULE` is set to `backend.settings`
* Worker count and worker class can be adjusted with `GUNICORN_WORKERS` and `GUNICORN_WORKER_CLASS`
