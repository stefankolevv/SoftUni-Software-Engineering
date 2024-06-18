CREATE OR REPLACE PROCEDURE udp_modify_account(
	address_street VARCHAR(30), 
	address_town VARCHAR(30)
) LANGUAGE plpgsql
AS 
$$
BEGIN
    UPDATE accounts a
    SET job_title = '(Remote) ' || job_title -- At the beginning of the current job title if the account exists.
    FROM addresses ad
    WHERE ad.street = address_street AND ad.town = address_town AND ad.account_id = a.id;
END;
$$;