# 🧪 Swag Labs Full-Cycle QA Automation & Test Management Portfolio

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-yellow?logo=pytest)
![Jira](https://img.shields.io/badge/Jira-Atlassian-0052CC?logo=jira)
![Grafana](https://img.shields.io/badge/Grafana-Performance_Monitoring-F46800?logo=grafana)

A comprehensive, industry-standard **Software Quality Assurance (QA)** portfolio project demonstrating manual test design, automated regression testing, defect reporting, and performance observability against the [Swag Labs (saucedemo.com)](https://www.saucedemo.com/) e-commerce web application.

---

## 📌 Project Overview & Highlights

This project demonstrates the complete software testing lifecycle:
1. **Manual Test Design & Jira Scrum Management**: Built a 4-column Agile Kanban/Scrum board (`To Do`, `In Progress`, `In Review`, `Done`) managing 8 tickets (`SCRUM-5` to `SCRUM-12`) with detailed defect reports (Preconditions, Steps to Reproduce, Severity, Expected vs. Actual results, and Retest verification logs).
2. **Web UI Automation (Selenium + Pytest)**: Automated test execution covering authentication validation, catalog visual regression, dropdown sorting, and end-to-end checkout transactions.
3. **Performance Testing & Observability (Grafana)**: Simulated load spikes (up to 500 concurrent Virtual Users) and generated live Grafana SLA monitoring dashboards tracking Throughput (1100+ RPS), Error Rate, and p95 Latency (>5500 ms SLA breach).

---

## 📂 Repository Structure

- `01_panduan_jira_dan_manual_qa.md`: Manual QA fundamentals, Test Cases, and Jira Bug Report template.
- `02_latihan_pytest_dasar.py`: Pytest assertions and test discovery principles.
- `03_latihan_api_testing.py`: REST API test automation using `requests` and `pytest`.
- `04_pengenalan_grafana_dan_load_test.md`: Performance testing metrics (VUs, RPS, p95, Error Rate).
- `05_latihan_web_automation_swaglabs.py`: Automated Selenium test verifying image asset bug (`SCRUM-5`).
- `06_full_test_suite_saucedemo.py`: Comprehensive test suite automating all Jira tickets (`SCRUM-6` to `SCRUM-12`).
- `07_daftar_todo_jira_lengkap.md`: Full English Jira ticket backlog & defect logs.
- `08_latihan_load_test_dan_grafana.py`: Load testing simulation and interactive Grafana Dark Mode dashboard generator.

---

## 🛠️ How to Run the Automated Tests

### 1. Prerequisites
Ensure Python 3.10+ is installed on your machine. Install the required QA libraries:

```bash
pip install pytest requests selenium
```

### 2. Run the Full Test Suite
Execute all automated test cases across Swag Labs:

```bash
pytest 06_full_test_suite_saucedemo.py -v -s
```

### 3. Run the Grafana Load Testing Dashboard
Launch the concurrent virtual user simulation and auto-open the Grafana Performance Dashboard:

```bash
python 08_latihan_load_test_dan_grafana.py
```

---

## 👤 Author
- **Alif Nugraha**
- GitHub: [@AlifNugraha17](https://github.com/AlifNugraha17)
- Quality Assurance | Test Automation | Python | Selenium | Jira | Grafana
