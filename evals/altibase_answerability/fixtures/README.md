# Fixtures

Fixtures are small calibration inputs for validator, answer-runner, judge, and report
tests. They should be small enough to run without the full benchmark or live model
calls.

Fixture question records must still be source-backed if they are real benchmark
questions. Synthetic fixtures used only for schema error handling should be clearly
named and kept out of production manifests.
