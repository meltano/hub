/* Count of connectors */

SELECT connector_type, count(*), count(distinct connector_name)
FROM dbt.list_connectors
GROUP BY connector_type
;

/* Count of issues */

select
    count(*)                            AS row_count,
    count(distinct comments)            AS comments,
    count(distinct created_at || id)    AS repos_with_comments
from raw_ajdev.issues
;

