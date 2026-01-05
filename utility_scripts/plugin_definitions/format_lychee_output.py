"""Format lychee output to match the original check_links.py format."""
import json
import sys


def parse_lychee_output(lychee_output):
    """Parse lychee JSON output and extract failed URLs."""
    failed_urls = []
    try:
        data = json.loads(lychee_output)
        # Extract URLs from error_map
        for results in data.get("error_map", {}).values():
            for result in results:
                failed_urls.append(result.get("url"))
    except json.JSONDecodeError:
        # Fallback: parse text output
        for line in lychee_output.split("\n"):
            if "[FAILED]" in line or "✗" in line:
                parts = line.split()
                if parts:
                    failed_urls.append(parts[-1])
    return failed_urls


def format_output(failed_urls, url_mapping):
    """Format output as file -> URLs for GitHub issue."""
    file_to_urls = {}

    for url in failed_urls:
        files = url_mapping.get(url, [])
        for file_path in files:
            if file_path not in file_to_urls:
                file_to_urls[file_path] = []
            file_to_urls[file_path].append(url)

    output = ""
    for file_name, urls in file_to_urls.items():
        output += f"- {file_name}\n"
        for url in urls:
            output += f"  - {url}\n"

    return output


if __name__ == "__main__":
    # Read lychee output from stdin
    lychee_output = sys.stdin.read()

    # Load URL mapping
    try:
        with open(".url_mapping.json") as f:
            url_mapping = json.load(f)
    except FileNotFoundError:
        print("Error: .url_mapping.json not found", file=sys.stderr)
        sys.exit(1)

    # Parse and format
    failed_urls = parse_lychee_output(lychee_output)
    output = format_output(failed_urls, url_mapping)

    print(output)
