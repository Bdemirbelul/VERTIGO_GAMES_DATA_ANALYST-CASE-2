# User Characteristics Analysis - Task 2

This project analyzes user characteristics, segmentations, and trends from in-game and monetization activities.

## Project Structure

```
Vertigo_games_task2/
│
├── data/
│   ├── raw/              # Place your original dataset here
│   └── processed/        # Processed/cleaned data will be saved here
│
├── analysis/
│   └── main_analysis.py  # Main analysis script
│
├── outputs/
│   ├── figures/          # Generated visualizations (PNG, PDF, etc.)
│   └── reports/          # Analysis reports and summaries
│
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add Your Dataset**
   - Place your dataset file in the `data/raw/` folder
   - Supported formats: CSV, Excel (.xlsx, .xls)
   - Update the file path in `analysis/main_analysis.py` if needed

3. **Run Analysis**
   ```bash
   python analysis/main_analysis.py
   ```

## Analysis Plan

The analysis will cover:

1. **First-Day Engagement Segmentation**
   - Segment users based on their engagement metrics on the first day
   - Identify high, medium, and low engagement groups

2. **Session Duration Trends**
   - Analyze how session duration changes over time
   - Identify if sessions get longer or shorter as time progresses
   - Detect any seasonal or periodic patterns

3. **Additional Creative Analyses**
   - User retention patterns
   - Monetization behavior analysis
   - Behavioral clustering
   - Other insights based on data exploration

## Output

- **Visualizations**: Saved in `outputs/figures/`
- **Reports**: Saved in `outputs/reports/`

## Notes

- The analysis script is a template that needs to be customized based on your actual dataset columns
- Make sure to update column names and data processing logic according to your dataset structure

