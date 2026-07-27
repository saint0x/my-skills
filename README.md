# My Skills

These are my personal skills. You might find them useful.

## Skills

- [LAMP Method First Principles Thinking](./lamp-method-first-principles-thinking/) - A first-principles reasoning skill for reframing hard questions, finding hidden assumptions, and turning surprising observations into falsifiable next experiments.
- [Kernel Engineering](./kernel-engineering/) - A production kernel engineering skill for narrowing hot-path contracts, partitioning execution regimes, designing metadata ABIs, and validating high-performance compute kernels without regressions.
- [RLM Model Evaluation Promotion](./rlm-model-evaluation-promotion/) - A model-eval and promotion discipline for separating ranking wins from generation wins, preserving safe baselines, and only promoting checkpoints that pass broad and live gates.
- [RLM SFT RL Round Control](./rlm-sft-rl-round-control/) - A round-by-round SFT/RL optimization workflow for making one measurable improvement at a time while preserving prior gates.
- [RLM Dataset Engineering](./rlm-dataset-engineering/) - A corpus-design skill for building held-out, OOD, hard-negative, balanced, and non-leaky datasets that expose real agent behavior rather than fixture memorization.
- [RLM Harness Environment Validation](./rlm-harness-environment-validation/) - A harness and environment validation skill for proving that evals, route guards, execution sandboxes, and runtime dependencies measure the intended behavior.
- [Inference Serving Benchmarking](./inference-serving-benchmarking/) - A serving benchmark skill for separating memory capacity, single-user streaming speed, aggregate throughput, queueing, and production inference experience.
- [Production Checkpoint Export Serving](./production-checkpoint-export-serving/) - A production export and serving skill for turning candidate checkpoints into lineage-safe, rollback-ready serving artifacts.
- [Research Optimization Documentation](./research-optimization-documentation/) - A documentation discipline for keeping optimization history, current status, commands, artifacts, and sober interpretation deduplicated and promotion-ready.

## Structure

Each skill is packaged as a standalone directory with a `SKILL.md` file. The layout is intended to be compatible with Codex-style and Claude-style skill conventions:

```text
skill-name/
└── SKILL.md
```

Copy the skill directory into your local skills folder for the agent environment you use.
