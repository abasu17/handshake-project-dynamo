import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log", encoding="utf-8") as handle:
    for line in handle:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if match:
            paths[match.group(1)] += 1

if paths:
    highest_count = max(paths.values())
    top_path = min(path for path, count in paths.items() if count == highest_count)
else:
    top_path = ""

with open("/app/report.json", "w", encoding="utf-8") as handle:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": top_path,
        },
        handle,
        indent=2,
    )
    handle.write("\n")
print("wrote /app/report.json")
