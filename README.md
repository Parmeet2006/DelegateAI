<div align="center">

# 🤖 DelegateAI / Prompt2Phone
### *Type the Task. AI Makes the Call.*

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![MongoDB Atlas](https://img.shields.io/badge/Database-MongoDB%20Atlas-47A248.svg?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/atlas)
[![OpenAI Model](https://img.shields.io/badge/LLM-GPT--4o--mini-412991.svg?style=for-the-badge&logo=openai)](https://openai.com/)
[![ElevenLabs Voice](https://img.shields.io/badge/Voice%20AI-ElevenLabs-black.svg?style=for-the-badge)](https://elevenlabs.io/)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg?style=for-the-badge)](LICENSE)

*An Autonomous Multi-Agent Voice System that translates natural language text prompts into real-world automated outbound phone calls.*

[Features](#-features) • [System Architecture](#-system-architecture) • [Tech Stack](#%EF%B8%8F-tech-stack) • [Installation & Setup](#%EF%B8%8F-installation--setup) • [Repository Structure](#-repository-structure) • [Author](#-author)

</div>

---

## 🌟 Overview

**DelegateAI (Prompt2Phone)** is a full-stack, autonomous telephony agentic platform developed as the capstone project for the **6-Week Industrial Agentic AI Program at Auribises Technologies, Ludhiana**.

Instead of manually parsing team contacts and calling individuals to give updates or follow-ups, users simply type an instruction in plain language (e.g., *"Call Gourav on 9872898728 and tell him to set up a client visit at Amritsar for parking at Golden Temple"*). 

The platform's **AI Agent** uses **OpenAI Function Calling** to extract intent, parameters, and contact metadata, saves the structured task in **MongoDB Atlas**, and triggers an **ElevenLabs + Twilio Conversational Voice Agent** to place a natural human-like outbound phone call autonomously.

---

## ✨ Features

- **💬 Conversational Prompting Engine:** Free-form text input interface built on Streamlit with custom typing animations and stateful session memory.
- **🧠 Zero-Shot Function Calling:** Leverages `gpt-4o-mini` native function tool schemas to parse natural language into structured JSON payloads (`title`, `description`, `name`, `action`).
- **📞 Outbound Voice Agent:** Integrated with ElevenLabs Conversational AI and Twilio API to place real-world outbound phone calls.
- **🔄 Dynamic Context Injection:** Automatically injects recipient names and task summaries as dynamic context variables into voice agent conversations.
- **📊 Real-Time Telephony Dashboard:** Live state machine tracking (`pending` ➔ `calling` ➔ `completed` / `failed`) with conversation status polling and task boards.
- **☁️ Persistent Cloud Storage:** NoSQL database backend powered by MongoDB Atlas for user tasks, status logs, and team contact directories.

---

## 🏗️ System Architecture

```text
  ┌──────────────────────┐      1. Natural Language Prompt      ┌──────────────────────┐
  │   Streamlit Web UI   │ ───────────────────────────────────> │     OpenAI Agent     │
  │   (Prompt2Phone)     │ <─────────────────────────────────── │    (gpt-4o-mini)     │
  └──────────┬───────────┘      2. Structured Tool Output       └──────────┬───────────┘
             │                                                             │
             │ 3. Save Task / Query Logs                                   │ Extract Parameters
             ▼                                                             ▼
  ┌────────────────────────────────────────────────────────────────────────────────────┐
  │                              MongoDB Atlas Database                                │
  │                      Collections: `tasks`  |  `contacts`                          │
  └────────────────────────────────────────┬───────────────────────────────────────────┘
                                           │
                                           │ 4. Fetch Pending Calls
                                           ▼
                               ┌──────────────────────┐
                               │   Caller Telephony   │
                               │     Voice Agent      │
                               │ (ElevenLabs + Twilio)│
                               └──────────────────────┘
