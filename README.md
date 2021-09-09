# glyphs-scripts
Scripts for Glyphs. Beware: Most of these script currently only fork on Glyphs 2 and are experimentally being updated for Glyphs 3. Use at your own risk. Apologies for broken stuff.

## Auto-Name Instances
Names instances based on assigned names. Useful for batch-renaming large families. Allows defining of naming exceptions for width classes.

## Batch Export
Opens a dialogue to choose multiple export formats. Sorts exported files into respective sub-directories (/Desktop/TTF, /Web/WOFF2, ...).

## Delete Duplicate Nodes
Checks for duplicate nodes (for instance after converting quadratic curves to cubic) and delete these.

## Instance Kerner (WIP, one axis only)
Adds Replace Feature custom parameter for every instance for kerning. Useful for hard-coded capital/sc spacing. Currently only works for single-axis setups, still trying to figure out how to make this work for multiple axes. Todo: more than two kerning values per axis

## Interpolate Anchors
Same as clicking Re-Interpolate in the layers panel, but only affects anchors.

## Interpolation Preview
Allows for visual interpolation, in order to add the interpolation as an instance or an intermediate layer. Respects multi-axis design spaces. Adding as an instance is still wobbly for Glyphs 3.

## Make Smooth Nodes
Finds nodes that are not set to smooth that should be smooth. Useful for cleaning up client projects when they don’t know how to draw properly.

## Make Web Weights
Converts master and instance weight values into USWeightClass values based on naming. Calculates AVAR table for correct interpolation. Takes care of intermediate layer values as well.

## Write AVAR
Writes an AVAR table based on stem weights. Affects only weight, regardless of axis count.


# License

Copyright 2020 The eweracs Glyphs-Scripts Project Authors.

Some code samples by Georg Seifert (@schriftgestalt) and Rainer Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use the software provided here except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
