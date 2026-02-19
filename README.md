# Autonomous CI/CD Healing Agent — RIFT 2026 Hackathon

> **AIML DevOps Automation | Agentic Systems Track**
> Team: **Byte-Force** | Leader: **Raunit Raj**

---

## Live Deployment

| Service | URL |
|---|---|
| React Dashboard | `https://your-deployed-dashboard-url.vercel.app` |
| Backend API (FastAPI) | `https://your-backend-url.railway.app` |

> Replace above URLs with your actual deployed URLs before submission.

---

## LinkedIn Demo Video

> [Watch the Demo on LinkedIn](https://www.linkedin.com/posts/your-post-link)
> Must be 2-3 min, public, and tagged with #RIFT2026

---

## Project Title

**Autonomous CI/CD Healing Agent with React Dashboard**

An end-to-end autonomous agent that takes a GitHub repository URL, clones it, discovers all test files, detects bugs (LINTING, SYNTAX, LOGIC, TYPE_ERROR, IMPORT, INDENTATION), auto-fixes them using an AI multi-agent system, commits fixes with `[AI-AGENT]` prefix to a new branch, monitors the CI/CD pipeline, and iterates until all tests pass — all visualized in a production-ready React dashboard.

---

## Architecture Diagram

```
+------------------+       +-------------------+       +-------------------+
|  React Dashboard | ----> |  FastAPI Backend   | ----> |  Orchestrator     |
|  (Vite + React)  | <---- |  /api/run-agent    | <---- |  Agent (LangGraph)|
+------------------+       +-------------------+       +-------------------+
                                                               |
                          +------------------------------------+
                          |                |
               +----------v---+    +-------v-----------+
               | Bug Detector  |    | Fix Generator     |
               | Agent         |    | Agent (GPT/Gemini)|
               +----------+---+    +-------+-----------+
                          |                |
               +----------v----------------v-----------+
               |         Git Agent                      |
               |  (creates branch, commits, pushes)     |
               +------------------------------------------+
                          |
               +----------v-----------+
               |   CI/CD Monitor       |
               |   Agent (GitHub API)  |
               +-----------------------+
```

**Flow:**
1. User submits GitHub repo URL + Team Name + Leader via React dashboard
2. FastAPI backend triggers the Orchestrator agent
3. Bug Detector agent clones repo, runs `flake8` + `pytest`, collects all failures
4. Fix Generator agent creates targeted fixes for each bug
5. Git Agent creates branch `BYTE-FORCE_RAUNIT_RAJ_AI_Fix`, commits with `[AI-AGENT]` prefix
6. CI/CD Monitor checks GitHub Actions status, retries up to 5 times
7. Results saved to `results.json` and sent back to dashboard

---

## Installation Instructions

### Prerequisites
- Node.js >= 18
- Python >= 3.10
- Docker (recommended for sandboxed code execution)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/raunitx-02/buggy-test-repo.git
cd buggy-test-repo
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

### 3. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Backend API runs at `http://localhost:8000`

---

## Environment Setup

Create a `.env` file in the `backend/` directory:

```env
# GitHub
GITHUB_TOKEN=your_github_personal_access_token

# AI Provider (choose one)
OPENAI_API_KEY=your_openai_api_key
# OR
GOOGLE_API_KEY=your_gemini_api_key

# Agent Config
MAX_RETRIES=5
BRANCH_PREFIX=AI_Fix

# Optional
DOCKER_SANDBOX=true
```

---

## Usage Examples

### Via React Dashboard
1. Open the dashboard at your deployed URL
2. Enter:
   - **GitHub Repository URL**: `https://github.com/raunitx-02/buggy-test-repo`
   - **Team Name**: `Byte-Force`
   - **Team Leader**: `Raunit Raj`
3. Click **Run Agent**
4. Watch the real-time CI/CD timeline and fixes table populate

### Via API directly

```bash
curl -X POST https://your-backend-url/api/run-agent \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/raunitx-02/buggy-test-repo",
    "team_name": "Byte-Force",
    "team_leader": "Raunit Raj"
  }'
```

### Sample `results.json` output

```json
{
  "repository_url": "https://github.com/raunitx-02/buggy-test-repo",
  "team_name": "Byte-Force",
  "team_leader": "Raunit Raj",
  "branch_created": "BYTE-FORCE_RAUNIT_RAJ_AI_Fix",
  "total_failures": 5,
  "total_fixes": 5,
  "ci_status": "PASSED",
  "score": { "base": 100, "speed_bonus": 10, "efficiency_penalty": 0, "total": 110 },
  "fixes": [
    { "file": "src/utils.py", "bug_type": "LINTING", "line_number": 15, "commit_message": "[AI-AGENT] Remove unused import os in src/utils.py line 15", "status": "Fixed" },
    { "file": "src/validator.py", "bug_type": "SYNTAX", "line_number": 8, "commit_message": "[AI-AGENT] Add missing colon in src/validator.py line 8", "status": "Fixed" },
    { "file": "src/calculator.py", "bug_type": "LOGIC", "line_number": 28, "commit_message": "[AI-AGENT] Fix power() logic error in src/calculator.py line 28", "status": "Fixed" },
    { "file": "src/converter.py", "bug_type": "TYPE_ERROR", "line_number": 36, "commit_message": "[AI-AGENT] Fix seconds_to_hms return type in src/converter.py line 36", "status": "Fixed" },
    { "file": "src/loader.py", "bug_type": "IMPORT", "line_number": 7, "commit_message": "[AI-AGENT] Add PyYAML to requirements.txt for src/loader.py line 7", "status": "Fixed" }
  ]
}
```

---

## Supported Bug Types

| Bug Type | Description | Example |
|---|---|---|
| `LINTING` | Unused imports, style violations (flake8) | `import os` never used |
| `SYNTAX` | Python syntax errors | Missing colon on `def` |
| `LOGIC` | Wrong arithmetic or conditional logic | `base ** (exp+1)` instead of `base ** exp` |
| `TYPE_ERROR` | Wrong return type | Function returns `list` instead of `str` |
| `IMPORT` | Missing module not in requirements | `import yaml` with no PyYAML installed |
| `INDENTATION` | Wrong indentation levels | Mixed tabs/spaces |

---

## Tech Stack

### Frontend
- React 18 (Vite)
- Tailwind CSS
- Recharts (score visualization)
- Axios (API calls)
- Zustand (state management)

### Backend
- Python 3.10+
- FastAPI
- LangGraph (multi-agent orchestration)
- GitPython (git operations)
- flake8 (linting)
- pytest (test runner)
- Docker (sandboxed execution)

### Infrastructure
- GitHub Actions (CI/CD)
- Vercel (frontend deployment)
- Railway (backend deployment)

---

## Known Limitations

- Agent currently supports Python repositories only (no JavaScript/TypeScript bug fixing)
- Maximum 5 CI/CD retry iterations (configurable)
- Docker sandbox required for safe code execution in production
- Very large repositories (>500 files) may exceed the agent's token context window
- GitHub API rate limiting may slow down CI/CD monitoring for rapid successive runs

---

## Team Members

| Name | Role |
|---|---|
| Raunit Raj | Team Leader, Full-Stack & Agent Development |
| Bhavesh Kumawat | Backend & Agent Architecture |
| Mohit Shrimali | Frontend & Dashboard Development |
| Hardik Nangia | DevOps & CI/CD Integration |

---

## Test Repository

This repository (`buggy-test-repo`) is the **intentionally buggy test repo** used to validate the agent.

| File | Bug Type | Line | Description |
|---|---|---|---|
| `src/utils.py` | `LINTING` | 15 | Unused `import os` |
| `src/validator.py` | `SYNTAX` | 8 | Missing colon on `def validate_username` |
| `src/calculator.py` | `LOGIC` | 28 | `power()` uses `exp+1` instead of `exp` |
| `src/converter.py` | `TYPE_ERROR` | 36 | `seconds_to_hms()` returns `list` instead of `str` |
| `src/loader.py` | `IMPORT` | 7 | `import yaml` but PyYAML missing from `requirements.txt` |

---

*Built with for RIFT 2026 Hackathon — AIML DevOps Automation Track*
