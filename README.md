# Spatial similarity analysis

**Repository structure**
1. corranalysis.py - correlation analysis script
2. inputs/ - input files for correlation analysis
3. outputs/ - output data from correlation analysis of memory and motor function maps (as per paper)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


**Example**
```terminal
$ python /filePath/corranalysis.py
Loading input files...
Extracting Neurosynth data for region of interest (mask)...
Getting MNI space coordinates
Checking values of the provided NIFTI file at well locations
No mask provided - using implicit (not NaN, not zero) mask
Co-registration done and saved!
Starting analysis for region of interest...
Gene #1
Plotting the correlation graph...
Saving the correlation graph...
```
