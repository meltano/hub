SELECT t.name, t.full_name, t.*
FROM {{ source('tap_github_index', 'tap_something') }} as t
WHERE t.name like 'tap-%'
   OR t.name like '%-tap-%'
