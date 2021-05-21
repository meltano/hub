WITH cte_shifted AS (

    -- The target-athena implementation has bug which left-shifts columns when others are omitted.
    SELECT
        _sdc_batched_at,
        _sdc_deleted_at,
        _sdc_extracted_at,
        author_association,
        body        AS created_at,
        created_at  AS id,
        id          AS org,
        org         AS repo,
        repo        AS updated_at
    FROM {{ source('tap_github', 'issues') }}

)

SELECT
    *
FROM (
    SELECT
        id                  AS issue_comment_id,
        author_association  AS author_association_type,
        org || '/' || repo  AS full_name,
        created_at          AS created_at_timestamp,
        updated_at          AS last_updated_timestamp,
        _sdc_batched_at     AS batch_timestamp,
        _sdc_deleted_at     AS deleted_at_timestamp,
        row_number() OVER (
            PARTITION BY id
            ORDER BY _sdc_batched_at DESC
        )               AS recency_rank
    FROM cte_shifted as t
) AS issues
WHERE recency_rank = 1
--   AND deleted_at_timestamp IS NULL
