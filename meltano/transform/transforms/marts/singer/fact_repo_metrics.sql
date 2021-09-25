SELECT *
FROM {{ ref("stg_repositories") }} AS stg
WHERE connector_type = 'tap'
