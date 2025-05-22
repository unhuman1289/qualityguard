from pathlib import Path
import os
import json
import random
from collections import Counter

output_folder = Path(r'C:\Users\tranv\OneDrive\unhuman1289\qualityguard_onedrive\output\fhir')
ndjson_file   = os.path.join(output_folder, 'data.ndjson')

with open(ndjson_file, 'w', encoding='utf-8') as outfile:
    for root, _, files in os.walk(output_folder):
        for file in files:
            if file.endswith('.json'):  # file.endswith('.ndjson') if input is NDJSON
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        line = line.strip()
                        if not line:
                            continue
                        # parse row by row
                        try:
                            obj = json.loads(line)
                        except json.JSONDecodeError:
                            # if input is JSON. fallback to read the whole file
                            infile.seek(0)
                            obj = json.load(infile)
                        json.dump(obj, outfile)
                        outfile.write('\n')


output_ndjson = 'data_with_quality.ndjson'

warning_rate = 0.05  # 5% warnings
error_rate = 0.02    # 2% errors

def inject_quality_score():
    with open(ndjson_file, 'r') as infile, open(output_ndjson, 'w') as outfile:
        for line in infile:
            resource = json.loads(line)
            # Default 100 quality score
            quality_score = 100

            # Random inject
            r = random.random()
            if r < error_rate:
                quality_score = random.uniform(70, 89)  # error range <90
            elif r < error_rate + warning_rate:
                quality_score = random.uniform(90, 98.9)  # warning range 90-<99

            resource['qualityScore'] = round(quality_score, 2)
            outfile.write(json.dumps(resource) + '\n')

    print(f"Injected quality scores written to {output_ndjson}")

if __name__ == '__main__':
    inject_quality_score()


quality_counter = Counter()

with open(output_ndjson, 'r') as f:
    for line in f:
        resource = json.loads(line)
        qs = resource.get('qualityScore', 100)
        if qs < 90:
            quality_counter['error'] += 1
        elif qs < 99:
            quality_counter['warning'] += 1
        else:
            quality_counter['ok'] += 1

print("Quality score distribution:")
for k, v in quality_counter.items():
    print(f"  {k}: {v}")