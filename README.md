# MLops CI/CD Demo with UV

This repository is a **minimal MLops CI/CD demo** project using [uv](https://github.com/astral-sh/uv) for dependency management and GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD).  

The focus of this project is **CI/CD**, not machine learning modeling. You can experiment with code changes, run tests automatically, and see the impact in GitHub Actions.



## 🚀 Features

- Automated **testing** with `pytest` using `uv`.
- **CI/CD workflow** triggers on every push or pull request to `master`.
- Simulated **deployment step** after tests pass.
- Easy to extend: add linting, formatting, artifact uploads, or real model training.



## 🗂️ Project Structure


```
mlops-cicd-demo/
│
├── src/
│   ├── train.py       # Simulated training code
│   ├── evaluate.py    # Simulated evaluation code
│   └── utils.py       # Utility functions
│
├── tests/
│   └── test_utils.py  # Unit tests
│
├── pyproject.toml     # uv project configuration & dependencies
├── README.md          # This file
└── .github/workflows/ci.yml  # GitHub Actions workflow
```




## ⚙️ Prerequisites

- Python ≥ 3.9
- Git
- GitHub account
- [uv](https://astral.sh/uv) installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or via pipx
pipx install uv
````

Verify installation:

```bash
uv --version
```

---

## 🏗️ Setup & Run Locally

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/mlops-cicd-demo.git
cd mlops-cicd-demo
```

2. Initialize uv environment:

```bash
uv init --python 3.10
```

3. Install dependencies:

```bash
uv sync
```

4. Run tests:

```bash
uv run pytest
```

5. Run training code (simulated):

```bash
uv run python src/train.py
```

---

## ⚡ CI/CD Workflow

The GitHub Actions workflow is located at `.github/workflows/ci.yml`.

### Workflow Steps:

1. **Checkout** your repository.
2. **Install uv** and set up Python.
3. **Sync dependencies** using uv.
4. **Run tests** using `pytest`.
5. **Deploy simulation** (runs only if tests pass):

   ```bash
   echo "🚀 Deployed successfully at $(date)" > deploy_log.txt
   ```

✅ **Result:** Your main branch is protected — broken code cannot deploy.

---

## 🧪 How to Experiment

* Modify `src/utils.py` and push changes.
* Observe the workflow in **GitHub Actions**:

  * ✅ Green = tests passed → deploy ran
  * ❌ Red = tests failed → deploy did NOT run
* Intentionally break tests to see CI fail.
* Fix code → push → CI/CD confirms it’s safe.

---

## 🧠 Learnings

* **CI/CD prevents broken code from reaching production.**
* **uv** provides fast, reproducible dependency management.
* **GitHub Actions** allows automating testing, building, and deployment.

---

## 🔧 Next Steps / Optional Enhancements

* Add linting: `uv add ruff` → `uv run ruff check .`
* Add formatting: `uv add black` → `uv run black .`
* Save model artifacts automatically during deploy.
* Trigger retraining automatically when `data/` changes.

---

## 📄 License

This project is licensed under the MIT License.


