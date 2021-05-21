# Meltano project for MeltanoHub

## Infra Setup

Initial infra setup steps are defined in [setup.md](./setup.md).

## Specifying local creds and dev config

1. Copy local settings and config from [`.env.template`](.env.template) to a new `.env` file.

## Testing EL locally

```bash
JOBID="LOCAL_DEV"
meltano elt tap-github target-jsonl --job_id=$JOBID
meltano elt tap-github target-jsonl --job_id=$JOBID --dump=state > .output/local-dev.state.json
```

## Running EL

```bash
JOBID="ATHENA_DEV"
meltano elt tap-github target-athena --job_id=$JOBID
meltano elt tap-github target-athena --job_id=$JOBID --dump=state > .output/local-dev.state.json
```

## Running dbt transforms

```bash
meltano invoke dbt run
```
