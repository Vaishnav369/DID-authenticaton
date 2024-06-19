import fingerprint_recognition as fr

# Initialize Fingerprint Scanner
scanner = fr.Scanner()

# Function to enroll fingerprints
def enroll_fingerprint(user_id):
    print("Place your finger on the scanner multiple times for enrollment.")
    fingerprints = []
    for _ in range(3):  # Capture multiple scans
        scan = scanner.capture()
        fingerprints.append(scan)
    fr.store_fingerprint(user_id, fingerprints)
    print("Enrollment successful for user:", user_id)

# Function to load known fingerprints
def load_known_fingerprints():
    return fr.load_fingerprints()

# Function to authenticate fingerprint
def authenticate_fingerprint():
    print("Place your finger on the scanner for authentication.")
    scan = scanner.capture()
    known_fingerprints = load_known_fingerprints()
    user_id = fr.match_fingerprint(scan, known_fingerprints)
    if user_id:
        print("Authentication successful for user:", user_id)
    else:
        print("Authentication failed.")

# Enroll a user (example)
enroll_fingerprint("user123")

# Authenticate a user
authenticate_fingerprint()

# Cleanup
scanner.close()