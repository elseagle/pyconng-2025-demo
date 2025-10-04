# 👋 START HERE - PyCon NG 2025 AutoGen Demo

**Welcome!** This project contains a complete multi-agent demo for your PyCon NG 2025 talk.

## 🚀 Three Steps to Run the Demo

### 1. Install Dependencies (2 min)

```bash
cd /Users/oluwasogo/PYCONNG_2025
poetry install
```

### 2. Add Your API Key (1 min)

```bash
# Copy the example
cp .env.example .env

# Edit and add your OpenAI API key
nano .env
```

Change this line:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

To your actual key:
```env
OPENAI_API_KEY=sk-proj-...your-actual-key...
```

### 3. Run the Demo! (2-3 min)

```bash
poetry run python demo1_content_pipeline/main.py
```

Or use the quick script:
```bash
./run_demo1.sh
```

## 📚 Next: Read the Documentation

After your first run, check out these guides:

1. **For Quick Setup** → `QUICKSTART.md`
2. **For Your Presentation** → `demo1_content_pipeline/DEMO_SHEET.md` ⭐
3. **For Understanding the Code** → `demo1_content_pipeline/README.md`
4. **For Full Details** → `README.md` and `PROJECT_SUMMARY.md`

## 🧪 Test Your Setup

Verify everything is configured correctly:

```bash
poetry run python demo1_content_pipeline/test_setup.py
```

This will check:
- ✓ All packages installed
- ✓ API key configured
- ✓ Tools working
- ✓ Agents ready

## ❓ Having Issues?

### "No module named 'autogen'"
```bash
poetry install
```

### "API key not found"
Make sure `.env` file exists with your `OPENAI_API_KEY`

### Other issues?
Check the troubleshooting section in `QUICKSTART.md`

## 🎤 Preparing for Your Talk?

**Read this first:** `demo1_content_pipeline/DEMO_SHEET.md`

It contains:
- ✓ Pre-demo checklist
- ✓ Demo timeline and talking points
- ✓ Common questions and answers
- ✓ Backup strategies
- ✓ Customization examples

## 🎯 What You'll Demo

A multi-agent content creation system with:
- **Planner** - Coordinates the workflow (triage agent)
- **Researcher** - Gathers info using knowledge base
- **Writer** - Creates content based on research
- **Critic** - Reviews and provides feedback

**Runtime:** 2-3 minutes  
**No external APIs needed** - Everything runs locally!

## 📁 Project Structure

```
PYCONNG_2025/
├── START_HERE.md                  ← You are here!
├── QUICKSTART.md                  Quick setup guide
├── README.md                      Main documentation
├── PROJECT_SUMMARY.md             Comprehensive overview
│
└── demo1_content_pipeline/        The demo!
    ├── main.py                    ⭐ Run this file
    ├── DEMO_SHEET.md             ⭐ Read before presenting
    ├── agents/                    4 specialized agents
    └── tools/                     Simple knowledge base
```

## ⚡ Quick Commands

```bash
# Install
poetry install

# Test setup
poetry run python demo1_content_pipeline/test_setup.py

# Run demo
poetry run python demo1_content_pipeline/main.py

# Or use the script
./run_demo1.sh

# Show structure
tree demo1_content_pipeline -L 2
```

## 🎉 You're Ready!

Once you've run the demo successfully, you're all set for your talk!

**Good luck at PyCon NG 2025! 🚀**

---

**Questions?** Check the documentation files or the troubleshooting sections.

**Need to customize?** All guides show you how to:
- Change the topic
- Modify content type
- Adjust agent behavior
- Enable human-in-the-loop

---

*Project created for: Oluwasogo Ogundowole*  
*Talk: Autogen 101: Building Your First Multi-Agent System*  
*Event: PyCon NG 2025*

