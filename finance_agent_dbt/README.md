# 🧠 finance_agent_dbt

This is a modular and scalable [dbt](https://www.getdbt.com/) project built on top of [DuckDB](https://duckdb.org/), designed to support analytical pipelines for a local finance-focused data stack.

> ⚡ This project is part of a broader initiative: building an AI-powered Finance Agent that interacts directly with the gold layer.  
> It serves both as a **full-stack data engineering showcase** and as the **foundation for future AI integrations**.

---

## 🔧 Project Overview

This project implements a **medallion architecture** using DBT + DuckDB, organized into the following layers:

- **Bronze**: Raw ingested data from CSV files (e.g. customers, channels, transactions)
- **Silver** _(coming soon)_: Cleaned, normalized and joined data for analysis
- **Gold** _(coming soon)_: Final data models and aggregated metrics ready for reporting, decision-making or AI interaction

All data is stored locally in a single DuckDB database file.

---

## 💡 Vision & Roadmap

The final goal of this repo is to support an AI Agent — the **Finance AI Agent** — capable of querying business-relevant information directly from the Gold layer using natural language.

This includes:
- Automating analysis of revenue, transactions and customer behavior
- Powering dashboards, alerts, or Slack assistants
- Supporting decision-making for early-stage fintechs and analysts

By designing this pipeline from scratch, the project also showcases end-to-end capabilities across:

✅ Data Engineering  
✅ Analytics Engineering  
✅ AI Integration (soon)

---

## 📁 Project Structure

```
finance_agent_dbt/
├── models/
│   ├── bronze/        # Raw staging models loaded from CSVs
│   ├── silver/        # Cleaned, filtered and transformed data (soon)
│   └── gold/          # Final business-facing models for AI (soon)
├── dbt_project.yml    # DBT config
├── README.md          # Project documentation
```

---

## 📦 Environment Setup

### 1. Clone this repository
```bash
git clone https://github.com/your_username/finance_agent_dbt.git
cd finance_agent_dbt
```

### 2. Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use:
```bash
pip install dbt-duckdb pandas numpy
```

---

## 🛠️ DBT Usage

Make sure your DuckDB file is already created (e.g. by running `load_bronze_tables.py` before any `dbt run`).

### Run all models:
```bash
dbt run
```

### Run only one layer:
```bash
dbt run --select bronze
```

### Test the connection:
```bash
dbt debug
```

---

## 📄 Notes

- The DuckDB file is located at:  
  `../database_duckdb/duckdb_files/finance_db.duckdb`
- This project is **local-first** and does not require any external warehouse
- Ideal for:
  - AI Agents
  - Prototypes and MVPs
  - Lightweight data pipelines
  - Training data engineers in full-stack thinking

---

## 📌 TODO

- [x] Build bronze models from mockdata
- [ ] Build silver layer (cleaned + joined data)
- [ ] Build gold layer (aggregates & metrics)
- [ ] Integrate with an AI Agent
- [ ] Add tests and data validation
- [ ] Create documentation with `dbt docs`
- [ ] Add CI/CD integration

---

## 📬 Author

Nicolas — [https://github.com/nicolasmap]