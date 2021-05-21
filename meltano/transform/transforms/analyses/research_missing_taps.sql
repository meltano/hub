/* These were expected but not found:

https://github.com/singer-io/tap-ordway
https://github.com/singer-io/tap-pendo
https://github.com/singer-io/tap-yotpo
*/

SELECT *
FROM dbt.list_targets
WHERE full_name in (
    'singer-io/tap-ordway',
    'singer-io/tap-pendo',
    'singer-io/tap-yotpo'
)
