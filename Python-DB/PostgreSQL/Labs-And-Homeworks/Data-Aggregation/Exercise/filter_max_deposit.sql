SELECT
    magic_wand_creator,
    MAX(deposit_amount) AS max_deposit_amount
FROM wizard_deposits
GROUP BY magic_wand_creator
HAVING MAX(deposit_amount) NOT BETWEEN 20000 and 40000
ORDER BY max_deposit_amount DESC
LIMIT 3