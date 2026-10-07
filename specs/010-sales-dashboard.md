# 010: Sales dashboard project

**Files:** `pages/21_Project_Sales_Dashboard.py`, `core/lessons.py`
**Status:** Implemented

## Purpose
The second mini project: explore a table of sales with pandas and Streamlit.
It needs no extra package and no outside data. The table is generated in code
with a fixed seed, so every learner sees the same numbers.

## Requirements
- **R1** The project is listed in the registry in the category "Projects".
- **R2** The page has five numbered parts: the idea, then four steps (look at
  the data, summarise with groupby, filter with widgets, the dashboard). Each
  step has the Learn, Code and Try tabs.
- **R3** The data has 24 months x 4 regions x 3 products: 288 rows and 5
  columns.
- **R4** The filter step starts with North and South selected (144 of 288 rows).
  Choosing East and Laptop leaves 24 rows.
- **R5** The dashboard shows three numbers: Revenue, Orders and Average order.
  The average order is the revenue divided by the orders.
- **R6** Narrowing the filters lowers the revenue.
- **R7** If nothing is selected, the dashboard shows a warning instead of
  numbers.
- **R8** The data is the same every time the page runs.
- **R9** The downloaded script runs on its own: it keeps the data function
  (without its decorator), and its `pip install` line lists numpy and pandas.

## Notes
- Each demo's widgets have different labels, because Streamlit needs every
  widget on a page to be unique.
