import base64
import json
from collections import deque

def _shift_string(s, n):
    """
    Helper to perform a circular shift on a string.
    
    Args:
        s (str): The string to shift.
        n (int): The number of positions to shift.
    
    Returns:
        str: The circularly shifted string.
    """
    d = deque(s)
    d.rotate(n)
    return ''.join(d)

def custom_encrypt(data):
    """
    Encrypts data using a basic, custom substitution and reversal scheme.
    This is for demonstration/educational purposes only and is not
    cryptographically secure.
    
    The encryption process involves:
    1.  Converting the data (e.g., a dictionary) to a JSON string.
    2.  Encoding the JSON string to Base64.
    3.  Performing a circular string shift.
    4.  Reversing the shifted string.
    
    Args:
        data (dict): The data to encrypt (e.g., a user's pillbox data).
    
    Returns:
        str: The "encrypted" string.
    """
    # Convert data to JSON string and encode to Base64
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    
    # Apply a circular shift
    shift_amount = 3
    shifted_data = _shift_string(encoded_data, shift_amount)
    
    # Reverse the string
    return shifted_data[::-1]

def custom_decrypt(encrypted_data):
    """
    Decrypts data encrypted with `custom_encrypt`.
    
    Args:
        encrypted_data (str): The string to decrypt.
    
    Returns:
        dict: The original decrypted dictionary.
    """
    # Reverse the string back
    reversed_data = encrypted_data[::-1]
    
    # Apply the reverse circular shift
    shift_amount = -3
    unshifted_data = _shift_string(reversed_data, shift_amount)
    
    # Decode from Base64 and load JSON
    decoded_data = base64.b64decode(unshifted_data.encode('utf-8')).decode('utf-8')
    return json.loads(decoded_data)

# Example Usage:
if __name__ == "__main__":
    # Sample "pillbox" data
    pillbox_data = {
        "user_id": 123,
        "meds": [
            {"name": "Lipitor", "dose": "20mg"},
            {"name": "Aspirin", "dose": "81mg"}
        ],
        "supplements": [
            {"name": "Vitamin D", "dose": "1000 IU"},
            {"name": "Calcium", "dose": "500mg"}
        ]
    }
    
    # Encrypt the data
    encrypted_payload = custom_encrypt(pillbox_data)
    print("Original Data:", pillbox_data)
    print("Encrypted String:", encrypted_payload)
    
    # Decrypt the data
    decrypted_payload = custom_decrypt(encrypted_payload)
    print("Decrypted Data:", decrypted_payload)

    # Validate that the decrypted data matches the original
    assert pillbox_data == decrypted_payload
    print("Decryption successful: Original and decrypted data match.")