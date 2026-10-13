# Alibaba Cloud Model Studio V4.1 Pilot

## Run metadata

| Field | Value |
| --- | --- |
| Provider | Alibaba Cloud Model Studio |
| Endpoint | `https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions` |
| Dataset | 6 synthetic Literary Benchmark seeds |
| Temperature | 0.2 for Qwen; provider default for Kimi K3 |
| Models | `qwen3.8-27b`, `kimi-k3` |
| Human scores | pending |
| Baseline comparison | pending |

## Observed runtime

| Model | Completed | Visible final outputs | Total tokens | Average latency |
| --- | ---: | ---: | ---: | ---: |
| qwen3.8-27b | 6/6 | 6/6 | 5036 | 22535 ms |
| kimi-k3 | 6/6 | 5/6 | 11305 | 31484 ms |

Kimi K3 always uses thinking mode. One pilot case reached the output limit before a visible final answer; it is counted as completed API transport but incomplete for answer quality.

## Interpretation

This pilot proves the DashScope adapter, model routing, metadata capture and comparison files work. It does not compare model quality or prove superiority. A valid comparison still needs identical task IDs, baseline outputs, human scores, evidence rubric and confidence intervals.
