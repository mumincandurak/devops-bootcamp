# DevOps Bootcamp

![CI](https://github.com/mumincandurak/devops-bootcamp/actions/workflows/ci.yml/badge.svg)

A hands-on, self-directed DevOps learning journey — from Linux fundamentals and networking basics to a fully containerized, CI/CD-driven Python API. This repository documents real work, not tutorials copy-pasted: every script and pipeline here was built, broken, debugged, and fixed by hand.

## What's in here

| Area | Where | What it covers |
|---|---|---|
| **ML API + DevOps pipeline** | [`devops-python/`](devops-python/) | FastAPI service, Docker, Docker Compose, GitHub Actions CI/CD |
| **Linux administration** | [`linux-command/`](linux-command/) | Shell scripting, automated backups, system monitoring |
| **Networking fundamentals** | [`network/`](network/) | Interface/routing inspection, socket auditing, health-check tooling |
| **Python fundamentals** | [`devops-python/python_course/`](devops-python/python_course/) | File I/O, subprocess, YAML/JSON config, scripting patterns |

---

## Flagship project: Sentiment Analysis API

A small FastAPI service that classifies text sentiment, built to practice the full path from "code that runs on my machine" to "service with a CI/CD pipeline."

**Stack:** Python 3.14 · FastAPI · scikit-learn (TF-IDF + Logistic Regression) · Pydantic Settings · Docker · Docker Compose · GitHub Actions · GitHub Container Registry

### Architecture

```
Client → FastAPI (uvicorn) → sentiment model (scikit-learn pipeline, trained at build time)
                            → dummy rule-based model (baseline/fallback endpoint)
```

The model isn't committed to the repo as a binary artifact — it's trained from source (`train.py`) both inside the Docker build and in CI, so the image is always reproducible from code alone.

### API endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Liveness check |
| `POST` | `/models/predict` | Sentiment via a simple keyword-based baseline model |
| `POST` | `/models/sentiment` | Sentiment via the trained scikit-learn pipeline |

### Running it

**Locally (venv):**
```bash
cd devops-python
pip install -r requirements.txt
python app/train.py                 # generates the model
uvicorn app.main:app --reload
```

**With Docker Compose (recommended — includes hot reload):**
```bash
cd devops-python
docker compose up --build
```

Then:
```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/models/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "this is a great day"}'
```

### Testing

```bash
pytest devops-python/tests
```

### CI/CD pipeline

Every push and pull request runs the `test` job (install deps, train the model, run the pytest suite). On a push to `main` — and only once tests pass — a second job builds the Docker image and publishes it to GitHub Container Registry (`ghcr.io/mumincandurak/devops-python-api`). Pull requests never produce an image; only reviewed, merged code does.

```
pull_request → test
push (main)  → test → build → push to GHCR
```

The Dockerfile also declares a `HEALTHCHECK` (implemented in pure Python, no extra OS packages needed), and a standalone monitoring script ([`monitoring/watch_health.py`](devops-python/monitoring/watch_health.py)) polls the `/health` endpoint independently of the container it watches — so the monitor doesn't go silent the moment the thing it's monitoring crashes.

---

## Linux & networking

Small, purpose-built scripts from working through core sysadmin/networking tasks:

- [`linux-command/backup.sh`](linux-command/backup.sh) — timestamped `tar.gz` backups with error handling
- [`linux-command/system-info.sh`](linux-command/system-info.sh) — quick disk/memory/user snapshot
- [`network/health-check.sh`](network/health-check.sh) — reads a URL list, checks HTTP status codes, logs results with timestamps
- [`network/ag-kesif.md`](network/ag-kesif.md) — notes from exploring interfaces, routing tables, and open sockets (`ip addr`, `ip route`, `ss -tulnp`)

## Learning journal

Running notes on commands and concepts as they were learned: [`learning-journal.md`](learning-journal.md).

---

*This repository is a work in progress — new modules are added as new DevOps topics are covered.*
