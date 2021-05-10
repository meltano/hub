SELECT
    repo_id,
    name,
    full_name
FROM (
    SELECT
        t.id            AS repo_id,
        t.name,
        t.full_name,
        row_number() OVER (
            PARTITION BY full_name ORDER BY _sdc_batched_at DESC
        )               AS recency_rank
    FROM {{ source('tap_github_index', 'tap_something') }} as t
    WHERE (t.name like 'tap-%' OR t.name like '%-tap-%')
      AND t.name not like 'tap-practica-%'
) list_taps
WHERE recency_rank = 1
