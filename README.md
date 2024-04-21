

# NBA Search Engine
COMP 631 Information Retrieval Final Project

## Authors
- Chia-Wei Jan (cj35)
- Rung-De Chu (rc118)
## Overview

This project presents a search engine for NBA data using Apache Solr, Python Flask, and Bootstrap for the user interface. Our goal is to provide an intuitive and efficient search tool that allows users to explore detailed play-by-play NBA data with ease.

## Features

- **Backend using Python Flask**: Our backend API is designed with Python Flask, offering robustness and flexibility in handling search queries.
- **Apache Solr Integration**: We leverage the power of Apache Solr to manage and query large datasets effectively.
- **Responsive Frontend**: Utilizing HTML and Bootstrap, the frontend delivers a clean and responsive user interface.
- **Advanced Search Capabilities**: Users can perform complex queries using boolean expressions and filter results by specific dates and other criteria such as game quarters.

## Installation

### Prerequisites

- Python 3.8+
- Flask
- Apache Solr 8.8+

### Setting Up Solr

1. **Start Solr**:
   ```bash
   bin/solr start
   ```

2. **Create a Core**:
   ```bash
   bin/solr create -c nba_data
   ```

3. **Index the Data**:
   ```bash
   bin/post -c nba_data NBA_PBP_2022-2023_correct.csv
   ```

### Launching the Flask App

1. Install dependencies:
   ```bash
   pip install flask
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage

To use the NBA Search Engine, navigate to the hosted URL or localhost if running locally. Enter your search parameters, such as date and team names, to filter through the NBA play-by-play data.

- **Basic Search**: Enter a date (e.g., "Oct 18, 2022") to retrieve all related events.
- **Filtered Search**: Use boolean expressions to narrow down results (e.g., "Lakers" and the specific date).

