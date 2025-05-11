#!/usr/bin/python3
"""
Reads from STDIN line by line, computes:
 - Total file size
 - Count of each status code (200,301,400,401,403,404,405,500)
Every 10 lines and on keyboard interruption, prints the stats.
"""

import sys

def print_stats(total_size, counts):
    """Print total size and counts for non-zero status codes (ascending)."""
    print(f"File size: {total_size}")
    for code in sorted(counts):
        if counts[code]:
            print(f"{code}: {counts[code]}")

def main():
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    counts = {code: 0 for code in status_codes}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            # status code is penultimate, file size is last
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                # skip malformed lines
                continue

            if status in counts:
                counts[status] += 1
            total_size += size

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        pass
    finally:
        # print on exit if we've read at least one line and not just after a perfect multiple of 10
        if line_count % 10 != 0:
            print_stats(total_size, counts)

if __name__ == "__main__":
    main()

