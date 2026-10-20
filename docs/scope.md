# Version 1.0 Scope

## Purpose

Generate a statistical report describing, without making evaluative judgments, how a pitcher’s performance as a starter changed between two seasons, using official data from the MLB Stats API.

## Report Contents

All metrics are calculated exclusively from the pitcher’s starts; relief appearances are excluded.

**Primary metrics.** K%, BB%, K-BB%, and HR/9, expressed as indices where 100 represents the league average for starting pitchers in the corresponding season. For each metric, the report indicates whether a higher value is better or worse. Each metric has its own threshold table based on FanGraphs; descriptors are assigned using the raw value, not the index. Metrics without a published threshold table are reported only as indices.

**Sample context.** Games started, innings pitched (in standard baseball notation), and outs per start. These are displayed without indices or descriptors.

**Supplementary metrics.** ERA, FIP, WHIP, and BABIP, calculated using outs. These are displayed as raw values, without indices or descriptors.

**Chart.** A comparison of the primary metric indices across both seasons, with a reference line at 100. The chart opens in an interactive window with zoom, pan, and save controls when a display is available, and is always saved as a PNG image.

## Handling Innings Pitched

The API reports innings pitched in baseball notation, where ".1" and ".2" represent one-third and two-thirds of an inning, respectively, rather than tenths. Internally, innings are converted to outs (integers), and all calculations that depend on innings pitched use outs as their starting point. Standard baseball notation is used only for display.

## Input and Output

- Input: The pitcher’s MLB player ID and two different seasons, provided through a terminal command.
- If the seasons are entered in reverse order, the program sorts them chronologically; the comparison is always presented from the earlier season to the more recent one.
- Supported seasons in v1.0: 2025 and 2026, regular season only.
- Output: A text report in the terminal and a chart saved as a PNG image.
- The program stops with a clear message explaining the reason when:
- The same season is entered twice.
- An unsupported season is requested; the message lists the available seasons.
- The player ID does not exist.
- The pitcher has no starts in either of the selected seasons.
- The API does not respond or there is no internet connection.

## Data Sources

- Pitcher statistics: The MLB Stats API, using game logs filtered to include only starts.
- League averages for starting pitchers and each season’s FIP constant: Entered manually in `reference.py`, kept separate from the calculation logic, with a source and access date recorded for each value.
- Descriptive thresholds: FanGraphs Library, with the source cited in the code.

## Priorities

- **Must have:** Everything described in the preceding sections.
- **Should have:** A split covering the pitcher’s last five starts of the more recent season, reported as indices without descriptors. This feature will be implemented only after the season-to-season comparison works end to end; if implementation becomes too complex, it will be deferred to v1.1.
- **Could have:** Pitcher lookup by name instead of ID; exact values displayed when hovering over the chart.

## Non-Goals

- Expected statistics (xERA, xwOBA, or other Statcast metrics).
- Support for other sports.
- Real-time data.
- Predictions of any kind, including betting predictions.
- A web interface.
- Pitch-by-pitch analysis.
- Postseason statistics.
- Relief pitcher analysis.

## Known Limitations

- Reference values are entered manually: their accuracy depends on correct data entry, and league averages for an ongoing season change daily.
- FanGraphs thresholds are fixed, do not distinguish between starters and relievers, and may not reflect each season’s run-scoring environment.
- Metrics are unstable over a small number of starts; sample context is provided to help readers keep this limitation in mind.

## Definition of Done

1. Another person can clone the repository, install the dependencies by following the README, and run a query using the documented command.
2. For a pitcher with starts in both seasons, the report includes every section listed under "Report Contents" and generates the chart image.
3. The error cases described under "Input and Output" result in a clear message and program termination, without a traceback.
4. The test suite passes with `pytest` without an internet connection and includes tests for metric calculations, innings-to-outs conversion, and error cases.
5. Every value in `reference.py` has a documented source.

## Deployment Definition

As the final stage of v1.0, the project is installed on a Raspberry Pi and the query is run over SSH, producing the same text report and image file as on the development PC. The image is transferred to the PC using `scp`.
