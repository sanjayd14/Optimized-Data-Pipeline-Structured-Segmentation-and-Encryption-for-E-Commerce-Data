#installation - pip install cryptography
import sys
import csv
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_value(value):
    # Encrypt the value
    encrypted_value = cipher_suite.encrypt(value.encode())
    return encrypted_value.decode()

def decrypt_value(encrypted_value):
    # Decrypt the value
    decrypted_value = cipher_suite.decrypt(encrypted_value.encode()).decode()
    return decrypted_value

# Function to encrypt a column by header name
def encrypt_column_by_name(csv_content, header_name):
    # Read CSV content from stdin
    csvreader = csv.reader(csv_content.splitlines())
    
    # Extract headers and find index of header_name
    headers = next(csvreader)
    if header_name not in headers:
        raise ValueError(f"Header '{header_name}' not found in CSV.")
    
    column_index = headers.index(header_name)
    
    # Initialize output CSV content
    output_csv = [headers]
    
    # Iterate through each row
    for row in csvreader:
        if len(row) > column_index:
            # Encrypt the specified column
            row[column_index] = encrypt_value(row[column_index])
            
        # Append the modified row to the output CSV
        output_csv.append(row)
    
    # Write the modified CSV back to stdout
    sys.stdout.write('\n'.join([','.join(row) for row in output_csv]))

# Main execution
if __name__ == "__main__":
    # Read input CSV data from stdin (flow file content)
    csv_content = sys.stdin.read()
    column_header_name = "Payment Info"  # Column to be encrypted
    
    # Call function to encrypt the specified column by header name
    encrypt_column_by_name(csv_content, column_header_name)

# Note: To decrypt the values later, use the `decrypt_value` function