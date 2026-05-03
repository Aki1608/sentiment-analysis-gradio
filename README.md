# Sentiment Analysis

A lightweight, machine learning-powered web application that analyzes raw text and instantly determines the underlying emotional tone (Positive, Negative, or Neutral). This project demonstrates natural language processing (NLP) capabilities using pre-trained transformer models wrapped in a clean, interactive user interface.

## Features
* **Real-Time Inference:** Instantly categorizes text sentiment with high accuracy.
* **Interactive Web UI:** Clean, intuitive interface for users to type or paste text and see immediate results.
* **Confidence Scoring:** Outputs the model's mathematical confidence percentage alongside the final prediction.
* **Lightweight Architecture:** Designed to run efficiently on local machines without requiring massive GPU resources.

## Tech Stack
* **Python 3.10+**
* **Hugging Face Transformers** (NLP pipeline)
* **PyTorch / TensorFlow** (Backend ML framework)
* **Gradio** (Frontend Web UI)

## Project Structure
* `app.py` - The main application script containing both the UI and the model inference logic.
* `model_logic.py` - The core inference engine. It handles loading the pre-trained NLP model, evaluating the text, and returning the predicted sentiment label alongside its mathematical confidence score.
* `requirements.txt` - The exact list of dependencies needed to run the environment.

## Quick Start Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Set Up the Environment
It is highly recommended to run this inside a Virtual Environment to keep your system clean.
```bash
python -m venv venv

# Activate on Mac/Linux:
source venv/bin/activate  

# Activate on Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required machine learning libraries and UI framework:
```bash
pip install -r requirements.txt
```
*(Note: The first time you run the app, it may take a minute to download the pre-trained model weights from Hugging Face).*

### 4. Launch the Application
Start the local web server:
```bash
python app.py
```
Click the local URL generated in your terminal (e.g., `http://127.0.0.1:7860`) to open the app in your browser and start analyzing text!

---

## How It Works
When a user submits text through the UI, the input is tokenized and passed through a pre-trained NLP classification model. The model calculates the mathematical probability of the text belonging to specific sentiment classes, returning the highest probability as the final label along with its confidence score.
