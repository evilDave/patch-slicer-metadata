#!/usr/bin/env python3
import sys
import re

file = sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(file, "r") as f:
    lines = f.readlines()
f.close()

# Overwrite the g-code file
with open(file, "w") as of:
    of.write('; Postprocessed by [patch-slicer-metadata](https://github.com/evilDave/patch-slicer-metadata)\n\n')
    for i in range(len(lines)):
        line = lines[i]
        match = re.search('filament_density:|filament_diameter:', line)
        if not match:
            of.write(line)  # skip the added metadata
of.close()
