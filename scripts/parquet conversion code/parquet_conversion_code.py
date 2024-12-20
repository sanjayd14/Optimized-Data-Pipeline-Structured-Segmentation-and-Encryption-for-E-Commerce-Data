import sys
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io
import csv

# Function to convert CSV content to Parquet content
def csv_to_parquet(csv_content):
    # Read CSV content from stdin
    csv_data = csv_content.strip().split('\n')
    csv_reader = csv.reader(csv_data)
    
    # Convert CSV to Pandas DataFrame
    df = pd.DataFrame(csv_reader)
    
    # Assuming first row as header, set columns and reset index
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    
    # Convert DataFrame to PyArrow Table
    table = pa.Table.from_pandas(df)
    
    # Write PyArrow Table to Parquet format in memory
    parquet_buffer = io.BytesIO()
    pq.write_table(table, parquet_buffer)
    
    # Get Parquet bytes from buffer
    parquet_bytes = parquet_buffer.getvalue()
    
    # Return Parquet content as bytes
    return parquet_bytes

# Main execution
if __name__ == "__main__":
    try:
        # Read input CSV data from stdin (flow file content)
        csv_content = sys.stdin.read()
        
        # Convert CSV content to Parquet content
        parquet_content = csv_to_parquet(csv_content)
        
        # Output Parquet content to stdout (will be captured as a new FlowFile)
        sys.stdout.buffer.write(parquet_content)
    
    except Exception as e:
        # Print error traceback
        import traceback
        traceback.print_exc()
        raise e
