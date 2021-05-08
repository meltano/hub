SELECT
    t.id          AS repo_id,
    t.name,
    t.full_name
FROM {{ source('tap_github_index', 'target_something') }} as t
WHERE t.name like 'target-%'
   OR t.name like '%-target-%'
