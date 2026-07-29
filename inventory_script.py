import csv

def generate_restock_report(input_csv, output_csv):
    items_to_reorder = []
    
    try:
        with open(input_csv, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                sku = row['SKU']
                name = row['Product_Name']
                qty = int(row['Quantity'])
                threshold = int(row['Threshold'])
                

                if qty < threshold:
                    # Bonus 1: Priority levels
                    if qty < (0.25 * threshold):
                        priority = "Critical"
                    else:
                        priority = "Low"
                        
                    # Bonus 2: Reorder quantity suggestion
                    suggested_order = int(threshold * 1.5) - qty
                        
                    items_to_reorder.append({
                        'SKU': sku,
                        'Product_Name': name,
                        'Current_Qty': qty,
                        'Threshold': threshold,
                        'Priority': priority,
                        'Suggested_Order': suggested_order
                    })
                    
    except FileNotFoundError:
        print(f"Error: The file {input_csv} could not be found.")
        return
    except (ValueError, KeyError) as e:
        print(f"Error: Issue with CSV data formatting - {e}")
        return

    # Bonus 3: Export as CSV report
    if items_to_reorder:
        try:
            with open(output_csv, mode='w', newline='') as file:
                fieldnames = ['SKU', 'Product_Name', 'Current_Qty', 'Threshold', 'Priority', 'Suggested_Order']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(items_to_reorder)
                
            print(f"Success: Found {len(items_to_reorder)} low-stock items.")
            print(f"Report saved to '{output_csv}'.")
        except IOError:
            print(f"Error: Could not write to the file {output_csv}.")
    else:
        print("All items are sufficiently stocked. No report generated.")


generate_restock_report('inventory.csv', 'restock_report.csv')