# GitHub Submission Checklist

- [ ] Extract `SmartBiz-AI-GitHub-Ready.zip`
- [ ] Open the project folder in VS Code
- [ ] Create `.env` from `.env.example`
- [ ] Run `pip install -r requirements.txt`
- [ ] Run `uvicorn backend.main:app --reload`
- [ ] Open `http://127.0.0.1:8000`
- [ ] Open `http://127.0.0.1:8000/docs`
- [ ] Run `streamlit run dashboard/app.py`
- [ ] Open the Streamlit dashboard
- [ ] Run `pytest -q`
- [ ] Create a GitHub repository named `smartbiz-ai`
- [ ] Push the project
- [ ] Add screenshots to the README after running it locally
- [ ] Replace the demo dataset with institution-approved data if required

## Git commands

```bash
git init
git add .
git commit -m "Initial SmartBiz AI full-stack project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smartbiz-ai.git
git push -u origin main
```
