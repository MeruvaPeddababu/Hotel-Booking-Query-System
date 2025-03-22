# Hotel-Booking-Query-System
# **https://colab.research.google.com/drive/1n_kZBeLsHSjiPs888tiC6ffT3wJrTRke#scrollTo=CzxPGw72Geu-**

# Overview

This project is a Hotel Booking Query System that provides analytics reports and allows users to ask questions about hotel booking data. It integrates LLM-based responses with precomputed analytics and a vector database for efficient retrieval.

# Features

LLM Integration: Uses OpenRouter API (LLaMA 3) for answering queries.

Precomputed Analytics: Provides revenue trends, top booking countries, and lead time distributions.

Vector Search with ChromaDB: Retrieves relevant booking records based on user queries.

Interactive Web UI: Built with Gradio for an intuitive user experience.

Chat History: Stores and displays past interactions.

# Installation

Clone the Repository:

git clone https://github.com/your-repo/hotel-booking-query.git
cd hotel-booking-query

# Install Dependencies:

pip install -r requirements.txt

Download Dataset:
Ensure the hotel_bookings.csv file is placed in the project directory.

Run the Application:

python app.py

# Usage

Enter a question related to hotel bookings in the input box.

Click Ask to get an answer from analytics or LLM.

Click Show History to view past interactions.

Use the Analytics Reports dropdown to view predefined insights.

API Integration

LLM (LLaMA 3 via OpenRouter)

ChromaDB for efficient query retrieval

Gradio UI for user interaction

Sample Queries & Expected Answers

Query

Expected Answer

Which locations had the highest cancellations?

List of top 10 countries with the most cancellations.

Show revenue trends.

Graph displaying monthly revenue changes.

What is the average lead time for bookings?

Summary of lead time statistics.

Implementation Choices & Challenges

Implementation Choices

Used ChromaDB for efficient semantic search over booking records.

Precomputed analytics to quickly respond to common queries.

Integrated OpenRouter API for handling unknown queries.

Developed an interactive UI with Gradio.

# Challenges & Solutions

Data Cleaning: Handled missing values and date inconsistencies.

Query Handling: Distinguished between predefined analytics and LLM-based answers.

Scalability: Optimized database queries for faster response time.

# Submission Checklist

Codebase with LLM integration, analytics, and API.

Sample test queries and expected answers.

Short report on implementation choices and challenges.

Packaged solution with setup instructions in README.

# Contributing

Feel free to submit pull requests for improvements!

License

MIT License
