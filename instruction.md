Review the access log at /app/access.log and write a single JSON report to /app/report.json.

1. The report must be valid JSON and must contain exactly three top-level fields: total_requests, unique_ips, and top_path.
2. total_requests must equal the number of non-empty log lines in /app/access.log.
3. unique_ips must equal the number of distinct client IP addresses seen in /app/access.log.
4. top_path must equal the path from the request line that appears most often in /app/access.log. If several paths tie, use the lexicographically smallest path.

Do not include any extra fields or explanatory text in the report.
