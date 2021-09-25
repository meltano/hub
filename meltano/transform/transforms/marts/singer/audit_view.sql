-- {{ config(materialized='table') }}

SELECT max(last_push_timestamp) as max_last_push_timestamp
FROM {{ ref("fact_repo_metrics") }} AS stg
