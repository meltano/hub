SELECT
    t.id          AS repo_id,
    t.name,
    t.full_name,
    row_number() OVER (
        PARTITION BY full_name ORDER BY _sdc_batched_at DESC
    )               AS recency_rank
FROM {{ source('tap_github_index', 'target_something') }} as t
WHERE t.name like 'target-%'
   OR t.name like '%-target-%'
