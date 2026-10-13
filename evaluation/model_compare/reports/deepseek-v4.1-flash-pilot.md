# DeepSeek V4.1 Flash Pilot

## Run metadata

| Field | Value |
| --- | --- |
| Provider | DeepSeek |
| API model | `deepseek-flash` |
| Model family | DeepSeek-V4.1-Flash |
| Endpoint | `https://api.deepseek.com/chat/completions` |
| Dataset | 6 synthetic Literary Benchmark seeds |
| Temperature | 0.2 |
| Thinking | disabled for visible final-answer measurement |
| Run file | `experiments/runs/deepseek-v4.1-flash-pilot.jsonl` |

## Observed runtime

```text
Cases: 6
Completed: 6
Non-empty outputs: 6
Total tokens: 2729
Average latency: 3077.17 ms
Human scores: pending
Baseline comparison: pending
```

## Interpretation

This pilot proves that the DeepSeek V4.1 Flash API path, dataset adapter, metadata capture and output persistence work. It does not measure model superiority: there is no matched baseline, no independent human scoring and no confidence interval. The next run should use a fixed sample, a baseline model, and blind review.
