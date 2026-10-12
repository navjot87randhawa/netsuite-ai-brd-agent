# NetSuite AI Implementation Accelerator (Agent 2 Core) Open in Colab

An open-source, AI-powered documentation pipeline designed to accelerate NetSuite ERP manufacturing implementations by converting raw discovery transcripts into professional Business Requirement Documents (BRDs).

## 🚀 Project Overview
ERP implementation consulting involves heavy administrative documentation. This capstone project builds a modular, multi-agent AI system to automate the documentation lifecycle (reducing post-meeting drafting time by up to 80%).

This repository hosts the core open-source Python engine, starting with **Agent 2 (The NetSuite BRD Specialist)**.

---

## 🛠️ Hybrid Architecture
- **Agents 1–4 (Python / Google Colab):** Local open-source scripts handling document processing, transcript ingestion, BRD generation, walkthrough planning, and UAT test scripts.
- **Agent 5 (MindStudio):** A hosted interactive portal acting as an enterprise NetSuite architectural guide and Scrum Master.

---

## 📄 Agent 2: NetSuite BRD Specialist
Agent 2 ingests raw text transcripts from client discovery sessions and maps them directly against enterprise NetSuite functional standards (Discrete & Process Manufacturing, Work Orders & Assemblies, WIP & Routing, and Inventory Management).

### Structured Output Format:
1. **Project Scope & Objectives**
2. **Current State vs. NetSuite Future State** (Native features vs. custom SuiteCustomizations)
3. **Functional Requirements & Process Flows** (Order-to-Cash, Procure-to-Pay, Shop Floor Control)
4. **Data Migration & Integration Touchpoints**
5. **Out-of-Scope & Risk Warnings**

---

## ⚙️ How to Run Agent 2 (Google Colab)
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/navjot87randhawa/netsuite-ai-brd-agent/blob/main/agent2_brd_agent.py)
2. Copy and run the code from `agent2_brd_agent.py`.
3. When prompted, upload your discovery session text transcript file (`.txt`).
4. The agent will parse the text and output a client-specific NetSuite BRD.

---

## 💻 Tech Stack
- **Language:** Python
- **Environment:** Google Colab
- **AI Model:** OpenAI API (`gpt-4o-mini`)
- **Domain:** NetSuite Cloud ERP (Manufacturing & Supply Chain)
