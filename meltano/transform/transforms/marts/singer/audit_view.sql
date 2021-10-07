-- {{ config(materialized='table') }}

SELECT 'fact_repo_metrics' as table_name, max(last_push_timestamp) as max_as_of_date
FROM {{ ref("fact_repo_metrics") }} AS tbl

/*
UNION ALL

SELECT 'source:repositories' as table_name, max(last_push_timestamp) as max_as_of_date
FROM {{ source("tap_github", "repositories") }} AS tbl

UNION ALL

SELECT 'source:issues' as table_name, max(last_push_timestamp) as max_as_of_date
FROM {{ source("tap_github", "issues") }} AS tbl

UNION ALL

SELECT 'source:issue_comments' as table_name, max(last_push_timestamp) as max_as_of_date
FROM {{ source("tap_github", "issue_comments") }} AS tbl
*/
