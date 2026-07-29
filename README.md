# Inventory Reorder Alert System


## Approach Summary
The script reads the inventory using `csv.DictReader`, catching basic file and value errors using try/except blocks. I compared quantities against thresholds to flag items 

Additionally, it handles the following bonus objectives:
*   **Priority Levels:** Differentiates between "Critical" (below 25% of threshold) and "Low" stock.
*   **Reorder Suggestion:** Calculates a suggested reorder amount to reach 150% of the item's threshold.
*   **CSV Export:** Exports the flagged data to a `restock_report.csv` file.

## Expected output
When run successfully, the terminal will display the following confirmation, and a new restock_report.csv file will be generated in the same folder:

$ python inventory_script.py

Success: Found 2 low-stock items.

Report saved to 'restock_report.csv'.

