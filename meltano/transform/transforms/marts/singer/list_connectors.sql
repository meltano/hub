SELECT *
FROM {{ ref("stg_repositories") }} AS stg
;
