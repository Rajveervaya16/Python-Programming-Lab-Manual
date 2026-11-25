print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import base64
# Accept message
message = input("Enter a message: ")
# Convert message into bytes
data = message.encode()
# Encode message
encoded = base64.b64encode(data)
# Display encoded message
print("Encoded message:", encoded.decode())
# Decode message
decoded = base64.b64decode(encoded)
# Display decoded message
print("Decoded message:", decoded.decode())
