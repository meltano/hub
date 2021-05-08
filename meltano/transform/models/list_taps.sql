SELECT
    t.id          AS repo_id,
    t.name,
    t.full_name
FROM {{ source('tap_github_index', 'tap_something') }} as t
WHERE t.name like 'tap-%'
   OR t.name like '%-tap-%'
