SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;
SELECT sites.domain_name, leads.first_name, leads.last_name
from sites
JOIN leads ON sites.id = leads.sites_id;
SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leasds ON sites.id = leads.sites_id;
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites on clients.id = sites.clients_id;
SELECT clients.first_name, clients.last_name, SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;