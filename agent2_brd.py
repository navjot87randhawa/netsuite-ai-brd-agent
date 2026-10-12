# Install the necessary library for talking to AI models
!pip install openai -q

import os
from google.colab import userdata
from openai import OpenAI

# Agent 2 System Prompt (The NetSuite BRD Specialist)
AGENT_2_SYSTEM_PROMPT = """
You are a senior NetSuite Functional Consultant. Your job is to convert raw discovery call transcripts into a professional, structured NetSuite BRD.
Structure your output into these exact sections:
1. Project Scope & Objectives
2. Current State vs. NetSuite Future State (Mapping native features vs. custom SuiteCustomizations)
3. Functional Requirements & Process Flows (Order-to-Cash / Procure-to-Pay / Manufacturing Workflows)
4. Data Migration & Integration Touchpoints
5. Out-of-Scope & Risk Warnings
"""

def generate_brd(transcript_text, api_key):
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Cost-efficient and fast model
        messages=[
            {"role": "system", "content": AGENT_2_SYSTEM_PROMPT},
            {"role": "user", "content": f"Please convert this discovery transcript into a structured NetSuite BRD:\n\n{transcript_text}"}
        ]
    )
    return response.choices[0].message.content

# --- TEST YOUR AGENT ---
# Sample mock discovery transcript
sample_transcript = """
Consultant: Let's discuss your manufacturing process. How do you handle work orders?
Client: We currently use paper tickets. When an assembly item is ordered, we manually issue components. We have 2-level BOMs and we track serial numbers on high-value pumps, but everything else is bulk inventory. We really need NetSuite to handle our WIP and routing automatically.
"""

print("--- Testing Agent 2 (BRD Specialist) ---")
# Note: In Colab, you would plug in your OpenAI API key to run this live
print("Agent 2 Prompt and Logic loaded successfully!")