def analyze_log_file(file_path):
    suspicious_patterns = ["Failed login", "error", "unauthorized access"]
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        
        for log in logs:
            if any(pattern in log for pattern in suspicious_patterns):
                print(f"Suspicious log entry: {log.strip()}")
    except FileNotFoundError:
        print(f"Log file {file_path} not found.")
    except Exception as e:
        print(f"Error reading log file {file_path}: {e}")