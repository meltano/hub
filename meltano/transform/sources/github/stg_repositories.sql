SELECT
    *
FROM (
    SELECT
        t.name              AS connector_name,
        CASE
            WHEN t.name LIKE 'tap-%'
              OR t.name LIKE '%-tap-%'
            THEN 'tap'
            ELSE 'target'
        END                 AS connector_type,
        t.id                AS repo_id,
        t.full_name         AS repo_full_name,
        fork                AS is_fork,
        forks               AS num_forks,
        license__spdx_id    AS license_spdx_id,
        owner__url          AS repo_owner_url,
        open_issues_count   AS num_open_issues,
        watchers_count      AS num_watchers,
        stargazers_count    AS num_stargazers,
        created_at          AS created_at_timestamp,
        pushed_at           AS last_push_timestamp,
        updated_at          AS last_updated_timestamp,
        search_name         AS repo_search_name,
        _sdc_batched_at     AS batch_timestamp,
        _sdc_deleted_at     AS deleted_at_timestamp,
        row_number() OVER (
            PARTITION BY id
            ORDER BY _sdc_batched_at DESC
        )               AS recency_rank
    FROM {{ source('tap_github', 'repositories') }} as t
    WHERE (
        (t.name like 'tap-%' OR t.name like '%-tap-%') OR
        (t.name like 'target-%' OR t.name like '%-target-%')
    )
      AND t.name not like 'tap-practica-%'
) list_connectors
WHERE recency_rank = 1
--   AND deleted_at_timestamp IS NULL
