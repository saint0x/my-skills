# My Skills

These are my personal skills. You might find them useful.

## Skills

- [Synthesys Bug Triage](./synthesys-bug-triage/) - A production bug-triage skill for investigating Synthesys backend issues across code, database, telemetry, and providers, then repairing the canonical root cause, verifying the real execution path, and shipping safely through staging, main, and redeploy.
- [LAMP Method First Principles Thinking](./lamp-method-first-principles-thinking/) - A first-principles reasoning skill for reframing hard questions, finding hidden assumptions, and turning surprising observations into falsifiable next experiments.
- [Kernel Engineering](./kernel-engineering/) - A production kernel engineering skill for narrowing hot-path contracts, partitioning execution regimes, designing metadata ABIs, and validating high-performance compute kernels without regressions.
- [Model Eval](./model-eval/) - A promotion discipline for separating ranking, generation, execution, OOD, and live-canary evidence before accepting a model checkpoint.
- [Inference Engineering](./inference-engineering/) - A runtime and serving skill for streaming speed, aggregate throughput, memory pressure, checkpoint export, serving profiles, and rollback-safe deployment.
- [Aria Intelligence](./aria-intelligence/) - A canonical Aria artifact skill for selecting the right surface, defining typed contracts, building bundles, uploading to local or cloud runtime profiles, and proving tools, agents, teams, and pipelines on live `/api/v1/run/*` paths.
- [RLM](./rlm/) - An end-to-end coding-agent skill for workflow contracts, tool/action behavior, project-building quality, qualitative generalization, and promotion loops.
- [Env Harness](./env-harness/) - A validation skill for harnesses, route guards, sandboxes, canaries, dependencies, and runtime environments used by RLM/RL systems.
- [RL](./rl/) - A reinforcement-learning skill for preference optimization, hard negatives, reward diagnostics, checkpoint selection, and generation preservation.
- [SFT](./sft/) - A supervised fine-tuning skill for teaching strict formats, action chains, tool JSON, project trajectories, and behavior-first checkpoint selection.
- [Dataset Engineering](./dataset-engineering/) - A corpus-design skill for held-out splits, OOD gates, hard negatives, balanced tool coverage, leakage prevention, and project-builder data.

## Structure

Each skill is packaged as a standalone directory with a `SKILL.md` file. The layout is intended to be compatible with Codex-style and Claude-style skill conventions:

```text
skill-name/
└── SKILL.md
```

Copy the skill directory into your local skills folder for the agent environment you use.
